from flask import Flask,render_template,redirect,url_for,request
from form_classes import *
import sqlite3 as sql

app = Flask(__name__)

@app.route("/")
def index():
    db = sql.connect("database.db")
    c = db.cursor()
    c.execute("PRAGMA foreign_keys = ON")
    db.commit()
    db.close()

    return render_template("index.html")

@app.route("/error")
def error():
    return render_template("error.html")

@app.route("/teams")
def teams():
    with sql.connect("database.db") as con:
        con.row_factory = sql.Row
        cursor=con.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")

        query=""" SELECT * FROM TEAMS """

        cursor.execute(query)

        teams = cursor.fetchall()

    return render_template("teams/teams.html",teams=teams) 


@app.route("/teams/add_team", methods=["GET","POST"])
def add_team():
    form = TeamsForm(request.form)

    if request.method == "POST" and form.validate(): 
        team_name = form.team_name.data

        con = sql.connect("database.db") 

        try:
            
            cursor=con.cursor()
            query = "INSERT INTO TEAMS (teamName) VALUES (?)"
            cursor.execute("PRAGMA foreign_keys = ON")#this line enable f-key, without this sqlite doesnt enable f-keys by default
            
            cursor.execute(query,(team_name,))
            con.commit()  

            cursor.close() 

        except:
            con.rollback()
            return redirect(url_for("error"))

        return redirect(url_for("teams"))
    
    else:

        return render_template("teams/add_team.html", form=form) 


@app.route("/delete_team/<string:id>")
def delete_team(id):

    with sql.connect("database.db") as con:
        cursor=con.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")

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
            cur.execute("PRAGMA foreign_keys = ON")

            query = "SELECT teamName FROM TEAMS WHERE (teamId = ?)"
            cur.execute(query,(id,))
            team = cur.fetchone()#matching element

            form.team_name.data = team["teamName"]

        return render_template("teams/edit_team.html", form=form)

    if request.method == "POST":
        form = TeamsForm(request.form)
        new_name = form.team_name.data

        con = sql.connect("database.db") 
        try:
            con.row_factory = sql.Row
            cur=con.cursor()
            cur.execute("PRAGMA foreign_keys = ON")
            query = "UPDATE TEAMS SET teamName = ? WHERE teamId = ?"
            cur.execute(query,(new_name, id))
            con.commit()
        except:
            con.rollback()
            return redirect(url_for("error"))            
        
        return redirect(url_for("teams"))


@app.route("/attempts")
def attempts():
    with sql.connect("database.db") as con:
        con.row_factory = sql.Row
        cursor=con.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")

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

        con = sql.connect("database.db") 
        try:
            cursor=con.cursor()
            query = "INSERT INTO ATTEMPTS (team,matches,attempts,attemptsOnTarget,attemptsOffTarget,attemptsBlocked) VALUES (?,?,?,?,?,?)"
            cursor.execute("PRAGMA foreign_keys = ON")
            cursor.execute(query,(team_name,matches,attempts,attempts_on_target,attempts_off_target,attempts_blocked))

            if cursor.lastrowid == 0:
                return render_template("index.html")

            con.commit()  

            cursor.close() 

        except:
            con.rollback()
            return redirect(url_for("error"))

        return redirect(url_for("attempts"))
    
    else:
        return render_template("attempts/add_attempts.html", form=form) 

@app.route("/delete_attempts/<string:id>")
def delete_attempts(id):

    with sql.connect("database.db") as con:
       cursor=con.cursor()
       cursor.execute("PRAGMA foreign_keys = ON") 
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
            cur.execute("PRAGMA foreign_keys = ON")
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

        con = sql.connect("database.db")

        try:
            con.row_factory = sql.Row
            cur=con.cursor()
            cur.execute("PRAGMA foreign_keys = ON")
            query = "UPDATE ATTEMPTS SET team = ?, matches = ?, attempts = ?, attemptsOnTarget = ?, attemptsOffTarget = ?, attemptsBlocked = ?  WHERE id = ?"
            cur.execute(query,(team_name,matches,attempts,attempts_on_target,attempts_off_target,attempts_blocked,  id))
            con.commit()
            cur.close()
        except:
            con.rollback()
            return redirect(url_for("error"))            
        
        
        return redirect(url_for("attempts"))


@app.route("/attack")
def attack():
    with sql.connect("database.db") as con:
        con.row_factory = sql.Row
        cursor=con.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
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

        con = sql.connect("database.db") 

        try:            
            cursor=con.cursor()
            query = "INSERT INTO ATTACK (team,matches,totalCorners,averageCorners,crossesAttempted,crossingAccuracy) VALUES (?,?,?,?,?,?)"
            cursor.execute("PRAGMA foreign_keys = ON")
            cursor.execute(query,(team_name,matches,total_corners,float(average_corners),crosses_attempted,crossing_accuracy))
            con.commit()  

            cursor.close() 
        except:
            con.rollback()
            return redirect(url_for("error"))

        return redirect(url_for("attack"))
    
    else:
        return render_template("attack/add_attack.html", form=form)

@app.route("/delete_attack/<string:id>")
def delete_attack(id):

    with sql.connect("database.db") as con:
       cursor=con.cursor()
       cursor.execute("PRAGMA foreign_keys = ON")
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
            cur.execute("PRAGMA foreign_keys = ON")

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

        con = sql.connect("database.db")

        try:
            con.row_factory = sql.Row
            cur=con.cursor()
            cur.execute("PRAGMA foreign_keys = ON")
            query = "UPDATE ATTACK SET team = ?, matches = ?, totalCorners = ?, averageCorners = ?, crossesAttempted = ?, crossingAccuracy = ?  WHERE id = ?"
            cur.execute(query,(team_name,matches,total_corners,float(average_corners),crosses_attempted,crossing_accuracy,  id))
            con.commit()
            cur.close()
        except:
            con.rollback()
            return redirect(url_for("error"))

        return redirect(url_for("attack"))



#if __name__ == "__main__":
#    app.run(debug=True)





@app.route("/goals")
def goals():
    with sql.connect("database.db") as con:
        con.row_factory = sql.Row
        cursor=con.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")

        query=""" SELECT * FROM GOALS """

        cursor.execute(query)

        teams = cursor.fetchall()

    return render_template("goals/goals.html",teams=teams)

@app.route("/goal-type")
def goal_type():
    with sql.connect("database.db") as con:
        con.row_factory = sql.Row
        cursor=con.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")

        query=""" SELECT * FROM GOALTYPE """

        cursor.execute(query)

        teams = cursor.fetchall()
    return render_template("goal-type/goal-type.html",teams=teams)

@app.route("/goals/goals-add", methods=["GET","POST"])
def goals_add():
    form = GoalsForm(request.form)

    if request.method == "POST" and form.validate(): 
        TeamName = form.team_name.data
        Matches = form.matches.data
        TotalGoals = form.total_goals.data
        AverageGoals = form.average_goals.data
        GoalsConceded = form.goals_conceded.data
        AverageConceded = form.average_conceded.data
        GoalDifference = form.goal_difference.data

        con = sql.connect("database.db")
        try:
            cursor=con.cursor()
            query = "INSERT INTO GOALS (team,matches,totalGoals,averageGoals,goalsConceded,averageConceded,goalDifference) VALUES (?,?,?,?,?,?,?)"
            cursor.execute("PRAGMA foreign_keys = ON")
            cursor.execute(query,(TeamName,Matches,TotalGoals,float(AverageGoals),GoalsConceded,float(AverageConceded),GoalDifference))
            con.commit()

            cursor.close()
        except:
            con.rollback()
            return redirect(url_for("error"))
        return redirect(url_for("goals"))
    else:
        return render_template("goals/goals-add.html", form=form)

@app.route("/goal-type/goal-type-add", methods=["GET","POST"])
def goal_type_add():
    form = GoalTypeForm(request.form)

    if request.method == "POST" and form.validate(): 
        TeamName = form.team_name.data
        Goals = form.goals.data
        LeftFoot = form.left_foot.data
        RightFoot = form.right_foot.data
        Header = form.header.data
        OwnGoals = form.own_goals.data
        Penalties = form.penalties.data
        con = sql.connect("database.db")
        try:
            cursor=con.cursor()
            query = "INSERT INTO GOALTYPE (team,goals,leftFoot,rightFoot,header,ownGoal,Penalties) VALUES (?,?,?,?,?,?,?)"
            cursor.execute("PRAGMA foreign_keys = ON")
            cursor.execute(query,(TeamName,Goals,LeftFoot,RightFoot,Header,OwnGoals,Penalties))
            con.commit()

            cursor.close()
        except:
            con.rollback()
            return redirect(url_for("error"))
        return redirect(url_for("goal_type"))
    else:
        return render_template("goal-type/goal-type-add.html", form=form) 


@app.route("/delete_goal_type/<string:id>")
def delete_goal_type(id):
    
    with sql.connect("database.db") as con:
       cursor=con.cursor()
       cursor.execute("PRAGMA foreign_keys = ON")
       query = "DELETE FROM GOALTYPE WHERE id = ?" 

       cursor.execute(query,(id))

       con.commit() 

   
    return redirect(url_for("goal_type"))


@app.route("/delete_goals/<string:id>")
def delete_goals(id):
    with sql.connect("database.db") as con:
       cursor=con.cursor()
       cursor.execute("PRAGMA foreign_keys = ON")
       query = "DELETE FROM GOALS WHERE id = ?" 

       cursor.execute(query,(id))

       con.commit() 
   
    return redirect(url_for("goals"))


@app.route("/edit_goal_type/<string:id>",methods = ["GET","POST"])
def edit_goal_type(id):

   if request.method == "GET":      
       updateForm = GoalTypeForm()

       with sql.connect("database.db") as con:
            con.row_factory = sql.Row
            cur=con.cursor()
            cur.execute("PRAGMA foreign_keys = ON")
            query = "SELECT * FROM GOALTYPE WHERE (id = ?)"
            cur.execute(query,(id))
            row = cur.fetchone()

            updateForm.team_name.data = row["team"]
            updateForm.goals.data = row["goals"]
            updateForm.left_foot.data = row["leftFoot"]
            updateForm.right_foot.data = row["rightFoot"]
            updateForm.header.data = row["header"]
            updateForm.own_goals.data = row["owngoal"]
            updateForm.penalties.data = row["Penalties"]

       return render_template("goal-type/goal-type-update.html", form=updateForm)

   if request.method == "POST":
      updateForm = GoalTypeForm(request.form)
      newTeamName = updateForm.team_name.data
      newGoals = updateForm.goals.data
      newLeftFoot = updateForm.left_foot.data
      newRightFoot = updateForm.right_foot.data
      newHeader = updateForm.header.data
      newOwnGoals = updateForm.own_goals.data
      newPenalties = updateForm.penalties.data

      con = sql.connect("database.db")

      try:
          con.row_factory = sql.Row
          cur=con.cursor()
          cur.execute("PRAGMA foreign_keys = ON")
          query = "UPDATE GOALTYPE SET team = ?, goals = ?, leftFoot = ?, rightFoot = ?, header = ?, ownGoal = ?, Penalties = ? WHERE id = ?"
          cur.execute(query,( newTeamName,newGoals,newLeftFoot,newRightFoot,newHeader,newOwnGoals,newPenalties,id))
          con.commit()
          cur.close()
      except:
          con.rollback()
          return redirect(url_for("error")) 
      return redirect(url_for("goal_type"))

      
@app.route("/edit_goals/<string:id>",methods = ["GET","POST"])
def edit_goals(id):

    if request.method == "GET":      
        updateForm = GoalsForm()

        with sql.connect("database.db") as con:
            con.row_factory = sql.Row
            cur=con.cursor()
            cur.execute("PRAGMA foreign_keys = ON")
            query = "SELECT * FROM GOALS WHERE (id = ?)"
            cur.execute(query,(id))
            row = cur.fetchone()

            updateForm.team_name.data = row["team"]
            updateForm.matches.data = row["matches"]
            updateForm.total_goals.data = row["totalgoals"]
            updateForm.average_goals.data = row["averagegoals"]
            updateForm.goals_conceded.data = row["goalsconceded"]
            updateForm.average_conceded.data = row["averageconceded"]
            updateForm.goal_difference.data = row["goaldifference"]

        return render_template("goals/goals-update.html", form=updateForm)

    if request.method == "POST":
        updateForm = GoalsForm(request.form)
        newTeamName = updateForm.team_name.data
        newMatches = updateForm.matches.data
        newTotalGoals = updateForm.total_goals.data
        newAverageGoals = updateForm.average_goals.data
        newGoalsConceded = updateForm.goals_conceded.data
        newAverageConceded = updateForm.average_conceded.data
        newGoalDifference = updateForm.goal_difference.data
        con = sql.connect("database.db")

        try:
            con.row_factory = sql.Row
            cur=con.cursor()
            cur.execute("PRAGMA foreign_keys = ON")
            query = "UPDATE GOALS SET team = ?,matches = ?,totalgoals = ?,averagegoals = ?,goalsconceded = ?,averageconceded = ?,goaldifference = ? WHERE id = ?"
            cur.execute(query,(newTeamName,newMatches,newTotalGoals,float(newAverageGoals),newGoalsConceded,float(newAverageConceded),newGoalDifference,id))
            con.commit() 
            con.close()
        except:
            con.rollback()
            return redirect(url_for("error"))
        return redirect(url_for("goals"))
      


@app.route("/defence")
def defence():
    with sql.connect("database.db") as con:
        con.row_factory = sql.Row
        cursor=con.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")

        query=""" SELECT * FROM DEFENCE """

        cursor.execute(query)

        teams = cursor.fetchall()

    return render_template("defence/defence.html",teams=teams)



@app.route("/defence/add_defence", methods=["GET","POST"])
def add_defence():
    form = DefenceForm(request.form)

    if request.method == "POST" and form.validate(): 
        team_name = form.team_name.data
        saves_made = form.saves_made.data
        blocks = form.blocks.data
        total_clearances = form.total_clearances.data
        interceptions = form.interceptions.data
        recoveries = form.recoveries.data
        goals_conceded = form.goals_conceded.data

        con = sql.connect("database.db") 
        try:
            cursor=con.cursor()
            query = "INSERT INTO DEFENCE (team,savesMade,blocks,totalClearances,interceptions,recoveries,GoalsConceded) VALUES (?,?,?,?,?,?,?)"
            cursor.execute("PRAGMA foreign_keys = ON")
            cursor.execute(query,(team_name,saves_made,blocks,total_clearances,interceptions,recoveries,goals_conceded))

            if cursor.lastrowid == 0:
                return render_template("index.html")

            con.commit()  

            cursor.close() 

        except:
            con.rollback()
            return redirect(url_for("error"))

        return redirect(url_for("defence"))
    
    else:
        return render_template("defence/add_defence.html", form=form)


@app.route("/delete_defence/<string:id>")
def delete_defence(id):

    with sql.connect("database.db") as con:
       cursor=con.cursor()
       cursor.execute("PRAGMA foreign_keys = ON") 
       query = "DELETE FROM DEFENCE WHERE id = ?" 

       cursor.execute(query,(id,))

       con.commit() 

    return redirect(url_for("defence"))


@app.route("/edit_defence/<string:id>", methods=["GET","POST"])
def edit_defence(id):

    if request.method == "GET":
        form = DefenceForm()

        with sql.connect("database.db") as con:
            con.row_factory = sql.Row
            cur=con.cursor()
            cur.execute("PRAGMA foreign_keys = ON")
            query = "SELECT * FROM DEFENCE WHERE (id = ?)"
            cur.execute(query,(id,))

            team = cur.fetchone()

            form.team_name.data = team["team"]
            form.saves_made.data = team["savesMade"]
            form.blocks.data = team["blocks"]
            form.total_clearances.data = team["totalClearances"]
            form.interceptions.data = team["interceptions"]
            form.recoveries.data = team["recoveries"]
            form.goals_conceded.data = team["GoalsConceded"]

        return render_template("defence/edit_defence.html", form=form)

    if request.method == "POST":
        team_name = form.team_name.data
        saves_made = form.saves_made.data
        blocks = form.blocks.data
        total_clearances = form.total_clearances.data
        interceptions = form.interceptions.data
        recoveries = form.recoveries.data
        goals_conceded = form.goals_conceded.data

        con = sql.connect("database.db")

        try:
            con.row_factory = sql.Row
            cur=con.cursor()
            cur.execute("PRAGMA foreign_keys = ON")
            query = "UPDATE DEFENCE SET team = ?, savesMade = ?, blocks = ?, totalClearances = ?, interceptions = ?, recoveries = ?, GoalsConceded = ?  WHERE id = ?"
            cur.execute(query,(team_name,saves_made,blocks,total_clearances,interceptions,recoveries,goals_conceded,  id))
            con.commit()
            cur.close()
        except:
            con.rollback()
            return redirect(url_for("error"))            
        
        
        return redirect(url_for("defence"))



@app.route("/discipline")
def discipline():
    with sql.connect("database.db") as con:
        con.row_factory = sql.Row
        cursor=con.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        query=""" SELECT * FROM DISCIPLINE """

        cursor.execute(query)

        teams = cursor.fetchall()

    return render_template("discipline/discipline.html",teams=teams)



@app.route("/discipline/add_discipline", methods=["GET","POST"])
def add_discipline():
    form = DisciplineForm(request.form)

    if request.method == "POST" and form.validate(): 
        team_name = form.team_name.data
        matches = form.matches.data
        fouls_win = form.fouls_win.data
        fouls_conceded = form.fouls_conceded.data
        yellow_cards = form.yellow_cards.data
        red_cards = form.red_cards.data

        con = sql.connect("database.db") 

        try:            
            cursor=con.cursor()
            query = "INSERT INTO DISCIPLINE (team,matches,foulsWin,foulsConceded,yellowCards,redCards) VALUES (?,?,?,?,?,?)"
            cursor.execute("PRAGMA foreign_keys = ON")
            cursor.execute(query,(team_name,matches,fouls_win,fouls_conceded,yellow_cards,red_cards))
            con.commit()  

            cursor.close() 
        except:
            con.rollback()
            return redirect(url_for("error"))

        return redirect(url_for("discipline"))
    
    else:
        return render_template("discipline/add_discipline.html", form=form)

@app.route("/delete_discipline/<string:id>")
def delete_discipline(id):

    with sql.connect("database.db") as con:
       cursor=con.cursor()
       cursor.execute("PRAGMA foreign_keys = ON")
       query = "DELETE FROM DISCIPLINE WHERE id = ?" 

       cursor.execute(query,(id,))

       con.commit() 

    return redirect(url_for("discipline"))

@app.route("/edit_discipline/<string:id>", methods=["GET","POST"])
def edit_discipline(id):

    if request.method == "GET":
        form = DisciplineForm()

        with sql.connect("database.db") as con:
            con.row_factory = sql.Row
            cur=con.cursor()
            cur.execute("PRAGMA foreign_keys = ON")

            query = "SELECT * FROM DISCIPLINE WHERE (id = ?)"
            cur.execute(query,(id,))

            team = cur.fetchone()

            form.team_name.data = team["team"]
            form.matches.data = team["matches"]
            form.fouls_win.data = team["foulsWin"]
            form.fouls_conceded.data = team["foulsConceded"]
            form.yellow_cards.data = team["yellowCards"]
            form.red_cards.data = team["redCards"]

        return render_template("discipline/edit_discipline.html", form=form)

    if request.method == "POST":
        form = DisciplineForm(request.form)
        team_name = form.team_name.data
        matches = form.matches.data
        fouls_win = form.fouls_win.data
        fouls_conceded = form.fouls_conceded.data
        yellow_cards = form.yellow_cards.data
        red_cards = form.red_cards.data

        con = sql.connect("database.db")

        try:
            con.row_factory = sql.Row
            cur=con.cursor()
            cur.execute("PRAGMA foreign_keys = ON")
            query = "UPDATE DISCIPLINE SET team = ?, matches = ?, foulsWin = ?, foulsConceded = ?, yellowCards = ?, redCards = ?  WHERE id = ?"
            cur.execute(query,(team_name,matches,fouls_win,fouls_conceded,yellow_cards,red_cards,  id))
            con.commit()
            cur.close()
        except:
            con.rollback()
            return redirect(url_for("error"))

        return redirect(url_for("discipline"))




if __name__ == "__main__":
    app.run(debug=True)