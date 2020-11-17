for i in range(1,10):
    for j in range(1, i+1):
        # 格式为 i*j=k 的形式 为了保持一致 前面使用了补零 结尾使用空格分割
        print("{}*{}={:02}".format(j,i,j*i), end=' ')
    print("")