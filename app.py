import os
from flask import Flask, render_template, redirect, url_for, request
import main
import socket
from requests import get


app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/', methods=['GET','POST'])
def wow():
    hostname = socket.gethostname()
    user_ip = socket.gethostbyname(hostname)
    return render_template('index.html', ip=user_ip)

@app.route('/portfolio')
def readme():
    return redirect("https://www.yoomin.xyz")

@app.route('/inside',methods=['GET','POST'] )
def ing(methods=['GET','POST']):
    # 여기서 id를 이용하여 Python 변수를 가져온다.
    value = main.bookname

    # HTML 템플릿에 변수 값을 전달하여 출력한다.
    return render_template('readme.html', value=value)

@app.route('/search',methods=['GET','POST'] )
def soundgood(methods=['GET','POST']):
    # 여기서 id를 이용하여 Python 변수를 가져온다.
    value = main.bookname

    # HTML 템플릿에 변수 값을 전달하여 출력한다.
    return render_template('readme.html', value=value)




if __name__ == '__main__':
    port = int(os.environ.get('PORT', 1234))
    app.run(host='0.0.0.0', port=port, debug=True)
