import  time
import threading
#定义最多几个线程使用资源 semaphore s 要大写
semaphore = threading.Semaphore(3)

def fun():
    if semaphore.acquire():
        for i in range(5):
            print(threading.currentThread().getName()+'get sempahore')
            time.sleep(15)
            semaphore.release()
            print(threading.currentThread().getName()+'get semaphore')

for i in range(8):
    t1 =threading.Thread(target=fun)
    t1.start()

