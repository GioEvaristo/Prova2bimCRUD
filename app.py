from flask import Flask, render_template, request, flash, redirect
from database import db
from flask_migrate import Migrate
from models import Jogos

app = Flask(__name__)
app.config['SECRET_KEY'] = '9ebe6f92407c97b3f989420e0e6bebcf9d1976b2e230acf9faf4783f5adffe1b'

conexao = "mysql+pymysql://alunos:cefetmg@127.0.0.1/ProvaGio"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route("/")
def jogos():
    j = Jogos.query.all()
    return render_template("index.html", dados = j)

@app.route("/add")
def jogos_add():
    return render_template("jogos_add.html")

@app.route("/save", methods=['POST'])
def jogos_save():
    nome = request.form.get('nome')
    categoria = request.form.get('categoria')
    classificacao_etaria = request.form.get('classificacao_etaria')
    if nome and categoria and classificacao_etaria:
        jogos = Jogos(nome, categoria, classificacao_etaria)
        db.session.add(jogos)
        db.session.commit()
        flash('Jogo salvo com sucesso!!!')
        return redirect('/')
    else:
        flash('Preencha todos os campos!!!')
        return redirect('/add')
    

if __name__ == '__main__':
    app.run()
