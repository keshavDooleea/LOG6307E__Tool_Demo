import os
from flask import Flask

app = Flask(__name__)


@app.route('/')
def base_route():
    return '<h1>Hello LOG6370E, I am instance {}! This is my first url!</h1>'.format(os.environ['INSTANCE_ID_EC2'])

@app.route('/second_url')
def hello_route():
    return '<h1>Here is my second url!</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

