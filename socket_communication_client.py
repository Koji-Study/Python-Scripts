import socket

def client():
    # 创建socket对象
    socket_client = socket.socket()
    # 让socket对象socket_client连接到服务端
    result = socket_client.connect(("localhost", 8888))
    # 连接成功的返回值是None
    while result == None:
        msg = input("请输入你要发送的消息：")
        if msg == 'exit':
            msg = "客户端退出，主动停止连接"
            socket_client.send(msg.encode("UTF-8"))
            break
        # 发送消息
        socket_client.send(msg.encode("UTF-8"))
        # 接收消息
        data = socket_client.recv(1024).decode("UTF-8")
        # 收到服务器的终止命令，客户端停止
        if data == "客户端停止":
            break
        print(f"服务器回复的消息为：{data}")

    socket_client.close()

if __name__ == '__main__':
    client()
