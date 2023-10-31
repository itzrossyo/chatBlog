from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'cV.HIE?4g90ag~?8*YM:NuTHMGGw%~'

posts = [
    {
        'author': ' Corey schafer',
        'title': 'Blog Post 1',
        'content': 'first post',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': ' Corey schafer',
        'title': 'Blog Post 2',
        'content': 'second post',
        'date_posted': 'April 22, 2018'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@test.com' and form.password.data == 'password':
            flash('you are logged in', 'success')
            return redirect(url_for('home'))
        else:
            flash('login failed please try again', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
