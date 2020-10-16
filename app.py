#!flask/bin/python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/Table/', methods=['GET'])
def benchop(price, strike, time, rate, volatility):
        return 'results'


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)

