import json
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/', methods = ["GET"])
def index():
     output = {
          "slackUsername": "aaronben41", 
          "backend": True, 
          "age": 25, 
          "bio": "I'm a self-motivated software developer with a flare for backend development. I love taking on new challenges" 
     }
     return json.dumps(output), 200, {'content-type':'application/json'}