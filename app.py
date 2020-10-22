#!flask/bin/python
from flask import Flask, jsonify
from oct2py import Oct2Py
import pprint


app = Flask(__name__)

@app.route('/table', methods=['GET'])
def benchop():
    oc = Oct2Py()
    oc.addpath('/home/ubuntu/BENCHOP')
    oc.run('Table.m')

    return 'ok'


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)

