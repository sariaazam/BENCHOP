#!flask/bin/python
from flask import Flask, jsonify
from tasks import benchop

app = Flask(__name__)

@app.route('/table', methods=['GET'])
def process():
    results = benchop.delay()
    return 'ok'


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)

