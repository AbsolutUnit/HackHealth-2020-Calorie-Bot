from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired

class subForm(FlaskForm):
    #Age height weight stringfield
    age = StringField('Age', validators=[DataRequired()])
    height = StringField('Height', validators=[DataRequired()])
    weight = StringField('Weight', validators=[DataRequired()])
    # sex = SelectField("Sex", choices = [('male','Male'), ('female','Female')])
    # activity = SelectField("Activity Level", choices = [("0","Sedentary"),("1","Lightly Active"),("2","Moderately Active"),("3","Very Active"),("4","Extra Active")])
   
    submit = SubmitField('Submit')