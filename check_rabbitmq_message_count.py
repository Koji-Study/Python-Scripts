import pika

# RabbitMQ 连接信息
rabbitmq_host = 'ip'
rabbitmq_port = 5672
rabbitmq_username = 'username'
rabbitmq_password = 'passwd'
rabbitmq_vhost = 'vhost'
rabbitmq_queue_name = 'queue'

# 检查队列状态
def check_queue_status(connection):
    try:
        channel = connection.channel()
        queue = channel.queue_declare(queue=rabbitmq_queue_name, passive=True)
        count = queue.method.message_count
        return count
    except Exception as e:
        print(f"查看消息队列报错: {str(e)}")
        return -1

# 创建 RabbitMQ 连接
def create_rabbitmq_connection():
    credentials = pika.PlainCredentials(username=rabbitmq_username, password=rabbitmq_password)
    parameters = pika.ConnectionParameters(host=rabbitmq_host, port=rabbitmq_port, virtual_host=rabbitmq_vhost, credentials=credentials)
    connection = pika.BlockingConnection(parameters)
    return connection

# 主监控函数
def monitor_rabbitmq():
    try:
        connection = create_rabbitmq_connection()
        count = check_queue_status(connection)
        print(f"消息队列{rabbitmq_queue_name}有{count}条消息堆积")
        if count >= 3:
            print(f"消息队列{rabbitmq_queue_name}有超过3条消息堆积")
        connection.close()
    except Exception as e:
        print(f"连接RabbitMQ报错: {str(e)}")

if __name__ == "__main__":
    monitor_rabbitmq()
