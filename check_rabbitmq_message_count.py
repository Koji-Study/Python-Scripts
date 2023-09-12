import pika
import requests

# RabbitMQ 连接信息
rabbitmq_host = 'ip'
rabbitmq_port = 5672
rabbitmq_username = 'user'
rabbitmq_password = 'passwd'
rabbitmq_vhost_queue_name_dict = {
    'vhost1': 'queue1',
    'vhost1': 'queue2',
    'vhost3': 'queue2'
}

# 发送通知
def send(content):
    webhook = 'https://webhookurl'
    Header = {'Content-Type': 'application/json; charset=UTF-8'}
    Body = {
        "msgtype": "text",
        "text": {
            "content": "rabbitmq监控告警\n" + \
                       "告警内容：  消息队列有消息堆积" + content
        }
    }
    requests.post(url=webhook, json=Body, headers=Header)
# 检查队列状态
def check_queue_status(connection, queue_name):
    try:
        channel = connection.channel()
        queue = channel.queue_declare(queue=queue_name, passive=True)
        count = queue.method.message_count
        return count
    except Exception as e:
        print(f"检查消息队列报错: {str(e)}")
        return -1

# 创建 RabbitMQ 连接
def create_rabbitmq_connection(vhost):
    credentials = pika.PlainCredentials(username=rabbitmq_username, password=rabbitmq_password)
    parameters = pika.ConnectionParameters(host=rabbitmq_host, port=rabbitmq_port, virtual_host=vhost, credentials=credentials)
    connection = pika.BlockingConnection(parameters)
    return connection

# 主监控函数
def monitor_rabbitmq():
    content = ""
    try:
        for vhost in rabbitmq_vhost_queue_name_dict:
            print(vhost)
            queue_name = rabbitmq_vhost_queue_name_dict.get(vhost)
            connection = create_rabbitmq_connection(vhost)
            count = check_queue_status(connection, queue_name)
            print(f"消息队列{queue_name}有{count}条消息堆积")
            #消息堆积到一定数量时，才记录并告警
            if count >= 30:
                content = content + f"\n{vhost}的队列{queue_name}有超过{count}条消息堆积"
            connection.close()
    except Exception as e:
        print(f"查看RabbitMQ报错: {str(e)}")
    print(content)
    if content != ""：
        send(content)
if __name__ == "__main__":
    monitor_rabbitmq()
