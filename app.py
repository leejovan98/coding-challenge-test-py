from flask import Flask
from flask import request, jsonify
from clumsy_louis import solution


app = Flask(__name__)


@app.route("/")
def hello_world():  # put application's code here
    return "Hello World!"


@app.route("/the-clumsy-programmer", methods=["POST"])
def solveClumsy():
    data = request.json
    data = data[0]
    inputDict = data["dictionary"]
    mistypes = data["mistypes"]
    result = solution(inputDict, mistypes)
    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
