#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File	:   GetIPinfo.py
@Time	:   2020/07/17 03:56:05
@Author  :   R3start 
@Version :   1.0
'''

# 脚本介绍
# 扫描获取单个 IP 或者整个 C 段或指定 IP 列表的网卡信息，寻找多网卡主机方便内网跨网段渗透避免瞎打找不到核心网
#
# 原理:https://airbus-cyber-security.com/the-oxid-resolver-part-1-remote-enumeration-of-network-interfaces-without-any-authentication/


import sys
import time
import eventlet
import argparse
from impacket.dcerpc.v5 import transport
from impacket.dcerpc.v5.rpcrt import RPC_C_AUTHN_LEVEL_NONE
from impacket.dcerpc.v5.dcomrt import IObjectExporter


def main(target_ip,outfile):
	try :
		authLevel = RPC_C_AUTHN_LEVEL_NONE
		infotitle = "[*] Retrieving network interface of %s " % (target_ip)
		print(infotitle)
		stringBinding = r'ncacn_ip_tcp:%s' % target_ip
		rpctransport = transport.DCERPCTransportFactory(stringBinding)
		portmap = rpctransport.get_dce_rpc()
		portmap.set_auth_level(authLevel)
		portmap.connect()
		objExporter = IObjectExporter(portmap)
		bindings = objExporter.ServerAlive2()
		if bindings :
			outfile = open(outfile,'a+',encoding='UTF-8')
			outfile.write(infotitle + "\n")
			for binding in bindings:
				NetworkAddr = binding['aNetworkAddr']
				print("Address: " + NetworkAddr)
				outfile.write("Address: " + NetworkAddr + "\n")
			print("--------------------------------------")
			outfile.write("--------------------------------------\n")
			outfile.close()
	except Exception as e:
		print(e)


if __name__ == "__main__":
	banner = '''
     ____      _   ___ ____  _        __       
    / ___| ___| |_|_ _|  _ \(_)_ __  / _| ___  
   | |  _ / _ \ __|| || |_) | | '_ \| |_ / _ \ 
   | |_| |  __/ |_ | ||  __/| | | | |  _| (_) |
    \____|\___|\__|___|_|   |_|_| |_|_|  \___/ 
                                            
                   By:R3start
	'''
	print(banner)
	parser = argparse.ArgumentParser()
	parser.add_argument('-i','--ip',help='IP')
	parser.add_argument('-t','--time',help='interval time default 3s',default=3)
	parser.add_argument('-f','--file', help='IP List')
	parser.add_argument('-o','--out', help='Save File')
	args = parser.parse_args()
	eventlet.monkey_patch()
	ip = args.ip
	times = args.time
	lists = args.file
	outfile = "%s_scan.txt" % (time.strftime("%Y%m%d%H%M%S", time.localtime())) if not args.out else args.out

	if not ip and not lists :
		parser.print_help()
		sys.exit(1)
	if ip : 
		if "1/24" in ip :
			i = 1
			while(i <= 255):
				cip = args.ip[:-4] + str(i)
				with eventlet.Timeout(int(times),False):
					main(cip,outfile)
				i += 1
	if lists :
		for ip in open(lists):
			with eventlet.Timeout(int(times),False):
				main(ip.rstrip(),outfile)
	else:
		main(ip,outfile)
