from flask import Flask
APP = Flask(__name__)

# just a test comment
@APP.route('/')
def hello_world():
    return 'Hello, World from Flask!\n'


if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)
