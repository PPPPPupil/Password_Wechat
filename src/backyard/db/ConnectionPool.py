import pymysql
from threading import RLock
from DBUtils.PooledDB import PooledDB
from sshtunnel import SSHTunnelForwarder

class ConnectionPoolV1(object):
    def __init__(self, host: str, port: int, user: str, passwd: str, db: str, charset: str,_lock):
        """
        数据库连接池 V1版本
        :param host: 要连接的主机IP地址，比如 "127.0.0.1"
        :param port: 要连接的主机端口，比如 3306
        :param user: 数据库用户名，比如 "root"
        :param passwd: 数据库用户密码，比如 "123456"
        :param db: 要使用的数据库名，比如 "my_database"
        :param charset: 默认字符集，比如 "utf8mb4"
        """
        DeprecationWarning("现在V1版本的数据库连接池由于没有加锁会出错，被迫加了锁，性能降低")
        self.conn = PooledDB(
            creator=pymysql, mincached=1, maxcached=20, host=host, port=port, user=user, passwd=passwd, db=db,
            charset=charset
        ).connection()
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        self._lock = _lock

    def insert(self, sql, arg_tuple) -> int:
        """
        执行插入SQL语句
        :param sql: SQL模板语句
        :param arg_tuple: SQL模板语句参数
        :return: 被影响的行数
        """
        # with self._lock:
        #     _ = self.cur.execute(sql, arg_tuple)
        #     self.conn.commit()
        self._lock.acquire()
        _ = self.cur.execute(sql, arg_tuple)
        self.conn.commit()
        self._lock.release()
        return _

    def delete(self, sql, arg_tuple) -> int:
        """
        执行删除SQL语句
        :param sql: SQL模板语句
        :param arg_tuple: SQL模板语句参数
        :return: 被影响的行数
        """
        # with self._lock:
        #     _ = self.cur.execute(sql, arg_tuple)
        #     self.conn.commit()
        self._lock.acquire()
        _ = self.cur.execute(sql, arg_tuple)
        self.conn.commit()
        self._lock.release()
        return _

    def update(self, sql, arg_tuple) -> int:
        """
        执行更改SQL语句
        :param sql: SQL模板语句
        :param arg_tuple: SQL模板语句参数
        :return: 被影响的行数
        """
        # with self._lock:
        #     _ = self.cur.execute(sql, arg_tuple)
        #     self.conn.commit()
        self._lock.acquire()
        _ = self.cur.execute(sql, arg_tuple)
        self.conn.commit()
        self._lock.release()
        return _

    def fetch_all(self, sql: str, arg_tuple: tuple):
        """
        执行查询语句并返回所有查询结果（如果有的话），若无结果返回空tuple
        :param sql: SQL模板语句，比如 SELECT `id` FROM `tbl_user` WHERE `tbl_user`.`user_name`=%s;
        :param arg_tuple: 构建真正查询语句时，传递给SQL模板语句的tuple，比如('alice',)
        :return: 查询结果list，list中的每一个元素（dict类型）对应数据库里的一行
        """
        # with self._lock:
        #     self.cur.execute(sql, arg_tuple)
        self._lock.acquire()
        self.cur.execute(sql, arg_tuple)
        self.conn.commit()
        self._lock.release()
        return self.cur.fetchall()

    def fetch_one(self, sql: str, arg_tuple: tuple):
        """
        执行查询语句并返回第一条查询结果（如果有的话）,若无结果返回 * None *
        :param sql: SQL模板语句，比如 SELECT `id` FROM `tbl_user` WHERE `tbl_user`.`user_name`=%s;
        :param arg_tuple: 构建真正查询语句时，传递给SQL模板语句的tuple，比如('alice',)
        :return: 查询结果dict
        """
        # with self._lock:
        #     self.cur.execute(sql, arg_tuple)
        self._lock.acquire()
        self.cur.execute(sql, arg_tuple)
        self.conn.commit()
        self._lock.release()
        return self.cur.fetchone()

    def close(self):
        """关闭数据库连接池，估计暂时用不到"""
        self.conn.close()
        self.cur.close()


class ConnectionDB(object):
    def __init__(self ,ssh_host: str, ssh_username: str, ssh_password: str, db_user: str,
                 db_password: str, db_name: str,_lock):

        self.server = SSHTunnelForwarder(
            ssh_address_or_host=(ssh_host, 22),
            ssh_username=ssh_username,
            ssh_password=ssh_password,
            remote_bind_address=('localhost', 3306),
        )
        self.server.start()

        self.host = '127.0.0.1'
        self.port = self.server.local_bind_port

        self.user = db_user
        self.password = db_password
        self.db = db_name

        self._lock = _lock

    def insert(self, sql, arg_tuple) -> int:
        """
        执行插入SQL语句
        :param sql: SQL模板语句
        :param arg_tuple: SQL模板语句参数
        :return: 被影响的行数
        """
        # with self._lock:
        #     _ = self.cur.execute(sql, arg_tuple)
        #     self.conn.commit()

        self._lock.acquire()
        conn = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password, db=self.db)
        cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
        _ = cur.execute(sql, arg_tuple)
        conn.commit()
        self._lock.release()
        return _

    def delete(self, sql, arg_tuple) -> int:
        """
        执行删除SQL语句
        :param sql: SQL模板语句
        :param arg_tuple: SQL模板语句参数
        :return: 被影响的行数
        """
        # with self._lock:
        #     _ = self.cur.execute(sql, arg_tuple)
        #     self.conn.commit()
        self._lock.acquire()
        conn = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password, db=self.db)
        cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
        _ = cur.execute(sql, arg_tuple)
        conn.commit()
        self._lock.release()
        return _

    def update(self, sql, arg_tuple, commit=False) -> int:
        """
        执行更改SQL语句
        :param sql: SQL模板语句
        :param arg_tuple: SQL模板语句参数
        :return: 被影响的行数
        """
        # with self._lock:
        #     _ = self.cur.execute(sql, arg_tuple)
        #     self.conn.commit()
        self._lock.acquire()
        conn = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password, db=self.db)
        cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
        _ = cur.execute(sql, arg_tuple)
        if commit :
            conn.commit()
        self._lock.release()
        return _

    def fetch_all(self, sql: str, arg_tuple: tuple):
        """
        执行查询语句并返回所有查询结果（如果有的话），若无结果返回空tuple
        :param sql: SQL模板语句，比如 SELECT `id` FROM `tbl_user` WHERE `tbl_user`.`user_name`=%s;
        :param arg_tuple: 构建真正查询语句时，传递给SQL模板语句的tuple，比如('alice',)
        :return: 查询结果list，list中的每一个元素（dict类型）对应数据库里的一行
        """
        # with self._lock:
        #     self.cur.execute(sql, arg_tuple)
        self._lock.acquire()
        conn = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password, db=self.db)
        cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cur.execute(sql, arg_tuple)
        _ = cur.fetchall()
        conn.commit()
        self._lock.release()
        return _

    def fetch_one(self, sql: str, arg_tuple: tuple):
        """
        执行查询语句并返回第一条查询结果（如果有的话）,若无结果返回 * None *
        :param sql: SQL模板语句，比如 SELECT `id` FROM `tbl_user` WHERE `tbl_user`.`user_name`=%s;
        :param arg_tuple: 构建真正查询语句时，传递给SQL模板语句的tuple，比如('alice',)
        :return: 查询结果dict
        """
        # with self._lock:
        #     self.cur.execute(sql, arg_tuple)
        self._lock.acquire()
        conn = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password, db=self.db)
        cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cur.execute(sql, arg_tuple)
        _ = cur.fetchone()
        conn.commit()
        self._lock.release()
        return _
