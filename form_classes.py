#these classes are used for creating forms with WTForms
from wtforms import Form,StringField,validators,IntegerField,DecimalField

#eğer takım isimlerini değiştirmeye kalkarsam bağlantı kopabilir ona ne yapıcaz

class TeamsForm(Form):
   team_name = StringField("Team name:", validators=[validators.DataRequired()])
   coach = StringField("Coach",validators=[validators.DataRequired()])
   stadium = StringField("Stadium",validators=[validators.DataRequired()])

class AttackForm(Form):
   team_name = StringField("Team name:", validators=[validators.DataRequired()])
   matches = IntegerField("Matches: ", validators=[validators.DataRequired()])
   total_corners = IntegerField("Total Corners: ", validators=[validators.DataRequired()])
   average_corners = DecimalField("Average Corners: ", validators=[validators.DataRequired()])
   crosses_attempted = IntegerField("Crosses Attempted: ", validators=[validators.DataRequired()])
   crossing_accuracy = IntegerField("Crossing Accuracy: ", validators=[validators.DataRequired()])

class AttemptsForm(Form):
   team_name = StringField("Team name:", validators=[validators.DataRequired()])
   matches = IntegerField("Matches: ", validators=[validators.DataRequired()])
   attempts = IntegerField("Attempts: ", validators=[validators.DataRequired()])
   attempts_on_target =IntegerField("Attempts On Target: ", validators=[validators.DataRequired()])
   attempts_off_target = IntegerField("Attempts Off Target: ", validators=[validators.DataRequired()])
   attempts_blocked = IntegerField("Attempts Blocked: ", validators=[validators.DataRequired()])

class GoalsForm(Form):
   team_name = StringField("Team name:", validators=[validators.DataRequired()])
   matches = IntegerField("Matches: ", validators=[validators.DataRequired()])
   total_goals = IntegerField("Total Goals: ", validators=[validators.DataRequired()])
   average_goals = IntegerField("Average Goals: ", validators=[validators.DataRequired()])
   goals_conceded =IntegerField("Goals Conceded: ", validators=[validators.DataRequired()])
   average_conceded = IntegerField("Average Conceded: ", validators=[validators.DataRequired()])
   goal_difference = IntegerField("Goal Difference: ", validators=[validators.DataRequired()])

class GoalTypeForm(Form):
   team_name = StringField("Team name:", validators=[validators.DataRequired()])
   goals = IntegerField("Goals: ", validators=[validators.DataRequired()])
   left_foot = IntegerField("Left Foot: ", validators=[validators.DataRequired()])
   right_foot = IntegerField("Right Foot: ", validators=[validators.DataRequired()])
   header =IntegerField("Header: ", validators=[validators.DataRequired()])
   own_goals = IntegerField("Own Goals: ", validators=[validators.DataRequired()])
   penalties = IntegerField("Penalties: ", validators=[validators.DataRequired()])


class DefenceForm(Form):
   team_name = StringField("Team name:", validators=[validators.DataRequired()])
   saves_made = IntegerField("Saves Made: ", validators=[validators.DataRequired()])
   blocks = IntegerField("Blocks: ", validators=[validators.DataRequired()])
   total_clearances = IntegerField("Total Clearances: ", validators=[validators.DataRequired()])
   interceptions = IntegerField("Interceptions: ", validators=[validators.DataRequired()])
   recoveries = IntegerField("Recoveries: ", validators=[validators.DataRequired()])
   goals_conceded = IntegerField("Goals Conceded: ", validators=[validators.DataRequired()])

class DisciplineForm(Form):
   team_name = StringField("Team name:", validators=[validators.DataRequired()])
   matches = IntegerField("Matches: ", validators=[validators.DataRequired()])
   fouls_won = IntegerField("Fouls Won: ", validators=[validators.DataRequired()])
   fouls_conceded =IntegerField("Fouls Conceded: ", validators=[validators.DataRequired()])
   yellow_cards = IntegerField("Yellow Cards: ", validators=[validators.DataRequired()])
   red_cards = IntegerField("Red Cards: ", validators=[validators.DataRequired()])

