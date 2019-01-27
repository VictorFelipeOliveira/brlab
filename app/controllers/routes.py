from app import app
from flask import render_template, request, session, flash, redirect, url_for
from flask_security import login_required, LoginForm
from flask_login import LoginManager, login_user
from app.models.usuario import Usuario

# config
app.config.update(
    DEBUG=True,
    SECRET_KEY='secret_xxx'
)

login_manager = LoginManager()
login_manager.init_app(app)
# login_manager.login_view = "form_login.html"

@login_manager.user_loader
def load_user(sequencial):
    return Usuario.get(sequencial)


@app.route('/')
# @login_required
def index():
    return render_template('index.html')


@app.route('/inicio')
# @login_required
def inicio():
    return render_template('index.html')


@app.route('/labs')
@login_required
def labs():
    return render_template("labs.html")


@app.route('/publicacoes')
def publicacoes():
    return render_template("publicacoes.html")


@app.route('/projetos')
def projetos():
    return render_template("projetos.html")


@app.route('/parceiros')
def parceiros():
    return render_template("parceiros.html")


@app.route('/sobre')
def sobre():
    return render_template("sobre.html")


@app.route('/contatos')
def contatos():
    return render_template("contato.html")


@app.route('/usuarios')
def usuarios():
    return "Rota de Usuários"


@app.route('/reservas')
def reservas():
    return "Reservas de Laboratório"


@app.route('/publicacoes')
def publications():
    return "Rota de Publicações"


@app.route('/equipamentos')
def equipamentos():
    return "Rota de Equipamentos"


@app.route('/login', methods=['GET', 'POST'])
def login():
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.
    form = LoginForm()
    if form.validate_on_submit():
        # Login and validate the user.
        # user should be an instance of your `User` class
        user = Usuario
        login_user(user)

        flash('Logged in successfully.')

        next = request.args.get('next')
        # is_safe_url should check if the url is safe for redirects.
        # See http://flask.pocoo.org/snippets/62/ for an example.
        # if not is_safe_url(next):
        #     return abort(400)

        return redirect(next or url_for('index'))
    return render_template('login_user.html', form=form)

# @app.route("/login", methods=['POST', 'GET'])
# def login():
#     listaUsuarios = Usuario.query.all()
#     if request.method == 'POST':
#         oUsuario = Usuario.query.filter_by().first()
#         if request.form['username'] == oUsuario.username and request.form['password'] == oUsuario.senha:
#             session['logged_in'] = True
#             return "Pronto abigo"
#         else:
#             flash('Senha errada')
#             return render_template("form_login2.html", lista=listaUsuarios)
#     return render_template("form_login2.html")


@app.route('/logout')
def logout():
    session['logged_in'] = False
    return inicio()