from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class SearchWordForm(FlaskForm):
    word = StringField('کلمه مورد نظر', validators=[DataRequired()])
    submit = SubmitField('جستجو')
