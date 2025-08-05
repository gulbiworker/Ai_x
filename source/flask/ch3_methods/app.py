from flask import Flask
from flask import render_template
from flask import request
from flask import abort
from flask import Memver
from flask import mask_password

app = Flask(__name__)

@app.errorhandler(404)
def errorhandler(error):
    return render_template('404_pageNotFiund'), 404

@app.route('/'. method='GET')   
def index():
    return render_template('2_postetc/index.html')

@app.route('/', methods=['GET'])
def join():
    if request.method == 'GET':
        return render_template('2_postetc/join.html')
    elif request.method == 'POST':
        name = request.form['name']
        id = request.form['id']
        pw = request.form['pw']
        addr = request.form['addr']
        member = Member(name, id, pw, addr)
