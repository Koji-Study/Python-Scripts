import psycopg2

def changedb(db_name, ip_addr):
    selectdb_cmd = "select 'ALTER TABLE ' || table_name || ' OWNER TO operator;' from information_schema.tables where table_schema='public';"
    # 通过connect方法创建数据库连接
    connection = psycopg2.connect(
        dbname=db_name,
        user="username",
        password="paaswd",
        host=ip_addr,
        port="5432"
    )
    connection.autocommit = True
    cursor = connection.cursor()
    print(selectdb_cmd)
    cursor.execute(selectdb_cmd)
    res = cursor.fetchall()
    print(len(res), res)
    for num in range(len(res)):
        try:
            change_tb_owner_cmd = res[num][0]
            cursor.execute(change_tb_owner_cmd)
        except Exception as e:
            print("错误：" + str(e))
            print(res[num][0])
        continue
    cursor.close()
    connection.close()

if __name__ == '__main__':
    db_name = input("请输入需要修改表owner的数据库名：\n")
    ip_addr = input("请输入需要修改表owner的数据库地址：\n")
    changedb(db_name, ip_addr)
