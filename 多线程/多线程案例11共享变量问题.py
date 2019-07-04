
# 导入多线程
import threading

sum = 0
loopsum = 1000000

def myAdd():
    '''定义一个sum每次加一的函数'''
    global  sum , loopsum
    for i in range(1,loopsum) :
        sum +=1

def myMinu():
    '''定义一个函数 sum每次减一'''
    global  sum ,loopsum
    for i in range(1,loopsum):
        sum -=1

if __name__ == '__main__':
    # 改成多线程：
    print('计算中----->总和是 :{0}'.format(sum))
    t = threading.Thread(target=myAdd,args=())
    t.start()
    t1 =threading.Thread(target=myMinu,args=())
    t1.start()
    # 多线程等待
    t.join()
    t1.join()
    print('done 。。。。。{0}'.format(sum))
 # 出现这个结果原因 1。 + - 不是原子操作 ， 所以在共享变量时候就发生了冲突
