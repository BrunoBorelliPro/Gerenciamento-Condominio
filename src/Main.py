from Pessoa import Pessoa
import sqlite3
conn = sqlite3.connect("src\\Database\\banco.db")

conn.execute("""CREATE TABLE IF NOT EXISTS PESSOA(
    idTeste INTEGER PRIMARY KEY,
    nome varchar(45),
    sobrenome varchar(45)
);""")
pessoa = Pessoa(nome="Bruno", sobrenome="Borelli")
pessoa.insertPessoa()
for pessoa in Pessoa.selectPessoas():
    print(pessoa)
    pass

