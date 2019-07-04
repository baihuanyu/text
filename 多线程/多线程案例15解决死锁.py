import time
import threading
lock1 = threading.Lock()
lock2 = threading.Lock()

def fun1():
    print('fun1 starting.....')
    # timeout 表示申请锁只等四秒
    lock1.acquire(timeout=4)
    print('fun1 申请了 lock1')
    time.sleep(2)
    print('fun1 正在等待lock2')
    ret = lock2.acquire(timeout=2)
    if ret :
        print('fun1 已经得到了lock2')
        lock2.release()
        print('fun1 释放了lock2')
    else :
        print('fun1 没有申请到lock2')
    lock1.release()
    print('fun1 释放了lock1...')
    print('fun1 done!!!!!')

def fun2():
    print('fun2 start**********')
    lock2.acquire()
    print('fun2 申请了lock2。。。。')
    time.sleep(4)
    print('fun2 d等待lock1')
    lock1.acquire()
    print('fun2申请了lock1。。。。')
    lock1.release()
    print('fun2 释放了lock1')
    lock2.release()
    print('fun2释放了lock2')

    print('fun2 done!!!!!!')
if __name__ == "__main__":

   print("主程序启动..............")
   t1 = threading.Thread(target=fun1, args=())
   t2 = threading.Thread(target=fun2, args=())

   t1.start()
   t2.start()

   t1.join()
   t2.join()

   print("主程序结束..............")