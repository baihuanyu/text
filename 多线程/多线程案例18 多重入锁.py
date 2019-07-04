import threading
import time

class my(threading.Thread):
    def run(self):
        global num
        time.sleep(1)
        if mutex.acquire(1):
            num = num +1
            msg = self.name + 'set num to ' +str(num)
            print(msg)
            mutex.acquire()
            mutex.release()
            mutex.release()
num = 0
# Rlock 表示可重入锁
mutex = threading.RLock()

def testTh():
    for i in range(5):
        t = my()
        t.start()



if __name__ == '__main__':
    testTh()
