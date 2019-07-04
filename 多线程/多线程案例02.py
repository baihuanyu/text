import time
import _thread as thread # 这个是不常用的

def text():
    print('当前时间是:',time.ctime())
    # 程序睡眠 单位是秒
    time.sleep(4)
    print('现在的时间是' ,time.ctime())

def text1() :
    print('当前时间是:', time.ctime())
    # 程序睡眠 单位是秒
    time.sleep(2)
    print('现在的时间是', time.ctime())

def main():
    print('开始时间',time.ctime())
    #启动一个新线程 thread.start_new_thread
    #总共三个线程 一个主线 两个新线
    #类似之前都该我干 到这里我叫了2个人来干
    # 后面的括号必须有 表示参数
    thread.start_new_thread(text,())

    thread.start_new_thread(text1, ())

    print('全部完成时间：',time.ctime())
if __name__ == '__main__':
    main()
    # 如果不用while 两个新线程只是开始了 并没有运行
    # 而主线直接就完成了 没有等待 新线程工作
    while True :
        time.sleep(1)