# Linux下遇到的问题以及解决办法

1.  刷新自己的IP地址

    1.  解除自己网卡的IP地址

        >   dhclient -r eth0	# 其中eth0为网卡编号

    2.  使用新的IP地址

        >   dhclient eth0		# 其中eth0为网卡编号

2.  