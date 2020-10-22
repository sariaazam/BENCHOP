from flask import Flask, request
from subprocess import Popen, PIPE
import subprocess

app = Flask(__name__)

originalParameters = ["octave", "Table.m"]

#Run all problems with default parameters
@app.route('/runall', methods=['GET'])
def run_all():
	p = Popen(["octave", "Table.m", "all"], stdin=PIPE, stdout=PIPE, stderr=PIPE)
	output, err = p.communicate(b"input data that is passed to subprocess' stdin")
	rc = p.returncode
	return output

#Run specified problem with specified parameters
#Example call: 
#curl -i "http://1.2.3.4:1234/p1a?K=1&F=5"

@app.route('/<problem>', methods=['GET'])
def input(problem):
	parameterList = originalParameters[:]
	
	parameterList.append(problem)
	
	#iterate through the dict from request to get parameters
	for k,v in request.args.iteritems():
		parameter = k + "=" + v
		parameterList.append(parameter)
	
	print(parameterList)

	#call octave with parameters
	#snippet found at: https://stackoverflow.com/questions/1996518/retrieving-the-output-of-subprocess-call
	p = Popen(parameterList, stdin=PIPE, stdout=PIPE, stderr=PIPE)
	output, err = p.communicate(b"input data that is passed to subprocess' stdin")
	rc = p.returncode
	return output

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
