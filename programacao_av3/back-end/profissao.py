from config import *

class Profissao(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    funcao = db.Column(db.String(254))
    salario = db.Column(db.Integer)
    detalhe = db.Column(db.String(254))
    caracteristica = db.Column(db.String(254))

    def __str__(self):
        return str(self.id)+") " + self.nome + ", " +\
            self.funcao + ", " + str(self.salario) + ", " +\
            self.detalhe + ", " + self.caracteristica

    def json(self):
        return ({
            "id": self.id,
            "nome": self.nome,
            "funcao": self.funcao,
            "salario": self.salario,
            "detalhe": self.detalhe,
            "caracteristica": self.caracteristica
        })