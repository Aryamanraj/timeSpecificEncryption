import pickle
from timeFromFirstDay import timeFromFirstDay
from findCommonSubstring import find_common_substring
from binaryTree import BinaryTree, Node
from loadTree import load_tree

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return 'Hello World'

@app.route('/find_hash', methods=['GET'])
def find_hash():
      #inputer = request.args["time"]
      inputer = timeFromFirstDay()
      tree = load_tree("test2.bin")
      print(tree.search(inputer))
      return jsonify(tree.search(inputer))

@app.route('/input_hash', methods=['GET'])
def inputHash():
    #taking inputs
    _inputer_from = request.args["From"]
    _inputer_to = request.args["To"]

    #finding common substring
    inputer = find_common_substring(_inputer_from, _inputer_to)

    tree = load_tree("test2.bin")
    print(tree.search(inputer))
    return jsonify(tree.search(inputer))

@app.route('/get_hash', methods=["GET"])
def getHash():
    _inputer_from = request.args["Bin"]
    inputer = _inputer_from
    tree = load_tree("test2.bin")
    print(tree.search(inputer))
    return jsonify(tree.search(inputer))


app.run(host = '0.0.0.0',port = 5223)