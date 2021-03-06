# coding:utf-8
import redis
import logging

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_wtf import CSRFProtect
from config import config_map
from logging.handlers import RotatingFileHandler

from ihome.utils.commons import ReConverter

db = SQLAlchemy()
session = Session()
csrf = CSRFProtect()
redis_store = None

# 配置日志信息
# 设置日志的记录等级
logging.basicConfig(level=logging.INFO)
# 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024 * 1024 * 100, backupCount=10)
# 创建日志记录的格式                 日志等级    输入日志信息的文件名 行数    日志信息
formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
# 为刚创建的日志记录器设置日志记录格式
file_log_handler.setFormatter(formatter)
# 为全局的日志工具对象（flask app使用的）添加日记录器
logging.getLogger().addHandler(file_log_handler)


def create_app(config_name):
    """
    create flask object
    :param config_name:
    :return app:
    """
    app = Flask(__name__)
    config_class = config_map.get(config_name, "develop")
    # name get config class
    app.config.from_object(config_class)

    db.init_app(app)
    session.init_app(app)
    csrf.init_app(app)

    global redis_store
    redis_store = redis.StrictRedis(host=config_class.REDIS_HOST, port=config_class.REDIS_PORT, decode_responses=True)

    app.url_map.converters["re"] = ReConverter
    from ihome import api_1_0
    app.register_blueprint(api_1_0.api, url_prefix="/api/v1.0")
    from ihome import web_html
    app.register_blueprint(web_html.html)
    return app
