import  multiprocessing
import time

class Cprocess(multiprocessing.Process):
    '''
    1.两个函数比较重要
    __INIT__构造函数
    run
    '''
    def __init__(self,interval):
        # 一般都是要继承父类的构造函数
        super().__init__()
        self.interval = interval
    def run(self):
        while True :
            print('now the time is %s' % time.ctime())
            time.sleep(self.interval)
if __name__ == '__main__':
    p = Cprocess(3)
    p.start()
    while True :
         print('sleeping!!!!!!!!!!!')
         time.sleep(1)