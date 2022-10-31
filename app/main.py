import json
from flask import Flask
from flask_cors import CORS

def create_app(test_config=None):
     app = Flask(__name__)
     # Set up CORS. Allow '*' for origins.
     CORS(app, resources={r"/api/*": {"origins": "*"}})
 
#Access-Control-Allow
# CORS Headers
     @app.after_request
     def after_request(response):
          response.headers.add(
               "Access-Control-Allow-Headers", "Content-Type,Authorization,true"
          )
          response.headers.add(
               "Access-Control-Allow-Methods", "GET"
          )
          return response


     @app.route('/', methods = ["GET"])
     def index():
               output = {
                    "slackUsername": "aaronben41", 
                    "backend": True, 
                    "age": 25, 
                    "bio": "I'm a self-motivated software developer with a flare for backend development" 
               }
               return json.dumps(output)
     return app