from flask import Flask,render_template,redirect,url_for,request
from form_classes import *
import sqlite3 as sql

app = Flask(__name__)

@app.route("/")
def index():
    db = sql.connect("database.db")
    c = db.cursor()
    c.execute("BEGIN")
    c.execute("PRAGMA foreign_keys = ON")
    db.commit()
    db.close()

    return render_template("index.html")

@app.route("/teams")
def teams():
    with sql.connect("database.db") as con:
        con.row_factory = sql.Row
        cursor=con.cursor()

        query=""" SELECT * FROM TEAMS """

        cursor.execute(query)

        teams = cursor.fetchall()

    return render_template("teams/teams.html",teams=teams) 


@app.route("/teams/add_team", methods=["GET","POST"])
def add_team():
    form = TeamsForm(request.form)

    if request.method == "POST" and form.validate(): 
        team_name = form.team_name.data
        print(team_name)

        with sql.connect("database.db") as con:
            
            cursor=con.cursor()
            query = "INSERT INTO TEAMS (teamName) VALUES (?)"
            
            cursor.execute(query,(team_name,))
            con.commit()  

            cursor.close()  

        return redirect(url_for("teams"))
    
    else:

        return render_template("teams/add_team.html", form=form) 


@app.route("/delete_team/<string:id>")
def delete_team(id):

    with sql.connect("database.db") as con:
       cursor=con.cursor()

       query = "DELETE FROM TEAMS WHERE teamId = ?" 

       cursor.execute(query,(id,))

       con.commit() 

    return redirect(url_for("teams"))

@app.route("/edit_team/<string:id>", methods=["GET","POST"])
def edit_team(id):

    if request.method == "GET":
        form = TeamsForm()

        with sql.connect("database.db") as con:
            con.row_factory = sql.Row
            cur=con.cursor()

            query = "SELECT teamName FROM TEAMS WHERE (teamId = ?)"
            cur.execute(query,(id,))
            team = cur.fetchone()#matching element

            form.team_name.data = team["teamName"]

        return render_template("teams/edit_team.html", form=form)

    if request.method == "POST":
        form = TeamsForm(request.form)
        new_name = form.team_name.data

        with sql.connect("database.db") as con:
            con.row_factory = sql.Row
            cur=con.cursor()
            query = "UPDATE TEAMS SET teamName = ? WHERE teamId = ?"
            cur.execute(query,(new_name, id))
            con.commit()
        
        return redirect(url_for("teams"))


@app.route("/attempts")
def attempts():
    with sql.connect("database.db") as con:
        con.row_factory = sql.Row
        cursor=con.cursor()

        query=""" SELECT * FROM ATTEMPTS """

        cursor.execute(query)

        teams = cursor.fetchall()

    return render_template("attempts/attempts.html",teams=teams)

@app.route("/attempts/add_attempts", methods=["GET","POST"])
def add_attempts():
    form = AttemptsForm(request.form)

    if request.method == "POST" and form.validate(): 
        team_name = form.team_name.data
        matches = form.matches.data
        attempts = form.attempts.data
        attempts_on_target = form.attempts_on_target.data
        attempts_off_target = form.attempts_off_target.data
        attempts_blocked = form.attempts_blocked.data

        with sql.connect("database.db") as con:
            
            cursor=con.cursor()
            query = "INSERT INTO ATTEMPTS (team,matches,attempts,attemptsOnTarget,attemptsOffTarget,attemptsBlocked) VALUES (?,?,?,?,?,?)"
            
            cursor.execute(query,(team_name,matches,attempts,attempts_on_target,attempts_off_target,attempts_blocked))
            con.commit()  

            cursor.close()  

        return redirect(url_for("attempts"))
    
    else:
        return render_template("attempts/add_attempts.html", form=form) 

@app.route("/delete_attempts/<string:id>")
def delete_attempts(id):

    with sql.connect("database.db") as con:
       cursor=con.cursor()

       query = "DELETE FROM ATTEMPTS WHERE id = ?" 

       cursor.execute(query,(id,))

       con.commit() 

    return redirect(url_for("attempts"))


@app.route("/edit_attempts/<string:id>", methods=["GET","POST"])
def edit_attempts(id):

    if request.method == "GET":
        form = AttemptsForm()

        with sql.connect("database.db") as con:
            con.row_factory = sql.Row
            cur=con.cursor()

            query = "SELECT * FROM ATTEMPTS WHERE (id = ?)"
            cur.execute(query,(id,))

            team = cur.fetchone()#matching element

            form.team_name.data = team["team"]
            form.matches.data = team["matches"]
            form.attempts.data = team["attempts"]
            form.attempts_on_target.data = team["attemptsOnTarget"]
            form.attempts_off_target.data = team["attemptsOffTarget"]
            form.attempts_blocked.data = team["attemptsBlocked"]

        return render_template("attempts/edit_attempts.html", form=form)

    if request.method == "POST":
        form = AttemptsForm(request.form)
        team_name = form.team_name.data
        matches = form.matches.data
        attempts = form.attempts.data
        attempts_on_target = form.attempts_on_target.data
        attempts_off_target = form.attempts_off_target.data
        attempts_blocked = form.attempts_blocked.data

        with sql.connect("database.db") as con:
            con.row_factory = sql.Row
            cur=con.cursor()
            query = "UPDATE ATTEMPTS SET team = ?, matches = ?, attempts = ?, attemptsOnTarget = ?, attemptsOffTarget = ?, attemptsBlocked = ?  WHERE id = ?"
            cur.execute(query,(team_name,matches,attempts,attempts_on_target,attempts_off_target,attempts_blocked,  id))
            con.commit()
        
        return redirect(url_for("attempts"))


@app.route("/attack")
def attack():
    with sql.connect("database.db") as con:
        con.row_factory = sql.Row
        cursor=con.cursor()

        query=""" SELECT * FROM ATTACK """

        cursor.execute(query)

        teams = cursor.fetchall()

    return render_template("attack/attack.html",teams=teams)

@app.route("/attack/add_attack", methods=["GET","POST"])
def add_attack():
    form = AttackForm(request.form)

    if request.method == "POST" and form.validate(): 
        team_name = form.team_name.data
        matches = form.matches.data
        total_corners = form.total_corners.data
        average_corners = form.average_corners.data
        crosses_attempted = form.crosses_attempted.data
        crossing_accuracy = form.crossing_accuracy.data

        with sql.connect("database.db") as con:
            
            cursor=con.cursor()
            query = "INSERT INTO ATTACK (team,matches,totalCorners,averageCorners,crossesAttempted,crossingAccuracy) VALUES (?,?,?,?,?,?)"
            
            cursor.execute(query,(team_name,matches,total_corners,float(average_corners),crosses_attempted,crossing_accuracy))
            con.commit()  

            cursor.close()  

        return redirect(url_for("attack"))
    
    else:
        return render_template("attack/add_attack.html", form=form)

@app.route("/delete_attack/<string:id>")
def delete_attack(id):

    with sql.connect("database.db") as con:
       cursor=con.cursor()

       query = "DELETE FROM ATTACK WHERE id = ?" 

       cursor.execute(query,(id,))

       con.commit() 

    return redirect(url_for("attack"))

@app.route("/edit_attack/<string:id>", methods=["GET","POST"])
def edit_attack(id):

    if request.method == "GET":
        form = AttackForm()

        with sql.connect("database.db") as con:
            con.row_factory = sql.Row
            cur=con.cursor()

            query = "SELECT * FROM ATTACK WHERE (id = ?)"
            cur.execute(query,(id,))

            team = cur.fetchone()

            form.team_name.data = team["team"]
            form.matches.data = team["matches"]
            form.total_corners.data = team["totalCorners"]
            form.average_corners.data = team["averageCorners"]
            form.crosses_attempted.data = team["crossesAttempted"]
            form.crossing_accuracy.data = team["crossingAccuracy"]

        return render_template("attack/edit_attack.html", form=form)

    if request.method == "POST":
        form = AttackForm(request.form)
        team_name = form.team_name.data
        matches = form.matches.data
        total_corners = form.total_corners.data
        average_corners = form.average_corners.data
        crosses_attempted = form.crosses_attempted.data
        crossing_accuracy = form.crossing_accuracy.data

        with sql.connect("database.db") as con:
            con.row_factory = sql.Row
            cur=con.cursor()
            query = "UPDATE ATTACK SET team = ?, matches = ?, totalCorners = ?, averageCorners = ?, crossesAttempted = ?, crossingAccuracy = ?  WHERE id = ?"
            cur.execute(query,(team_name,matches,total_corners,float(average_corners),crosses_attempted,crossing_accuracy,  id))
            con.commit()
        
        return redirect(url_for("attack"))







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