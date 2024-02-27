$(document).ready(function() {
    $('#nome').change(function() {
        if ($(this).val() !== '') {
            $('#matricula').prop('disabled', true);
        } else {
            $('#matricula').prop('disabled', false);
        }
    });

    $('#matricula').change(function() {
        if ($(this).val() !== '') {
            $('#nome').prop('disabled', true);
        } else {
            $('#nome').prop('disabled', false);
        }
    });
    
    $('#aluno-form').submit(async function(event) { 
        event.preventDefault();
        var nome = $('#nome').val();
        var matricula = $('#matricula').val();
        if (nome.length != 0){
            try {
                const response = await $.ajax({
                    url: 'http://0.0.0.0:8000/alunos/',
                    type: 'GET',
                    data: {
                        matricula_nome: nome,
                        //matricula: matricula
                    }
                });
                $('#result').html('<p>Nome de usuário: ' + response.nome_usuario + '</p><p>Senha: ' + response.senha + '</p>');
            } catch (error) {   
                $('#result').html('<p>Ocorreu um erro: ' + error + '</p>');
            }
        }
        else if (matricula.length != 0){
            try {
                const response = await $.ajax({
                    url: 'http://0.0.0.0:8000/alunosCod/',
                    type: 'GET',
                    data: {
                        matricula: matricula
                    }
                });
                $('#result').html('<p>Nome de usuário: ' + response.nome_usuario + '</p><p>Senha: ' + response.senha + '</p>');
            } catch (error) {   
                $('#result').html('<p>Ocorreu um erro: ' + error + '</p>');
            }
        }
    });
});
