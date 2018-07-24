import xlogging
logger1=xlogging.Logger('xlogging')
logger1.log('一些日志信息。。。')
logger2=xlogging.Logger('xlogging')
logger2.log('另外一些日志信息。。。')
logger3=xlogging.Logger('xlog')
logger3.log('再来一些日志信息。。。')

print(logger1 is logger2)
print(logger1 is logger3)