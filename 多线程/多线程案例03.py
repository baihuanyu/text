import time
import _thread as thread # 这个是不常用的

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

    thread.start_new_thread(text,('baihuanyu',))
    thread.start_new_thread(text1,('baihuanyu','xiayuling'))
    print('全部结束时间： ',time.ctime())

if __name__ == '__main__':
    main()
    while True :
        time.sleep(10)