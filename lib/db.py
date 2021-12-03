# coding: UTF-8
# 数据库操作

from lib.logger import log
import pymysql
from config import setting
from read_write import Files


class DB:
    def __init__(self):
        try:
            # 获取数据库配置内容
            data = Files(setting.CONFIG).get_data().get("database", {})
            self.db = pymysql.connect(host=data['host'], user=data['user'], passwd=data['passwd'],
                                      database=data['database'], port=data['port'], charset='utf8')
            # 创建游标对象cursor
            self.cursor = self.db.cursor()
            log.info("数据库连接成功， {}".format(self.db.host_info))
        except ConnectionError as e:
            log.error("数据库连接失败，请检查配置文件")
            raise e

    # 数据查询
    def db_search(self, select_sql):
        try:
            self.cursor.execute(select_sql)  # 执行sql查询
            data = self.cursor.fetchall()  # 获取查询的所有结果
            log.info(f"{select_sql} --> 查询结果是：%s" % list(data))
            return data
        except Exception as e:
            log.warning("数据库查询异常：%s" % str(e))
            self.db.rollback()
        finally:
            self.db_close()

    # 数据更新（增删改）
    def db_update(self, select_sql):
        try:
            self.cursor.execute(select_sql)  # 执行sql语句
            self.db.commit()  # 提交到数据库
            log.info(f"{select_sql} --> 数据更新成功")
        except Exception as e:
            log.warning("数据库更新异常：%s" % str(e))
            self.db.rollback()
        finally:
            self.db_close()

    def db_close(self):
        self.cursor.close()
        self.db.close()


DB = DB()

if __name__ == '__main__':
    sql = "insert  into user_role(id, user_id, role_id, project_id) values (25, 10005, 104, 1);"
    sql1 = "delete from user_role where id=25;"
    sql2 = "update user_role set role_id=110 where id=5"
    DB.db_update(sql2)
    DB.db_search("select * from user_role")
    DB.db_close()
