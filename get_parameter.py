# -*- coding: utf-8 -*-
import argparse

def get_parameter():
        parser = argparse.ArgumentParser()
        parser.add_argument("-o", "--operation", type=str, help="想要处理的操作")
        parser.add_argument("-m", "--method", type=str, help="方法：POST、GET等")
        parser.add_argument("-a", "--address", type=str, help="想要登录的机器")
        parser.add_argument("-c", "--command", type=str, help="想要执行的命令")
        args = parser.parse_args()
        return args

def main():
        args = get_parameter()
        print(args, args.operation, args.method, args.address, args.command)

if __name__== "__main__":
        main()
