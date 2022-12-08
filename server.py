from flask import Flask,render_template,redirect,url_for,request
from form_classes import *
import sqlite3 as sqlite

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

@app.route("/goal-type/delete/<string:id>")
def delete(id):
   
   return redirect(url_for("goal-type"))
@app.route("/goals/delete/<string:id>")
def delete(id):
   
   return redirect(url_for("goals"))
@app.route("goal-type/edit/<string:id>",methods = ["GET","POST"])
def update(id):

   if request.method == "GET":      
      updateForm = GoalTypeForm()

    #  with sqlite.connect("tasks.sqlite") as con:
    #    con.row_factory = sqlite.Row
    #     cur=con.cursor()
    #     query = """ SELECT teamname,goals,leftfoot,rightfoot,header,owngoals,penalties from goaltype WHERE (ID = {})""".format(id)
    #     cur.execute(query)
    #     row = cur.fetchone()

    #  updateForm.team_name.data = row["Team Name"]
    #  updateForm.goals.data = row["Goals"]
    #  updateForm.left_foot.data = row["Left foot"]
    #  updateForm.right_foot.data = row["Right foot"]
    #  updateForm.header.data = row["Header"]
    #  updateForm.own_goals.data = row["Own Goals"]
    #  updateForm.penalties.data = row["Penalties"]

      return render_template("goal-type/goal-type-update.html", form=updateForm)

   if request.method == "POST":
      updateForm = GoalTypeForm(request.form)
      #newTeamname = updateForm.team_name.data
      #newGoals = updateForm.goals.data
      #newLeftFoot = updateForm.left_foot.data
      #newRightFoot = updateForm.right_foot.data
      #newHeader = updateForm.header.data
      #newOwnGoals = updateForm.own_goals.data
      #newPenalties = updateForm.penalties.data

      #with sqlite.connect("tasks.sqlite") as con:
      #   con.row_factory = sqlite.Row
      #   cur=con.cursor()
      #   query = """ UPDATE goaltype SET teamname = "{}", goals = {}, leftfoot = {}, rightfoot = {}, header = {}, owngoals = {}, penalties = {} WHERE (ID = {})""".format(newTeamName,newGoals,newLeftFoot,newRightFoot,newHeader,newOwnGoals,newPenalties,id)
      #   cur.execute(query)
      #   con.commit()
      return redirect(url_for("goal-type"))
@app.route("goals/edit/<string:id>",methods = ["GET","POST"])
def update(id):

   if request.method == "GET":      
      updateForm = GoalsForm()

    #  with sqlite.connect("tasks.sqlite") as con:
    #    con.row_factory = sqlite.Row
    #     cur=con.cursor()
    #     query = """ SELECT teamname,matches,totalgoals,averagegoals,goalsconceded,averageconceded,goaldifference from goals WHERE (ID = {})""".format(id)
    #     cur.execute(query)
    #     row = cur.fetchone()

    #  updateForm.team_name.data = row["Team Name"]
    #  updateForm.matches.data = row["Matches"]
    #  updateForm.total_goals.data = row["Total Goals"]
    #  updateForm.average_goals.data = row["Average Goals"]
    #  updateForm.goals_conceded.data = row["Goals Conceded"]
    #  updateForm.average_conceded.data = row["Average Conceded"]
    #  updateForm.goal_ifference.data = row["Goal Difference"]

      return render_template("goals/goals-update.html", form=updateForm)

   if request.method == "POST":
      updateForm = GoalsForm(request.form)
      #newTeamname = updateForm.team_name.data
      #newMatches = updateForm.matches.data
      #newTotalGoals = updateForm.total_goals.data
      #newAverageGoals = updateForm.average_goals.data
      #newGoalsConceded = updateForm.goals_conceded.data
      #newAverageConceded = updateForm.average_conceded.data
      #newGoalDifference = updateForm.goal_ifference.data

      #with sqlite.connect("tasks.sqlite") as con:
      #   con.row_factory = sqlite.Row
      #   cur=con.cursor()
      #   query = """ UPDATE Tasks SET teamname = {},matches = {},totalgoals = {},averagegoals = {},goalsconceded = {},averageconceded = {},goaldifference = {} WHERE (ID = {})""".format(newTeamname,newMatches,newTotalGoals,newAverageGoals,newGoalsConceded,newAverageConceded,newGoalDifference,id)
      #   cur.execute(query)
      #   con.commit() 
      return redirect(url_for("goals"))
      


@app.route("/defence")
def defence():
   return render_template("defence/defence.html")



@app.route("/defence/add_defence", methods=["GET","POST"])
def add_defence():
    form = DefenceForm(request.form)

    if request.method == "POST" and form.validate(): 
        pass
    
    else:
        return render_template("defence/add_defence.html", form=form)




@app.route("/discipline")
def discipline():
   return render_template("discipline/discipline.html")



@app.route("/discipline/discipline", methods=["GET","POST"])
def add_discipline():
    form = DisciplineForm(request.form)

    if request.method == "POST" and form.validate(): 
        pass
    
    else:
        return render_template("discipline/add_discipline.html", form=form)





if __name__ == "__main__":
    app.run(debug=True)