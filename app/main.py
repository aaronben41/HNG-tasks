import json
from flask import Flask


app = Flask(__name__)

@app.route('/', methods = ["GET"])
def index():
    output = {
         "slackUsername": "aaronben41", 
         "backend": True, 
         "age": 25, 
         "bio": "I'm a self-motivated software developer with a flare for backend development" 
    }
    return json.dumps(output)
