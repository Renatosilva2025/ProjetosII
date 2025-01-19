const express = require('express');
const mysql = require('mysql');
const bodyParser = require('body-parser');
const app = express();
const port = 3000;

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

const db = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'password',
    database: 'clinica'
});

db.connect((err) => {
    if (err) throw err;
    console.log('Conectado ao banco de dados');
});

// Rota de login
app.post('/login', (req, res) => {
    const { cpf, senha } = req.body;
    const query = 'SELECT * FROM pacientes WHERE cpf = ? AND senha = ?';
    db.query(query, [cpf, senha], (err, results) => {
        if (err) throw err;
        if (results.length > 0) {
            res.send({ status: 'success', user: results[0] });
        } else {
            res.send({ status: 'error', message: 'CPF ou senha incorretos' });
        }
    });
});

// Rota de agendamento
app.post('/agendar', (req, res) => {
    const { paciente_id, funcionario_id, procedimento_id, data_horario } = req.body;
    const query = 'INSERT INTO horarios (paciente_id, funcionario_id, procedimento_id, data_horario) VALUES (?, ?, ?, ?)';
    db.query(query, [paciente_id, funcionario_id, procedimento_id, data_horario], (err, results) => {
        if (err) throw err;
        res.send({ status: 'success', message: 'Agendamento realizado com sucesso' });
    });
});

// Rota de contato com profissionais
app.post('/contato', (req, res) => {
    const { funcionario_id, paciente_id, mensagem } = req.body;
    const query = 'INSERT INTO contatos_profissionais (funcionario_id, paciente_id, mensagem, data_contato) VALUES (?, ?, ?, NOW())';
    db.query(query, [funcionario_id, paciente_id, mensagem], (err, results) => {
        if (err) throw err;
        res.send({ status: 'success', message: 'Mensagem enviada com sucesso' });
    });
});

app.listen(port, () => {
    console.log(`Servidor rodando na porta ${port}`);
});
