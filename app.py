from flask import Flask,request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "home"

@app.route('/<input>')
def inputHandle(input):
    return input

@app.route("/",methods=["POST"])
def post():
    value = request.get_data()
    return value 

if __name__ == "__main__":
    app.run(debug=True)