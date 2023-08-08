# -*- coding: UTF-8 -*-

import redis

def addin_blacklist(black_ip, black_time):
    db = redis.Redis(host="10.1.109.184", port=6379, db=0)
    print("需要封禁的IP是：" + black_ip + "封禁时间是: " + black_time)
    # 检查是否在黑名单中
    black_ip = "BlackIP" + black_ip
    if db.exists(black_ip):
        db.expire(black_ip, black_time)
        print("当前IP已经在黑名单中，已更新封禁时间")
    else:
        db.set(black_ip, '')
        db.expire(black_ip, black_time)
        print("添加IP到黑名单中，并设置封禁时间")

def main():
    black_ip = input("请输入需要封禁的IP: ")
    black_time = input("请输入需要封禁的时间(s)：")
    addin_blacklist(black_ip, black_time)

if __name__ == '__main__':
    main()
