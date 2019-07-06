# 客户端案例
import socket


def clientfunc():
    '''模拟一个客户端'''
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    text = 'i love xiayuling'
    # 发送
    data = text.encode()

    sock.sendto(data, ('127.0.0.1', 8000))

    data, addr = sock.recvfrom(200)

    data = data.decode
    print(data)


if __name__ == '__main__':
    clientfunc()