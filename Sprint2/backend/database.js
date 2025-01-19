const mysql = require('mysql');

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

module.exports = db;
