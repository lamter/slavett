# coding:utf-8

from app import app

# 使用Gunicorn需要这两行代码对接
from werkzeug.contrib.fixers import ProxyFix
app.wsgi_app = ProxyFix(app.wsgi_app)