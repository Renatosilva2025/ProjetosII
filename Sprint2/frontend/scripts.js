document.getElementById('login-form').addEventListener('submit', function(event) {
    event.preventDefault();
    // Lógica de autenticação
    alert('Login realizado com sucesso!');
});

document.getElementById('schedule-form').addEventListener('submit', function(event) {
    event.preventDefault();
    // Lógica de agendamento
    alert('Agendamento realizado com sucesso!');
});

document.getElementById('contact-form').addEventListener('submit', function(event) {
    event.preventDefault();
    // Lógica de envio de mensagem
    alert('Mensagem enviada com sucesso!');
});
