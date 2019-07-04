from random import choice
import matplotlib.pyplot as plt


class RandomWalk():
    '''创建一个随机漫步的数据的类'''

    def __init__(self, num=5000):
        # 初始随机漫步的属性
        self.num = num

        # 所有随机漫步都是从原点开始
        self.x = [0]
        self.y = [0]

    def fillwalk(self):
        # 不断漫步知道列表表达到一定长度
        while len(self.x) < self.num:
            # 觉得前进的方向和距离
            x_dirction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_dirction * x_distance

            y_dirction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4, 5])
            y_step = y_distance * y_dirction

            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            # 计算下一个点的x和y值
            # sefl.x[-1]表示列表的最后一个数 -1 是索引
            next_x = self.x[-1] + x_step
            next_y = self.y[-1] + y_step

            self.x.append(next_x)
            self.y.append(next_y)


rw = RandomWalk()
# 实例化调用
rw.fillwalk()
plt.scatter(rw.x, rw.y, s=20)
plt.show()