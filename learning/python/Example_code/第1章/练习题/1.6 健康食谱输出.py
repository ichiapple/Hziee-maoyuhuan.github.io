# 食谱预设
diet = ['西红柿','花菜','黄瓜','牛排','虾仁']
for x in range(0, 5):
    for y in range (0, 5):
        if not x == y:
            print("{} {}".format(diet[x],diet[y]))