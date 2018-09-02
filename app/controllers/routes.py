from app import app
from flask import render_template
from app.models import User

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/begin')
def begin():
    return render_template("contact.html");

@app.route('/labs')
def labs():
    return render_template("about.html");

@app.route('/publications')
def publications():
    return render_template("about.html");

@app.route('/projects')
def projects():
    return render_template("about.html");

@app.route('/partners')
def partners():
    return render_template("about.html");

@app.route('/about')
def about():
    return render_template("about.html");

@app.route('/contact')
def contact():
    return render_template("contact.html");

# @app.route('/profile/<email>')
# @login_required
# def profile(email):
#     user = User.query.filter_by(email = email).first()
# return render_template("profile.html", user=user)


# @app.route('/post_user',methods=['POST'])
# def post_user():
#     user = User(request.form['username'], request.form['email'], request.form['password'])
#     db.session.add(user)
#     db.session.commit()
#     return redirect(url_for('index'))
