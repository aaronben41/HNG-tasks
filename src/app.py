from flask import Flask, jsonify, request
from flask_cors import CORS
import json, operator

from settings import SLACK_UNAME

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



ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.div
}

ops_words = {
    "+": 'addition',
    "-": 'subtraction',
    "*": 'multiplication',
    "/": 'division'
}

#Stage 2 task

@app.route('/', methods = ["POST"])
def index():
     body = request.get_json()
     if body != None:
          operation_type = body.get('operation_type', '')
          x = body.get('x')
          y = body.get('y')
     
     elif body == None or body == '':
          operation_type = '+'
          x = 5
          y = 20

     if operation_type == '+' or '-' or '*' or '/':
          operation = ops['operation_type']
          result = operation(x,y)
          
          output =  {
               "slackUsername": SLACK_UNAME, 
               "operation_type" : ops_words['operation_type'],
               "result": result 
          }

          return json.dumps(output), 200, {'content-type':'application/json'}
     
     elif operation_type != '+' or '-' or '*' or '/':
          output =  {
               "slackUsername": SLACK_UNAME, 
               "operation_type" : operation_type,
               "result": "Please enter operation type with standard notation - eg. '+', '-' - and try again " 
          }
          return json.dumps(output), 200, {'content-type':'application/json'}
     

