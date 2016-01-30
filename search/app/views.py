# coding: utf-8
from . import app
from flask import render_template
from .forms import SearchForm
import redis


# test views
@app.route('/test/')
def test():
    """测试视图"""
    return "<h1>just tell you everything is ok!</h1>"


# you can writing your views here
@app.route('/', methods=['GET', 'POST'])
@app.route('/search/', methods=['GET', 'POST'])
def search():
    """搜索视图"""
    form = SearchForm()
    id = '请查询'
    if form.validate_on_submit():
        pool = redis.ConnectionPool(host='host', port=port, db=0)
        r = redis.Redis(connection_pool = pool)
        stu = form.stu.data
        id = r.get(stu)
        if (id == None):
            id = 'CCNU查无此人...'
    return render_template('search.html',
        form=form,
        id=id
    )

