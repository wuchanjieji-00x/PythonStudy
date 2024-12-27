

import socket
# 1.创建socket对象
socket_server = socket.socket()

# 2.绑定ip地址和端口
socket_server.bind(('localhost', 8888))  # 将socket_server绑定在本机的8888端口
# 服务端是绑定ip地址和端口

# 3.监听端口
socket_server.listen(1) # listen方法中的形参接收一个int参数，表示链接的数量

# 4.等待客户端链接
# result_tuple: tuple = socket_server.accept()  # accept返回一个二元元组(链接对象, 客户端地址)
# conn = result_tuple[0]  # 第一个元素：客户端和服务端的链接对象
# addr = result_tuple[1]  # 第二个元素：客户端的地址信息
# 等价于：
conn, addr = socket_server.accept() # 可以通过变量1, 变量2 = socket_server.accept()这种写法，直接接收二元元组的两个元素
# 注意：accept()是阻塞方法，等待客户端的链接，如果没有客户端链接，就卡在这一行
print(f'接收到了客户端的链接，客户端的信息是：{addr}')

# 服务端是先接收再发送
# 5.接收客户端信息，要使用客户端和服务端的本次链接对象，而非socket_server对象
while True:
    data: str = conn.recv(1024).decode('UTF-8')
# recv接收的参数是buffersize(缓冲区大小)，一般给1024即可
# recv方法的返回值是一个字节数组，也就是bytes对象，不是字符串，可以通过UTF-8将其解码为字符串
# recv同样也是阻塞方法，如果客户端不发消息，就会一直卡在这里
    print(f'客户端发来的消息是：{data}')

# 6.向客户端发送回复消息
    msg = input('请输入你要向客户端回复的消息：')
    if msg == 'exit':  # 退出循环的标记
        break  # 跳出循环，执行循环体下面的代码
    conn.send(msg.encode('UTF-8'))  # 将字符串通过UTF-8编码成字节数组对象
# 7.关闭链接
conn.close()  # 关闭此次客户端和服务端的链接对象
socket_server.close() # 关闭服务端，不再接收客户端的消息了
