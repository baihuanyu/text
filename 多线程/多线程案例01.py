'''
利用time函数 生成两个函数
计算程序所用时间
'''

import time

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
    text()
    text1()
    print('全部完成时间：',time.ctime())

if __name__ == '__main__':
    main()
    