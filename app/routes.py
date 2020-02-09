from flask import render_template
from app import app
from app.forms import subForm
from app.main import Plan

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = subForm()
    if form.validate_on_submit():
        calorie_count = 2000
        meal_count = 3


        return "valid"
    
    return render_template('index.html', form=form)