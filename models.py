from database import db

class Jogos(db.Model):
    __tablename__= "jogos"
    id_jogo = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    categoria = db.Column(db.String(50))
    classificacao_etaria = db.Column(db.Integer)

    # construtor
    def __init__(self, nome, categoria, classificacao_etaria):
        self.nome = nome
        self.categoria = categoria
        self.classificacao_etaria = classificacao_etaria

    # representação do objeto criado...
    def __repr__(self):
        return "<Jogo: {}>".format(self.nome)