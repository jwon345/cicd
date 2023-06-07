from flask import Flask, render_template 
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
    return render_template('index.html')


if __name__ == '__main__':
    api.run( HOST,PORT, threaded=True, debug=False)

