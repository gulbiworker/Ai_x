# python -m venv .venv
# ctrl+shift+p -> select interpretre -> 가상환경 만들기 -> .venv로 가상 환경 만들기
# -> 인터프리터경로입력 -> 찾기(python.exe) (가상환경 생성하기 2)
# .venv\Script\activate (가상환경들어가기)
# python -m pip install --upgrade pip
# pip install flask
from flask import Flask
from flask import render_template
from flask import request
from flask import abort # 강제로 예외발생
class Member:
    def __init__(self, name, id, pw, addr):
        self.name = name
        self.id = id
        self.pw = pw
        self.addr = addr
        from models import  Member

        app = Flask(__name__)
        @app.route("/user/<name>")
        def viewFunction_handlerFunction(name):
            return f"<h1>{name}님 환영합니다</h>"
        
        @app.route("/user")
        def user(): 
            name = request.args.get('name', "들어온이름 없음")
            if name:
                return f"<h1>전달받은 파라미터 이름 : {name}님</h1>"
            esle:
                abort(404)
        @    
    if __name__ == 'main':
        app.run(debug=True, port=80)