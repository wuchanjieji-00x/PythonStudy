

import socket
# 1.创建socket对象
socket_client = socket.socket()

# 2. 连接服务器
socket_client.connect(('localhost', 8888)) # connect形参是一个二元元组，第一个元素是服务端的ip地址，第二个元素是链接端口
# 客户端是连接ip地址和端口

# 客户端是先发送再接收
while True:
    # 3.向服务端发送消息
    msg = input('请输入你要向服务端发送的消息：')
    if msg == 'exit':
        break
    socket_client.send(msg.encode('UTF-8'))

    # 4.接收服务端的返回消息
    recv_data = socket_client.recv(1024)
    print(f'服务端返回的消息是：{recv_data.decode("UTF-8")}')

# 关闭客户端
socket_client.close()