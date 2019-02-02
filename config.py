import redis


class Config(object):
    """ 配置信息 """

    SECRET_KEY = "123"

    # 数据库
    SQLALCHEMY_DATABASE_URI = "mysql://root:tmantest@127.0.0.1:3306/ihome"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379
    SESSION_TYPE = 'redis'
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    SESSION_USE_SINGER = True
    PERMANENT_SESSION_LIFETIME = 86400


class DevelopmentConfig(Config):
    """ 开发模式"""
    DEBUG = True


class ProductionConfig(Config):
    """生产环境"""
    pass


config_map = {
    "develop": DevelopmentConfig,
    "product": ProductionConfig,
}
