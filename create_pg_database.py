#apt install libpq-dev
#pip3 install psycopg2
#使用root用户创建数据库，然后给opreator用户授权

import psycopg2


def createdb(db_name):
    createdb_cmd = 'CREATE DATABASE ' + db_name + ';'
    print("正在创建数据库：" + db_name)
    # 通过connect方法创建数据库连接
    connection = psycopg2.connect(
        dbname="postgres",
        user="root",
        password="paaswd",
        host="0.0.0.0",
        port="5432"
    )
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(createdb_cmd)
        print("创建数据库完成：" + db_name)
        result = 1
    except Exception as e:
        result = 0
        print("错误：" + str(e))
    cursor.close()
    connection.close()
    return result

def grantpri(db_name):
    grantpri_cmd1 = 'GRANT ALL PRIVILEGES ON DATABASE "' + db_name + '" TO opreator;'
    grantpri_cmd2 = 'GRANT ALL PRIVILEGES ON all tables in schema public TO opreator;'
    print("正在给opreator用户授权")
    connection = psycopg2.connect(
        dbname=db_name,
        user="root",
        password="passwd",
        host="0.0.0.0",
        port="5432"
    )
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(grantpri_cmd1)
        cursor.execute(grantpri_cmd2)
    except Exception as e:
        print("错误：" + str(e))
    cursor.close()
    connection.close()
    print("给opreator用户授权完成")

if __name__ == '__main__':
    db_name = input("请输入需要创建的数据库名：\n")
    result = createdb(db_name)
    if result == 1:
        grantpri(db_name)
    else:
        print("数据库创建出现错误，请检查!")
