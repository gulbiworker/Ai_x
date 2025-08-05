# python -m pip install --upgrade pip
# pip install flask
from flask import Flask
app = Flask(__name__)   # 앱 인스턴스 생성
@app.route("/") # @ : 데코레이터를 통해 요청 가능한 url 등록
def handler_viewFunc():
    return "<h1>hello, world</h1>"

if __name__=="__main__":
    app.run(port=80, debug=True)

# 파일명이