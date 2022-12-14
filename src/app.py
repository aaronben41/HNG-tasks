from flask import Flask, jsonify, request
from flask_cors import CORS
import json, operator


app = Flask(__name__)

CORS(app, resources={r"/api/*": {"origins": "*"}})
   #Access-Control-Allow
    # CORS Headers
@app.after_request
def after_request(response):
     response.headers.add(
          "Access-Control-Allow-Headers", "Content-Type,Authorization,true"
     )
     response.headers.add(
          "Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS"
     )
     return response





#Stage 2 task

@app.route('/', methods = ["POST"])
def index():
     
     # default values
     operation_type = '-'
     x = 5
     y = 20

     def calculate ():
          ops = {
               "addition": operator.add,
               "subtraction": operator.sub,
               "multiplication": operator.mul,
               "division": operator.truediv
               }


               
          if operation_type in ops:
               operation = ops[operation_type]
               output = int(operation(x,y))
               operation_output = operation_type
          else:
               operation_output = "Error encountered"
               output = "please enter operator as a symbol, eg. '+' or '-' "
          
          result =  {
               "slackUsername": "aaronben41", 
               "operation_type" : operation_output,
               "result": output 
               }
          return result

     body = request.get_json()

     if body != None:
          operation_type = body['operation_type']
          x = int(body['x'])
          y = int(body['y'])
          
          final_result = calculate()
          
     else:
          final_result = calculate()

     return json.dumps(final_result), 200, {'content-type':'application/json'}
     

