from flask import Flask, request, render_template,flash, redirect, url_for
from .forms import UserForm
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config

application =  Flask(__name__)

application.config.from_object(Config)
db = SQLAlchemy(application)
migrate = Migrate(application, db)
from .models import User
@application.route('/', methods=['GET','POST'])
@application.route('/index', methods=['GET','POST'])
def index():
    form = UserForm()
    if form.validate_on_submit():
        user = User(name=form.name.data, phonenumber=form.phonenumber.data,
        email=form.email.data, propertyaddress=form.propertyaddress.data, notes=form.notes.data)
        db.session.add(user)
        db.session.commit()
        flash('Thanks for submitting your info!'.format(
            form.name.data
        ))
        return redirect(url_for('index'))
    return render_template('index.html',form=form)

@application.route('/about')
def about():
    return render_template('about.html')

@application.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@application.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500

if __name__ == '__main__':
    application.run()