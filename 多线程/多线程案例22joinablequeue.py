import multiprocessing
import  time

def consumer(input_q):
    print('Into consumer ', time.ctime())
    while True:
        #处理项
        item = input_q.get()
        print('pull' , item,'out of q') # 此次替换为有用的工作
        input_q.task_done()# 发出信号通知任务完成
    print(' Out of consumer', time.ctime())

def producer(sequence,output_q):
    print('Into producer: ',time.ctime())
    #sequence表示一个仓库
    for i in sequence:
        output_q.put(i)
        print('put ',i ,' in q')
    print('Out of producer',time.ctime())

if __name__ == '__main__':
    q = multiprocessing.JoinableQueue()
    p = multiprocessing.Process(target=consumer,args=(q,))
    p.start()
    sequence = [1,2,3,4]
    producer(sequence, q)
    # 等待所有项被处理
    q.join()

