# Datetime 相关类
#   Date类：用来表示“年月日”的日期
#   Time类：用来表示某天的时间，独立于日期
#   Datetime类：包含来自date和time的所有信息的单一对象
#   Timedelta类：用来表示两个date或time的时间间隔
import datetime
now = datetime.datetime.now()
print(now)
today = datetime.date.today()
print(today)
d1 = datetime.date(2022, 6, 1)
print(d1)
print(type(d1))
print(d1.year)
print(d1.month)
print(d1.day)
t1 = datetime.time()
print(t1)
print(type(t1))
# t2 = datetime.time(11, 12, 23)
t2 = datetime.datetime.now()
print(t2)
print(t2.hour)
print(t2.minute)
print(t2.second)
dt1 = datetime.datetime(2022, 6, 17, 11, 16, 43)
print(dt1)
# timestamp()函数可以将时间转换成时区
print(dt1.timestamp())
today = datetime.date.today()
now = datetime.datetime.now()
dt2 = datetime.datetime(2022, 6, 12, 11, 30, 14)
delta1 = now - dt2
print(delta1)
# 日期和时间的格式化
# strftime 方法
# 熟悉格式化编码：%Y %m %d %H:%M:%s
now = datetime.datetime.now()
print(now.strftime('%Y-%m-%d %H:%M:%s'))
print(now.strftime('%Y-%b-%d %H:%M:%s'))
