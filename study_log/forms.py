from flask_wtf import FlaskForm
from wtforms import TextAreaField, IntegerField, SubmitField, DateField
from wtforms.validators import DataRequired, Required

class LogForm(FlaskForm):
    date = DateField('日時', format="%Y-%m-%d")
    time = IntegerField('作業時間', validators=[
        Required(u"作業時間を入力してください")
    ])
    memo = TextAreaField('作業メモ')
    todo = TextAreaField('Todo')
    submit = SubmitField('登録')