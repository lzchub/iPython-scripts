#!/usr/bin/python3
"""
    author: chuan
    date  : 2020-08-04
    used  : 获取nginx日志访问量前十的IP地址
"""


LOGFILE='/var/log/httpd/access_log'

IP = {}

# 打开文件
with open(LOGFILE) as file:
    # file 获取整个文件，以行为单位的列表
    for f in file.readlines():
        # strip去掉头尾空白
        i = f.strip().split()[0]
        
        # 统计每个IP的访问数并以字典存储
        if i in IP.keys():
            IP[i] += 1
        else:
            IP[i] = 1

# 以IP出现的次数排序返回对象为list
ip = sorted(IP.items(),key=lambda v:v[1],reverse=True)

# 打印排名前三的IP
print(ip[0:3:1])

