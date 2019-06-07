from flask import Blueprint, render_template, flash,

auth = Blueprint('site', __name__)

@auth.route('/',)
def login1():
    a='10'
    if a=='10' :
        d={"a":"succefully"}
        flash('login succefully')
        return render_template('index.html')
    else:
        error='hello world'

    return render_template('login.html',  error=error)