# http://localhost:5000/profile?name=hong&age=32 (static Route)
# http://localhost:5000/profile/hong/32 (dynamic Route)
from flask import Flask, url_for, render_template
# 라우팅 : URL을 특정함수(뷰함수)에 연결하는 작업
@app.route("/") # static Route
def hello():
    return render_template("06_index.html")
@app.route("/profile/<name>/<age>") # dynamic Route
def get_profile(name, age):
    return "<h1>profile : {}님 {}살입니다</h1>".format(name, age)
if __name__=="__main__":
    with app.test_request_context():
        print(hello())
        print(url_for('hello'))
    app.run(debug=True, port=80)