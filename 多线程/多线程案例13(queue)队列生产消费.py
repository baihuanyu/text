import queue
import time
import threading
# 生产者
class Producer(threading.Thread):
    def run(self):
        global  queue
        count = 0
        while True :
            if queue.qsize()< 1000:
                for i in range(100):
                    count += 1
                    msg = '产品-->' + str(count)
                    # put 是往queue里面放东西
                    queue.put(msg)
                    print(msg)
                time.sleep(0.5)
#消费者
class Consumer(threading.Thread):
    def run(self):
        global queue
        while True :
            if queue.qsize()>100:
                for i in range(3):
                    #get 是从queue中取出一个值
                    msg = self.name +' 消费了' + queue.get()
                    print(msg)
                time.sleep(1)

if __name__ == '__main__':
    queue = queue.Queue()

    for i in range(500):
        queue.put('初始产品' + str(i))
    #生成两个生产者
    for i in range(2):
        p = Producer()
        p.start()
    # 生成五个消费者
    for i in range(5):
        c = Consumer()
        c.start()