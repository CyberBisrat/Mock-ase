from flask import Flask, render_template, request, make_response, jsonify
import requests
import time
import sys

app = Flask(__name__, instance_relative_config=True)

@app.route('/mulstring')
def mulstring():
    a = request.args.get('a', type=str)
    n = request.args.get('n', type=int)
    if a is not None and n is not None:
        if n<0:
            return make_response('Invalid input [n<0]\n', 400)
        return make_response(jsonify(s=a*n), 200)
    else:
        return make_response('Invalid input [a or n]\n', 400)

def create_app():
    return app

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
