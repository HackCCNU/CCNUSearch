# coding: utf-8

from flask import Flask


app = Flask(__name__)
app.config['SECRET_KEY'] = 'CCNUHHHH'


from . import views, forms
