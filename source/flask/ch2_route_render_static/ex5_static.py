from flask import Flask
qpp = Flask(__name__)

@app.route('/hello')
def hello():
    return "hello"
@app.route('/profile/<name>/<age')
def get_profile(name, age):
    return name, age
if __name__ == '__main__':
    with app.test_request_context():
        print(url_for