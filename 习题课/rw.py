import  matplotlib.pyplot as plt
from rand import  RandomWalk

while True :
    rw = RandomWalk()
    # 实例化调用
    rw.fillwalk()
    plt.scatter(rw.x, rw.y, s=20)
    # 给点上颜色
    point_numbers = list(range(rw.num))
    plt.scatter(rw.x,rw.y,c=point_numbers,cmap=plt.cm.Blues,
        edgecolor = 'none', s= 15)
    plt.show()
    keep_running = input('需要再来一次随机漫步吗？y/n :')
    if keep_running == 'n':
        break