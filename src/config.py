import threading
from src.backyard.db.ConnectionPool import ConnectionPoolV1


class Config(object):
    """
    服务器自定义设置
    """
    # set the scrf protect false
    WTF_CSRF_ENABLED = False

    _lock = threading.RLock()
    # 数据库连接池（本地）
    CONNECTION_POOL = ConnectionPoolV1(
        host="127.0.0.1", port=3306, user="password_book", passwd="123456", db="passwordbook_db", charset="utf8mb4"
        , _lock=_lock
    )
