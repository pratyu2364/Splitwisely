from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField
from wtforms.validators import DataRequired,Length


class FriendForm(FlaskForm):
    number_of_members = IntegerField('Number of people to share the bill :',
                           validators=[DataRequired(),Length(min=2, max=20)])
    friends_list = StringField('List of friends(separated by comma) : ',
                           validators=[DataRequired(), Length(min=2, )])
    money_paid = StringField('Money paid by each(separated by commas)',
                           validators=[DataRequired(), Length(min=2)])
    submit = SubmitField('Submit')


class PercentageDiv(FlaskForm):
    number_of_members = IntegerField('Number of people to share the bill :',
                                     validators=[DataRequired(), Length(min=2)])
    friends_list = StringField('List of friends(separated by comma) : ',
                               validators=[DataRequired(), Length(min=2)])
    money_paid = StringField('Money paid by each(separated by commas)',
                             validators=[DataRequired(), Length(min=2)])
    percentage_each = StringField('Percentage of total money to pay by each(separated by commas)',
                             validators=[DataRequired(), Length(min=2)])
    submit = SubmitField('Submit')
