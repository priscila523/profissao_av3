$(function() { 
    
    function exibir_profissoes() {
        $.ajax({
            url: 'http://localhost:5000/listar_profissoes',
            method: 'GET',
            dataType: 'json', 
            success: listar, 
            error: function() {
                alert("erro ao ler dados, verifique o backend");
            }
        });
         
        function listar (profissoes) {
            $('#corpoTabelaProfissoes').empty();
            mostrar_conteudo("tabelaProfissoes");      
            for (var i in profissoes) { 
                lin = '<tr>' +
                '<td>' + profissoes[i].nome + '</td>' + 
                '<td>' + profissoes[i].funcao + '</td>' + 
                '<td>' + profissoes[i].salario + '</td>' + 
                '<td>' + profissoes[i].detalhe + '</td>' + 
                '<td>' + profissoes[i].caracteristica + '</td>' + 
                '</tr>';
                $('#corpoTabelaProfissoes').append(lin);
            }
        }
    }

    function mostrar_conteudo(identificador) {
        $("#tabelaProfissoes").addClass('invisible');
        $("#conteudoInicial").addClass('invisible');
        $("#"+identificador).removeClass('invisible');      
    }

    $(document).on("click", "#linkListarProfissoes", function() {
        exibir_profissoes();
    });
    
    $(document).on("click", "#linkInicio", function() {
        mostrar_conteudo("conteudoInicial");
    });

    $(document).on("click", "#btIncluirProfissao", function() {
        nome = $("#campoNome").val();
        funcao = $("#campoFuncao").val();
        salario = $("#campoSalario").val();
        detalhe = $("#campoDetalhe").val();
        caracteristica = $("#campoCaracteristica").val();
        var dados = JSON.stringify({ nome: nome, funcao: funcao, salario: salario, detalhe: detalhe, caracteristica: caracteristica });
        $.ajax({
            url: 'http://localhost:5000/incluir_profissao',
            type: 'POST',
            dataType: 'json', 
            contentType: 'application/json', 
            data: dados, 
            success: profissaoIncluida, 
            error: erroAoIncluir
        });
        function profissaoIncluida (retorno) {
            if (retorno.resultado == "ok") { 
                alert("Profissao incluída com sucesso!");
                $("#campoNome").val("");
                $("#campoFuncao").val("");
                $("#campoSalario").val("");
                $("#campoDetalhe").val("");
                $("#campoCaracteristica").val("");
            } else {
                alert(retorno.resultado + ":" + retorno.detalhes);
            }            
        }
        function erroAoIncluir (retorno) {
            alert("ERRO: "+retorno.resultado + ":" + retorno.detalhes);
        }
    });

    $('#modalIncluirProfissao').on('hide.bs.modal', function (e) {
        if (! $("#tabelaProfissoes").hasClass('invisible')) {
            exibir_profissoes();
        }
    });

    mostrar_conteudo("conteudoInicial");
});