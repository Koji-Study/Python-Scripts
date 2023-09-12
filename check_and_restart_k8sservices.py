import kubernetes
import requests
import paramiko
#service_name：[cluser_name,service_namespece,service_url]
services_dict = {
    "tomcat": ["k8s-cluser1", "testhao", "https://www.example.com"]
}
k8sc1_client = {
    "host": "ip",
    "user": "username",
    "passwd": "userpasswd"
}
k8sc2_client = {
    "host": "ip",
    "user": "username",
    "passwd": "userpasswd"
}
def send(cluster, service, namespace, url, pod_list_str):
    webhook = 'webhookurl'
    Header = {'Content-Type': 'application/json; charset=UTF-8'}
    Body = {
        "msgtype": "text",
        "text": {
            "content": "辅助服务监控告警\n" + \
                       "告警内容： " + cluster + "集群" + namespace + "下的" + service + "无法访问，已重启\n" + \
                       "服务地址： " + url + "\n" + \
                       "重启结果： " + pod_list_str + "Pod已删除重启"
        }
    }
    requests.post(url=webhook, json=Body, headers=Header)

def restart_service(cluster, service, namespace, url):
    pod_list = []
    pod_list_str = ""
    if services_dict.get(service)[0] == "k8s-c1":
        client = k8sc1_client
    elif services_dict.get(service)[0] == "qke-c1":
        client = qkec1_client
    #获取config文件
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=client.get("host"), port=22, username=client.get("user"), password=client.get("passwd"))
    stdin, stdout, stderr = ssh_client.exec_command("cat ~/.kube/config")
    config = stdout.read().decode()
    ssh_client.close()
    with open('k8sconfig', 'w') as f:
        f.write(config)
    #连接k8s集群
    kubernetes.config.load_kube_config("k8sconfig")
    k8s_client = kubernetes.client.CoreV1Api()
    #查看pod并根据service名字匹配pod
    pods = k8s_client.list_namespaced_pod(namespace)
    for pod in pods.items:
        if service in pod.metadata.name:
            print(pod.metadata.name)
            try:
                #删除掉匹配上的Pod
                k8s_client.delete_namespaced_pod(name=pod.metadata.name, namespace=namespace, body=kubernetes.client.V1DeleteOptions())
                print(f"Pod {pod.metadata.name} 已成功删除。")
                pod_list.append(pod.metadata.name)
            except kubernetes.client.rest.ApiException as e:
                print(f"删除Pod时出错：{e}")
        else:
            print(f"pod name{pod.metadata.name} 不匹配")
    if len(pod_list) != 0:
        for pod in pod_list:
            print(pod)
            pod_list_str = pod_list_str + "★" + pod
    print(pod_list_str)
    send(cluster, service, namespace, url, pod_list_str)

def check():
    for service in services_dict:
        cluster = services_dict.get(service)[0]
        namespace = services_dict.get(service)[1]
        url = services_dict.get(service)[2]
        print(url)
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print("service is available")
            else:
                print("restart service")
                restart_service(cluster, service, namespace, url)
        except Exception as e:
            print("请求出错")
            print(e)

if __name__ == '__main__':
    check()
