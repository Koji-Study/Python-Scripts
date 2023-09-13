import socket

def server():
    # 创建 socket对象
    socket_server = socket.socket()
    # 绑定server到指定的ip地址
    socket_server.bind(("localhost", 8888))
    # 监听端口, listen()内写数字，表示可以接受链接的数量
    socket_server.listen(1)
    print("等待客户端连接...")
    # 等待客户端连接，接收到的result是一个二元元组, accept()是一个阻塞的方法，如果没有连接不会往下执行
    result = socket_server.accept()
    print("客户端连接成功")
    connection = result[0]  # 客户端连接对象
    address = result[1]  # 客户端地址信息
    print(f"接收到的客户端连接信息为{address}")
    while True:
        # 接收客户端信息，recv接受的参数是缓冲区大小，一般1024即可，返回的是一个字节数组，bytes对象，不是字符串，再将其decode解码为字符串对象
        data = connection.recv(1024).decode("UTF-8")
        print(f"客户端发来的消息是:{data}")
        # 如果客户端发出"服务器停止"的消息时，服务器将终止
        if data == '服务器停止':
            break
        # 回复消息
        msg = input("请输入回复的消息:")
        # 服务器主动输入exit停止，服务器自己停止自己
        if msg == 'exit':
            msg = "服务器退出，主动停止连接"
            connection.send(msg.encode("UTF-8"))
            break
        connection.send(msg.encode("UTF-8"))
    # 关闭连接
    connection.close()
    socket_server.close()
if __name__ == '__main__':
    server()
