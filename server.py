from flask import Flask,render_template,redirect,url_for,request
from form_classes import *

app = Flask(__name__)

@app.route("/")
def index():
   return render_template("index.html")

@app.route("/teams")
def teams():
   return render_template("teams/teams.html") 

@app.route("/teams/add_team", methods=["GET","POST"])
def add_team():
    form = TeamsForm(request.form)

    if request.method == "POST" and form.validate(): 
        pass
    
    else:
        return render_template("teams/add_team.html", form=form) 









@app.route("/attempts")
def attempts():
   return render_template("attempts/attempts.html")

@app.route("/attempts/add_attempts", methods=["GET","POST"])
def add_attempts():
    form = AttemptsForm(request.form)

    if request.method == "POST" and form.validate(): 
        pass
    
    else:
        return render_template("attempts/add_attempts.html", form=form) 











@app.route("/attack")
def attack():

    return render_template("attack/attack.html")

@app.route("/attack/add_attack", methods=["GET","POST"])
def add_attack():
    form = AttackForm(request.form)

    if request.method == "POST" and form.validate(): 
        pass
    
    else:
        return render_template("attack/add_attack.html", form=form)





@app.route("/goals")
def goals():
   return render_template("goals/goals.html")

@app.route("/goal-type")
def goal_type():
   return render_template("goal-type/goal-type.html")

@app.route("/goals/goals-add", methods=["GET","POST"])
def goals_add():
    form = GoalsForm(request.form)

    if request.method == "POST" and form.validate(): 
        pass
    
    else:
        return render_template("goals/goals-add.html", form=form)

@app.route("/goal-type/goal-type-add", methods=["GET","POST"])
def goal_type_add():
    form = GoalTypeForm(request.form)

    if request.method == "POST" and form.validate(): 
        pass
    
    else:
        return render_template("goal-type/goal-type-add.html", form=form) 


if __name__ == "__main__":
    app.run(debug=True)