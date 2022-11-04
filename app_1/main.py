import json
from flask import Flask, jsonify, request


#from flask_cors import CORS

app = Flask(__name__)
'''
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
'''

#Stage 1 task

@app.route('/', methods = ["GET"])
def index():
     output = {
          "slackUsername": "aaronben41", 
          "backend": True, 
          "age": 25, 
          "bio": "I'm a self-motivated software developer with a flare for backend development. I love taking on new challenges" 
     }
     return json.dumps(output), 200, {'content-type':'application/json'}
