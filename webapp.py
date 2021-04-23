import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)

# In order to use "sessions",you need a "secret key".
# This is something random you generate.  
# For more info see: https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY

app.secret_key=os.environ["SECRET_KEY"]; #This is an environment variable.  
                                     #The value should be set in Heroku (Settings->Config Vars).  
                                     #To run locally, set in env.sh and include that file in gitignore so the secret key is not made public.

@app.route('/')
def renderMain():
    return render_template('home.html')

@app.route('/retakeQuiz')
def retakeQuiz():
    session.clear() #clears variable values and creates a new session
    return redirect(url_for('renderMain')) # url_for('renderMain') could be replaced with '/'

@app.route('/question1')
def renderQuetion1():
    return render_template('question1.html')

@app.route('/question2',methods=['GET','POST'])
def renderQuestion2():
    session["answer1"]=request.form['a1']
    return render_template('question2.html')

@app.route('/question3',methods=['GET','POST'])
def renderQuestion3():
    session["answer2"]=request.form['a2']
    return render_template('question3.html', s1=get_s1(), s2=get_s2())
  
def get_s1():
  if session["answer1"] == "32":
    s1 = "1 out of 1"
  else:
    s1 = "0 out of 1"
  
def get_s2():
  if session["answer2"] == "0":
    s1 = "1 out of 1"
  else:
    s1 = "0 out of 1"

if __name__=="__main__":
    app.run(debug=False)
