from app import app
from flask import render_template, request, session, flash, redirect, url_for
# from flask_security import login_required, LoginForm
from flask_login import LoginManager, login_user, login_required
from app.models.usuario import Usuario
from app.models.forms import LoginForm


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
    form = LoginForm()
    if form.validate_on_submit():
        user = Usuario.query.filter_by(username=form.username.data).first()
        print (user)
        if user and user.password == form.senha.data:
            login_user(user)
            return redirect(url_for('inicio'))
        else:
            flash("Login inválido")
    else:
        print(form.errors)
    return render_template('form_login.html', form=form)



@app.route('/logout')
def logout():
    session['logged_in'] = False
    return inicio()
