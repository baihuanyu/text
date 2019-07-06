# 服务器案例
import socket


def serverfunc():
    '''模拟服务器函数'''
    # 建立socket
    soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # socket.AE_INET 表示使用ipv4协议
    # socket.SOCK_DGRAM 使用UDP通信

    # 绑定ip和port
    # 127.0.0.1 这个ip地址代表机器本身
    # 地址是一个元组
    addr = ('127.0.0.1', 8000)
    soc.bind(addr)

    # 接受对方消息
    # 等待方式为死等， 没有其他可能性
    # recvfrom 接受返回值的一个 元组 ，前一项表示数据，后一项表示地址
    # 参数含义是缓冲区大小
    data, addr = soc.recvfrom(500)

    # 发送过来消息是bytes，
    # decode 默认参数UTF-8
    text = data.decode()

    # 给对方反馈的消息
    rsp = '我不饿'
    # 发送的数据要bytes  需要编码
    data = rsp.encode()
    # 发送用sendto 地址addr之前已经得到
    soc.sendto(data, addr)


if __name__ == '__main__':
    print("Starting server.........")
    serverfunc()
    print("Ending server........")