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
    f = open("updated.txt", "r")
    Update = f.read()
    f = open("./templates/description.txt", "r")
    descriptionText = f.read()
    return render_template('index.html', content=Update, description=descriptionText)


if __name__ == '__main__':
    api.run( HOST,PORT, threaded=True, debug=False)

