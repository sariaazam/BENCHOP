#!flask/bin/python
from flask import Flask, jsonify
from tasks import frequencies

app = Flask(__name__)

@app.route('/Table/<float:price>/<float:strike>/<float:time>/<float:rate>/<float:volatility>', methods=['GET'])
def benchop(price, strike, time, rate, volatility):
        return 'results'


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)

