import os
from flask import Flask

app = Flask(__name__)


@app.route('/')
def base_route():
    return '<h1>Hey I am {}!</h1>'.format(os.environ['INSTANCE_ID_EC2'])

@app.route('/hello')
def hello_route():
    return '<h1>Hello World</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

