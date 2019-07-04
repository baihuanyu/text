import time
import threading

def text(in1):
    print('当前时间是:',time.ctime())
    #把参数打印出来
    print('我是参数',in1)
    # 程序睡眠 单位是秒
    time.sleep(4)
    print('现在的时间是' ,time.ctime())

def text1(in1,in2) :
    print('当前时间是:', time.ctime())
    #打印参数
    print('我是参数',in1,'和参数',in2)
    # 程序睡眠 单位是秒
    time.sleep(2)
    print('现在的时间是', time.ctime())

def main():
    '''创建一个包工头函数'''
    print('开始时间：',time.ctime())
    # 多线程生成 threading.thread生成实例
    t1 = threading.Thread(target=text,args=('baihuanyu',))
    # 程序开始
    t1.start()

    t2 = threading.Thread(target=text1,args=('baihuanyu','xiayuling'))
    t2.start()
    # 假如join
    t1.join()
    t2.join()
    print('全部结束时间： ',time.ctime())

if __name__ == '__main__':
    main()
    while True :
        time.sleep(10)
