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


