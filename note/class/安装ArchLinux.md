# 安装ArchLinux

-   简介

    -   本教程记录了VMware下 ArchLinux的下载和安装

-   目录

    1.  下载 ArchLinux
    2.  下载 VMware
    3.  安装镜像
    4.  配置环境

-   步骤

    1.  下载 ArchLinux

        -   从Arch官网下载ArchLinux镜像 教程使用2021版本
        -   官网地址: https://archlinux.org/
            ![image-20210207031116172](安装ArchLinux.assets/image-20210207031116172.png)
        -   下载地址: https://archlinux.org/download/ 选择国家进行下载
            ![image-20210207030946912](安装ArchLinux.assets/image-20210207030946912.png)
            ![image-20210207031026160](安装ArchLinux.assets/image-20210207031026160.png)

    2.  下载Vmware

        -   教程使用VMware 16 Pro
        -   参考: https://jingyan.baidu.com/article/ff42efa91e19bd809e2202ee.html 百度经验

    3.  安装镜像

        -   启动VMware 新建虚拟机 选择对应镜像 启动虚拟机 选择第一项启动后 会进入命令行界面
            ![image-20210207040246567](安装ArchLinux.assets/image-20210207040246567.png)

            ![image-20210207031852439](安装ArchLinux.assets/image-20210207031852439.png)

        -   设置字体
            ![image-20210207033943466](安装ArchLinux.assets/image-20210207033943466.png)

        -   验证启动模式 列出efivars目录
            ![image-20210207042512605](安装ArchLinux.assets/image-20210207042512605.png)

        -   验证网络环境 (有可用的网络)
            ![image-20210207042608239](安装ArchLinux.assets/image-20210207042608239.png)

        -   更新系统时钟
            ![image-20210207042708164](安装ArchLinux.assets/image-20210207042708164.png)

        -   查看当前磁盘分配
            ![image-20210207043850496](安装ArchLinux.assets/image-20210207043850496.png)

        -   进行分区以及格式化
            ![image-20210207045653133](安装ArchLinux.assets/image-20210207045653133.png)
            ![image-20210207045736960](安装ArchLinux.assets/image-20210207045736960.png)
            ![image-20210207045754051](安装ArchLinux.assets/image-20210207045754051.png)

        -   安装文件系统 装载盘以及启动交换分区
            ![image-20210207045948426](安装ArchLinux.assets/image-20210207045948426.png)
            ![image-20210207050032862](安装ArchLinux.assets/image-20210207050032862.png)

        -   查看/编辑镜像源
            ![image-20210207050325727](安装ArchLinux.assets/image-20210207050325727.png)
            ![image-20210207050346201](安装ArchLinux.assets/image-20210207050346201.png)

        -   安装基本包
            ![image-20210207050658211](安装ArchLinux.assets/image-20210207050658211.png)
            ![image-20210207050714954](安装ArchLinux.assets/image-20210207050714954.png)

        -   安装基本软件 [自选]
            ![image-20210207052354852](安装ArchLinux.assets/image-20210207052354852.png)

        -   配置系统

            -   生成fstab文件
                ![image-20210207051206907](安装ArchLinux.assets/image-20210207051206907.png)
            -   转到新系统中
                ![image-20210207051554887](安装ArchLinux.assets/image-20210207051554887.png)
            -   设置时区 这里上海为例
                ![image-20210207052033078](安装ArchLinux.assets/image-20210207052033078.png)
                ![image-20210207052216266](安装ArchLinux.assets/image-20210207052216266.png)
            -   设置语言
                -   编辑locale-gen文件 开启对应的语言
                    ![image-20210207052750360](安装ArchLinux.assets/image-20210207052750360.png)
                    ![image-20210207052827248](安装ArchLinux.assets/image-20210207052827248.png)
                    ![image-20210207052906758](安装ArchLinux.assets/image-20210207052906758.png)
                -   设置语言
                    ![image-20210207053132746](安装ArchLinux.assets/image-20210207053132746.png)
                -   设置区域语言
                    ![image-20210207053328357](安装ArchLinux.assets/image-20210207053328357.png)
                -   设置键盘布局
                    ![image-20210207053543331](安装ArchLinux.assets/image-20210207053543331.png)
            -   网络配置
                -   设置主机名
                    ![image-20210207053710290](安装ArchLinux.assets/image-20210207053710290.png)
                -   添加host项目
                    ![image-20210207054354453](安装ArchLinux.assets/image-20210207054354453.png)
            -   配置root用户密码
                ![image-20210207053949474](安装ArchLinux.assets/image-20210207053949474.png)

        -   安装Bootloader

            -   安装grub
                ![image-20210207055853855](安装ArchLinux.assets/image-20210207055853855.png)
            -   

