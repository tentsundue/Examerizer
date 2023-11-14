
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "<h1>This is where the GPT API stuff will happen...hopefully/h1>"

if __name__ == '__main__':
    app.run(debug=True)
