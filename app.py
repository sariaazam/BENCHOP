#!flask/bin/python
from flask import Flask, jsonify
from tasks import benchop

app = Flask(__name__)

@app.route('/table/<prob>', methods=['GET'])
def process(prob):
    results = benchop.delay(prob)
    return 'queueing' prob


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)

