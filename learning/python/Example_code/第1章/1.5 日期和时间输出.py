# 引用datetime库
from datetime import datetime

# 获得当前的时间和日期
now = datetime.now()

# 打印当前的时间和日期
print(now)

# 输出其中的日期部分 输出的格式为 月/日/年
print(now.strftime("%x"))

# 输出其中的时间部分 输出的格式为 时/分/秒
print(now.strftime("%X"))
