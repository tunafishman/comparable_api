#!../flask/bin/python
from comparable import Comparable
from flask import Flask, jsonify

app = Flask(__name__)
comparables = [Comparable()]

@app.route('/comparables/cid/<int:cid>', methods=['GET'])
def get_comparables_by_cid(cid):
    scrubber = lambda x: x.Cid() == cid
    returns = [comp.Json() for comp in filter(scrubber, comparables)]
    return jsonify({'comparables': returns})

def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)
