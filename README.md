```
     ____      _   ___ ____  _        __
    / ___| ___| |_|_ _|  _ \(_)_ __  / _| ___
   | |  _ / _ \ __|| || |_) | | '_ \| |_ / _ \
   | |_| |  __/ |_ | ||  __/| | | | |  _| (_) |
    \____|\___|\__|___|_|   |_|_| |_|_|  \___/

                   By:R3start

usage: GetIPinfo.py [-h] [-i IP] [-t TIME] [-f FILE] [-o OUT]

optional arguments:
  -h, --help            show this help message and exit
  -i IP, --ip IP        IP
  -t TIME, --time TIME  interval time default 3s
  -f FILE, --file FILE  IP List
  -o OUT, --out OUT     Save File
  
```



![Ipinfo](https://raw.githubusercontent.com/r35tart/GetIPinfo/master/ip.png)

### 扫描单个IP

```
python3 GetIPinfo.py -i 192.168.0.1
```

### 扫描整个 C 段

```
python3 GetIPinfo.py -i 192.168.0.1/24
```

### 读取指定文本扫描（文本一个 IP 一行，不带端口）

```
python3 GetIPinfo.py -f ip.txt
```

### 其他

```
-t 每个 IP 连接的时长，默认三秒，网络不好的情况下建议调高
-o 保存文件
   每次扫描后都会将结果到当前文件夹，文件名为: 年月日时分秒_scan.log
```



### 原理:

[1. Nicolas Delhaye : The OXID Resolver [Part 1] – Remote enumeration of network interfaces without any authentication](https://airbus-cyber-security.com/the-oxid-resolver-part-1-remote-enumeration-of-network-interfaces-without-any-authentication/)
