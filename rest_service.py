from flask import Flask, jsonify, request
from scrapper import *

yo = Yo()

app = Flask(__name__)

@app.route("/transform", methods=['POST'])
def transform():
    words = []
    js = request.get_json()
    for i in js["words"]:
        if 'ё' in i:
            if (yo.getValid(i)):
                words.append(i)
            continue
        ind = 0
        for letter in i:
            if letter == "е":
                newStr = list(i)
                newStr[ind] = "ё"
                newStr = "".join(newStr)
                if (yo.getValid(newStr)):
                    words.append(newStr)
            ind += 1

    return jsonify(words = words)


@app.route("/get_all")
def getAll():
    return jsonify(yo.getWords())

@app.route("/is_valid_yo", methods=['POST', 'GET'])
def checkValid():
    searchword = request.args.get('word', '')
    if request.method == 'GET':
        return "true" if yo.getValid(searchword) else "false"
    else:
        return searchword

if __name__ == "__main__":
    app.run()