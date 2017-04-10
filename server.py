#!/usr/bin/env python
import mlBashHistory

from flask import Flask,jsonify,request
app = Flask(__name__)
from flask import abort

BH=mlBashHistory.ModelPredict()

@app.route('/add', methods=['POST'])
def add():
  if request.method == 'POST':
     f=request.form
     if "data" in f:
       BH.addNgramsFromString( f["data"] )
       return jsonify({"status":"success"})
     else: pass
       #TODO throw bad argument error  
  return jsonify({"status":"failure"})

@app.route('/status', methods=['GET'])
def status():
  return jsonify({ "count": BH.status() })

@app.route('/update', methods=['GET'])
def update():
  return jsonify({ "status": BH.update() })

@app.route('/predict', methods=['GET'])
def predict():
   word=request.args["q"]
   return jsonify( { "response": BH.predict( word ) } ) 

@app.route('/postdebug', methods=['POST', 'GET'])
def postdebug():
   print request.headers
   if request.method == 'POST':
      return jsonify( { 
         "form": request.form,
         "args": request.args,
         "values": request.values,
         "data": request.data,
         "is_json": request.is_json,
#         "get_json": request.get_json,
#         "headers": request.headers
       }) 

@app.route('/getdebug', methods=['GET'])
def getdebug():
    print request.headers
    return jsonify( { 
          "form": request.form,
          "args": request.args,
          "values": request.values,
          "data": request.data,
          "is_json": request.is_json,
#          "get_json": request.get_json,
#          "headers": request.headers
       })  


#@app.route('/predict/<string:word>', methods=['GET'])
#def predict( word ):
#  return jsonify({'word':word})


@app.route('/hello')
def index():
    return "Hello, World!"


if __name__ == '__main__':
    app.run(debug=True)

