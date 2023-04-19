# ! -*- coding: utf-8 -*-
#检查doris集群状态，宕机重启，并发送企业微信消息
import requests
import paramiko
import time
url = 'http://ip:port/api/backends'
def sent(ip, content):
    webhook = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=webhookofqiyeweixin'
    mHeader = {'Content-Type': 'application/json; charset=UTF-8'}
    mBody = {
        "msgtype": "text",
        "text": {
            "content": "Doris监测告警\n" + \
                       "告警内容： doris的节点" + ip + "挂了！\n" + \
                       "重启结果： " + content
        }
    }
    requests.post(url=webhook, json=mBody, headers=mHeader)


def restart_doris(restart_list):
    for num in range(len(restart_list)):
        doris_node = restart_list[num]
        ssh_client = paramiko.SSHClient()
        # 通过这个set_missing_host_key_policy方法用于实现登录是需要确认输入yes，否则保存
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=doris_node, port=22, username="user", password="paaswd")
        ssh_client.exec_command("cd /mnt/data/module/apache-doris-1.2.0/be;./bin/start_be.sh --daemon")
        #print(stdout.read().decode(),stdio.read().decode(),stderr.read().decode())
        ssh_client.close()

def check():
    ip = ''
    request = requests.session()
    request.auth = ('user', 'passwd')
    result = request.get(url, headers={'Cache-Control': 'no-cache'})
    result = result.json().get('data').get('backends')
    ip_list = [0] * len(result)
    alive_list = [0] * len(result)
    notalive_list = []
    for num in range(len(result)):
        ip_list[num] = result[num].get('ip')
        alive_list[num] = result[num].get('is_alive')
        if alive_list[num] !=  True:
            ip = ip + '★' + ip_list[num]
            notalive_list.append(ip_list[num])
    print(notalive_list)
    return ip, notalive_list

if __name__ == '__main__':
    while True:
        ip, notalive_list = check()
        print(ip, notalive_list)
        if ip != '':
            restart_doris(notalive_list)
            time.sleep(10)
            ip1, ip_list1, notalive_list1 = check()
            print(ip1, ip_list1, notalive_list1)
            if ip1 == '':
                content = ip + '自动重启成功！'
            else:
                content = ip1 + '自动重启失败！请检查！'
            sent(ip, content)
        time.sleep(60)
