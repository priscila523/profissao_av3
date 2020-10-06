from config import *
from profissao import Profissao

@app.route("/")
def inicio():
    return 'Sistema para cadastrar profissões. '+\
        '<a href="/listar_profissoes">Listar Profissões</a>'

@app.route("/listar_profissoes")
def listar_profissoes():
    profissoes = db.session.query(Profissao).all()
    profissoes_em_json = [ x.json() for x in profissoes]
    resposta = jsonify(profissoes_em_json)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta 
    
@app.route("/incluir_profissao", methods=['post'])
def incluir_profissao():
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    dados = request.get_json() 
    try:
      nova = Profissao(**dados) 
      db.session.add(nova) 
      db.session.commit() 
    except Exception as e:
      resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta 

app.run(debug=True)