from flask import Flask
from flask_wtf import CSRFProtect
from src.config import Config

# 创建Flask app实例
app = Flask(__name__)

# csrf防御

CSRFProtect(app)

# 从Python对象（Python类也是一个对象）中导入配置
# 这个能比JSON好一点
app.config.from_object(Config)

# 在app中注册视图函数
import src.backyard.passwordBook.passwordBook_service