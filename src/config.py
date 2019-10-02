import threading

class Config(object):
    """
    服务器自定义设置
    """
    # set the scrf protect false
    WTF_CSRF_ENABLED = False

    _lock = threading.RLock()



    # #========================aliyun===========================
    # # # 阿里云数据库连接池
    # CONNECTION_POOL = ConnectionDB(ssh_host="47.94.108.28", ssh_username="root", ssh_password='Liuli1617', db_user='root', db_password='123456',
    #                                db_name='fur_model_db', _lock = _lock)





