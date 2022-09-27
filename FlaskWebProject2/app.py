"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import request
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/api/GET')
def Get_Users():
    f = open('file.txt','r')
    users = f.read();
    f.close();
    return users;

@app.route('/api', methods = ['POST', 'PUT'])
def Post_User():
    if request.method == 'POST':
        f = open('file.txt','a')
        login = request.form['login']
        password = request.form['password']
        username= request.form['username']
        number= request.form['number']
        f.write(login + " " + password + " " + username + " "+number + "\n")
        f.close()
    if request.method == 'GET':
        f = open('file.txt','r')
        users = f.read();
        f.close();
        return users;
    if request.method == 'PUT':
        f = open('file.txt','r')
        login = request.form['login']
        password = request.form['password']
        username= request.form['username']
        number= request.form['number']


        newlogin = request.form['newlogin']
        newpassword = request.form['newpassword']
        newusername= request.form['newusername']
        newnumber= request.form['newnumber']
        s = (login + " " + password + " " + username + " "+number)
        data = f.read()
        data = data.replace(s, newlogin + " " + newpassword + " " + newusername + " "+newnumber)
        f.close()
        f = open('file.txt','wt')
        f.write(data)
        f.close
    
        

@app.route('/api/<int:idd>', methods = ['DELETE'])
def Put_User(idd):
    if request.method == 'DELETE':
        f = open('file.txt', 'w')
        f.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='3005')