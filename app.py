from flask import Flask
from flask import request, jsonify
import json


app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/louis_clumsy', methods=['POST'])
def solveClumsy():
    data = request.json
    parsedJson = json.loads(data)
    inputDict = parsedJson["dictionary"]
    mistypes = parsedJson["mistypes"]
    result = solveClumsy(inputDict, mistypes)
    return jsonify(result)

if __name__ == '__main__':
    app.run()
