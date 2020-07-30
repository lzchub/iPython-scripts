import pymysql

"""
    Insert操作
"""
def insert_sql(name,sex):

    # 1.创建连接对象
    conn = pymysql.connect(host='192.168.100.100',
                           port=3306,
                           user='admin',
                           password='admin',
                           db='school',
                           charset='utf8')

    try:
        # 获取游标对象
        with conn.cursor() as cursor:
            # 执行SQL得到结果
            result = cursor.execute('insert into tb_student(stuname,stusex) values(%s,%s)',(name,sex))

            if result == 1:
                print("添加成功")
            # 操作成功执行提交
            conn.commit()

    except pymysql.MySQLError as error:
        print(error)
        # 操作失败，执行回滚
        conn.rollback()

    finally:
        # 关闭连接释放资源
        conn.close()


"""
    delete操作
"""
def delete_sql(id):

    # 1.创建连接对象
    conn = pymysql.connect(host='192.168.100.100',
                           port=3306,
                           user='admin',
                           password='admin',
                           db='school',
                           charset='utf8')

    try:
        # 2.获取游标对象
        with conn.cursor() as cursor:
            # 3.执行SQL得到结果
            result = cursor.execute('delete from tb_student where stuid=%s',(id))

            if result == 1:
                print("删除成功")
            # 4.操作成功执行提交
            conn.commit()

    except pymysql.MySQLError as error:
        print(error)
        # 5.操作失败，执行回滚
        conn.rollback()

    finally:
        # 6.关闭连接释放资源
        conn.close()


"""
    update
"""
def update_sql(id,name,sex):

    # 1.创建连接对象
    conn = pymysql.connect(host='192.168.100.100',
                           port=3306,
                           user='admin',
                           password='admin',
                           db='school',
                           charset='utf8')

    try:
        # 获取游标对象
        with conn.cursor() as cursor:
            # 执行SQL得到结果
            result = cursor.execute('update tb_student set stuname=%s,stusex=%s where stuid=%s',(name,sex,id))

            if result == 1:
                print("更新成功")
            # 操作成功执行提交
            conn.commit()

    except pymysql.MySQLError as error:
        print(error)
        # 操作失败，执行回滚
        conn.rollback()

    finally:
        # 关闭连接释放资源
        conn.close()

"""
    select操作
"""
def select_sql():
    pass

if __name__ == '__main__':
    # insert_sql('张无忌',1)

    # delete_sql(1014)

    update_sql(1001,'金毛丝王',1)










