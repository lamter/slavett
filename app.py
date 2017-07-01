# encoding:utf-8

from flask import Flask

app = Flask(__name__)

# data = Data()

# @app.route('/futures_holiday')
# def futures_holiday():
#     return data.futures_holiday

@app.route('/')
def futures_holiday():
    return 'Hello World'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=30030)