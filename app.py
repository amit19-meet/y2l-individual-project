from flask import Flask
from flask import session as login_session
from flask import render_template, request, redirect, url_for
from database import *


app = Flask(__name__)

app.secret_key= "simba"


current_username = ''
@app.route('/ballet', methods=['GET', 'POST'])
def ballet_page():
    if request.method == 'GET':
        i = get_all_comments("ballet")     
        return render_template('ballet.html',  comments = i)
    else:
        name = request.form['firstname']

        comment= request.form['comment']
        type_dance = "ballet"
        


        add_comment(name, comment,type_dance)
        
        i = get_all_comments("ballet")        
        return render_template('ballet.html', comments = i)

@app.route('/hiphop', methods=['GET', 'POST'])
def hiphop_page():
    if request.method == 'GET':
        i = get_all_comments("hiphop")     
        return render_template('hip_hop.html',  comments = i)
    else:
        name = request.form['firstname']
        
        comment= request.form['comment']
        type_dance = "hiphop"
        


        add_comment(name, comment,type_dance)
        
        i = get_all_comments("hiphop")        
        return render_template('hip_hop.html', comments = i)
@app.route('/', methods= ['GET', 'POST'])
def signup_page():
    if request.method == 'GET':
        return render_template('sign_up.html')
    else:
        username = request.form['username']
        login_session["username"]= username
        password = request.form['password']

        add_user(username, password)
        return redirect("/home")

@app.route('/login', methods= ["GET", "POST"])
def login_page():
    if request.method == "GET":
        return render_template("log_in.html")

    else:
        username = request.form['username']
        login_session["username"]= username
        password = request.form['password']

        try:
            user = get_user_by_username(username)
        except:
            return render_template("log_in.html")
        
        if user.password == password:

            return redirect("/home")

        else:

            return render_template("log_in.html")



@app.route('/home', methods=['GET', 'POST'])
def home_page():
     if request.method == 'GET':
        print(login_session)
        return render_template('home.html')
     


















if __name__ == '__main__':
    app.run(debug = True)
