$(document).ready(function() {
    $('#aluno-form').submit(function(event) {
        event.preventDefault();
        var nome = $('#nome').val();
        var matricula = $('#matricula').val();
        
        $.ajax({
            url: 'sua_api/alunos/',
            type: 'GET',
            data: {
                nome: nome,
                matricula: matricula
            },
            success: function(response) {
                $('#result').html('<p>Nome de usuário: ' + response.nome_usuario + '</p><p>Senha: ' + response.senha + '</p>');
            },
            error: function(xhr, status, error) {
                $('#result').html('<p>Ocorreu um erro: ' + error + '</p>');
            }
        });
    });
});
