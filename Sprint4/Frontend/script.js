document.addEventListener('DOMContentLoaded', () => {
    mostrarAba('clientes');
    carregarClientes();
    carregarProfissionais();
    carregarServicos();
    carregarAgendamentos();

    // Carregar opções para o formulário de agendamento
    carregarOpcoesAgendamento();

    document.getElementById('formCliente').addEventListener('submit', (e) => {
        e.preventDefault();
        const cliente = {
            nome: document.getElementById('nome').value,
            telefone: document.getElementById('telefone').value,
            email: document.getElementById('email').value
        };
        criarCliente(cliente);
    });

    document.getElementById('formProfissional').addEventListener('submit', (e) => {
        e.preventDefault();
        const profissional = {
            nome: document.getElementById('nomeProfissional').value,
            especialidade: document.getElementById('especialidade').value
        };
        criarProfissional(profissional);
    });

    document.getElementById('formServico').addEventListener('submit', (e) => {
        e.preventDefault();
        const servico = {
            nome_servico: document.getElementById('nomeServico').value,
            descricao: document.getElementById('descricao').value,
            preco: document.getElementById('preco').value
        };
        criarServico(servico);
    });

    document.getElementById('formAgendamento').addEventListener('submit', (e) => {
        e.preventDefault();
        const agendamento = {
            cliente_id: document.getElementById('cliente_id').value,
            servico_id: document.getElementById('servico_id').value,
            profissional_id: document.getElementById('profissional_id').value,
            data_hora: document.getElementById('data_hora').value
        };
        criarAgendamento(agendamento);
    });
});

// Função para carregar opções de clientes, serviços e profissionais no formulário de agendamento
async function carregarOpcoesAgendamento() {
    const clientes = await fetch('http://localhost:5000/clientes').then(res => res.json());
    const servicos = await fetch('http://localhost:5000/servicos').then(res => res.json());
    const profissionais = await fetch('http://localhost:5000/profissionais').then(res => res.json());

    const clienteSelect = document.getElementById('cliente_id');
    const servicoSelect = document.getElementById('servico_id');
    const profissionalSelect = document.getElementById('profissional_id');

    clientes.forEach(cliente => {
        const option = document.createElement('option');
        option.value = cliente.id;
        option.textContent = cliente.nome;
        clienteSelect.appendChild(option);
    });

    servicos.forEach(servico => {
        const option = document.createElement('option');
        option.value = servico.id;
        option.textContent = servico.nome_servico;
        servicoSelect.appendChild(option);
    });

    profissionais.forEach(profissional => {
        const option = document.createElement('option');
        option.value = profissional.id;
        option.textContent = profissional.nome;
        profissionalSelect.appendChild(option);
    });
}

// Funções para mostrar/ocultar abas
function mostrarAba(aba) {
    document.querySelectorAll('.aba').forEach(sec => sec.style.display = 'none');
    document.getElementById(aba).style.display = 'block';
}

// Funções para Clientes, Profissionais, Serviços e Agendamentos (mantidas como antes)
// ...