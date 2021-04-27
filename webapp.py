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
count = 0
p_best = 0

@app.route('/')
def renderMain():
    return render_template('home.html')

@app.route('/retakeQuiz')
def retakeQuiz():
    session.clear() #clears variable values and creates a new session
    global count
    count = 0
    return redirect(url_for('renderMain')) # url_for('renderMain') could be replaced with '/'

@app.route('/question1')
def renderQuetion1():
    return render_template('question1.html')

@app.route('/question2',methods=['GET','POST'])
def renderQuestion2():
  if "answer1" not in session:
    session["answer1"]=request.form['a1']  
  return render_template('question2.html')

@app.route('/question3',methods=['GET','POST'])
def renderQuestion3():
  if "answer2" not in session:
    session["answer2"]=request.form['a2']
  return render_template('question3.html')

@app.route('/answers',methods=['GET','POST'])
def renderAnswers():
  if "answer3" not in session:
    session["answer3"]=request.form['a3']
  return render_template('answers.html', s1=get_s1(), s2=get_s2(), tsc=get_total(), bst=get_best())
  
def get_s1():
  score = ""
  global count
  if count != 0:
    count = 0
  if session["answer1"] == "32":
    score = "1 out of 1"
    count = count + 1
  else:
    score = "0 out of 1"
  return score
  
def get_s2():
  score2 = ""
  print(session)
  if session["answer2"] == "0":
    score2 = "1 out of 1"
    global count
    count = count + 1
  else:
    score2 = "0 out of 1"
  return score2

def get_total():
  global count
  tot_score = str(count) + " out of 2"
  return tot_score

def get_best():
  global count
  global p_best
  if count > p_best:
    p_best = count
  return p_best

if __name__=="__main__":
    app.run(debug=False)
