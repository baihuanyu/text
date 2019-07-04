import time
import  threading

def fun():
    print('start fun')
    time.sleep(2)
    print('end fun ')

print('main thread')

t1 = threading.Thread(target=fun,args=())
# 设置守护线程
#也可以这么设置: t1.daemon = True
t1.setDaemon(True)
t1.start()
#结果只显示了三句话 主线死了之后 end fun 就不再执行