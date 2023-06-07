from flask import Flask
import os

HOST = "0.0.0.0"
PORT = 5002

api = Flask(__name__)

# Copy of http://stackoverflow.com/a/20104705

api.debug = True


@api.route('/push', methods=['POST'])
def update():
    os._exit(1)

@api.route('/', methods=['GET'])
def mainPage():
    return "<h1>welcome :)</h1>"


if __name__ == '__main__':
    api.run( HOST,PORT, threaded=True, debug=False)

