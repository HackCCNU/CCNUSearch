# coding: utf-8
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required


class SearchForm(Form):
    stu = StringField(validators=[Required()])
    submit = SubmitField('search')

