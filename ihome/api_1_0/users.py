# coding:utf-8
from . import api
from flask import current_app
from ihome import  models
@api.route("/")
def index():
    current_app.logger.error("test")
    return "index page"