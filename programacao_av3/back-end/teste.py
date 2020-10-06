from profissao import *
import os

if __name__ == "__main__":

    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    db.create_all()

    p1 = Profissao(nome = "Arquitetura e Urbanismo", funcao = "construcao civil", 
    salario = 4823, detalhe = "desenvolve para estetica e estrutural de projetos civis", 
    caracteristica = "pode assinar predios de ate 4 andares sem engenheiro civil")
    p2 = Profissao(nome = "Engenharia Civil", funcao = "construcao civil", 
    salario = 6653, detalhe = "constroi pontes, barragens, etc", 
    caracteristica = "esta envolvido com projeto maiores")
    p3 = Profissao(nome = "Medico Veterinario", funcao = "cuidado de animais", 
    salario = 3524, detalhe = "cuida de todos os tipos de animais, variando pela expecializacao", 
    caracteristica = "existem varias areas na medicina veterinaria")
    p4 = Profissao(nome = "Administracao", funcao = "administra negacios", 
    salario = 7643, detalhe = "planejar, organizar, dirigir e controlar", 
    caracteristica = "traz lucro, evita desperdicio e reduz custos")

    db.session.add(p1)
    db.session.add(p2)
    db.session.add(p3)
    db.session.add(p4)
    db.session.commit()
    
    print(p1.json())
    print(p2.json())
    print(p3.json())
    print(p4.json())
