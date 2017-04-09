#!/usr/bin/env python
import mlBashHistory

from flask import Flask,jsonify,request
app = Flask(__name__)
from flask import abort


@app.route('/add', methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        return jsonify( request.form ) 

@app.route('/postdebug', methods=['POST', 'GET'])
def postdebug():
    print "Here"
    print request.headers
    if request.method == 'POST':
	return jsonify( { 
          "form": request.form,
          "args": request.args,
          "values": request.values,
          "data": request.data,
          "is_json": request.is_json,
#          "get_json": request.get_json,
#          "headers": request.headers
        }) 

@app.route('/predict/<string:word>', methods=['GET'])
def predict( word ):
  return jsonify({'word':word})


@app.route('/hello')
def index():
    return "Hello, World!"


if __name__ == '__main__':
    app.run(debug=True)

