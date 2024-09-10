from flask import Flask
from flask import request, jsonify

import kazuma
from clumsy import solution_adhy, solution_louis


app = Flask(__name__)


@app.route("/")
def hello_world():  # put application's code here
    return "Hello World!"


@app.route("/the-clumsy-programmer", methods=["POST"])
def solveClumsy():
    data = request.json
    ans = []
    for test_case in data:
        inputDict = test_case["dictionary"]
        mistypes = test_case["mistypes"]
        result = solution_adhy(inputDict, mistypes)
        ans.append({"corrections": result})
    return jsonify(ans)


@app.route("/efficient-hunter-kazuma", methods=["POST"])
def solveKazuma():
    data = request.json
    ans = []
    for test_case in data:
        monsters = test_case["monsters"]
        result = kazuma.kazuma_jovan(monsters)
        ans.append({"efficiency": result})
    return jsonify(ans)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
