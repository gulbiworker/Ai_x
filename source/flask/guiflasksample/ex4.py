from flask import Flask
from predict import loaded_model, predict_apt_price
application = Flask(__name__)   # 어플리케이션 객체 생성

@application.route("/")
def handller_function():
    return '<h1>Hello World!</h1>'

@application.route("/apt/<year>/<square>/<floor>")
def aptPredictHandler(year, square, floor):
    answer = predict_apt_price(year, square, floor)
    return answer

if __name__ == '__main__':
    #코드가 변경될떄마다 서버 자동 재시작
    application.run(debug=True)