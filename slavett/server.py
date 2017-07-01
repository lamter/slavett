# encoding:utf-8

from flask import Flask
from .data import Data

app = Flask(__name__)

data = Data()

@app.route('/futures_holiday')
def futures_holiday():
    return data.futures_holiday
