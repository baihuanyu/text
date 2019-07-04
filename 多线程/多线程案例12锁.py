import  threading

sum = 0
loopsum = 1000000
#Lock 是大写的L
lock = threading.Lock()
def myAdd():
    global sum , loopsum
    for i in range(1,loopsum):
        # 申请上锁:
        lock.acquire()
        sum += 1
        # 用完锁之后要释放锁
        lock.release()

def myMinu():
    global  sum , loopsum
    for i in range(1,loopsum):
        lock.acquire()
        sum -= 1
        lock.release()

if __name__ == '__main__':
    print('计算中----->总和是 :{0}'.format(sum))
    t = threading.Thread(target=myAdd, args=())
    t.start()
    t1 = threading.Thread(target=myMinu, args=())
    t1.start()
    # 多线程等待
    t.join()
    t1.join()
    print('done 。。。。。{0}'.format(sum))