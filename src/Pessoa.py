import sqlite3
conn = sqlite3.connect("src\\Database\\banco.db")   

class Pessoa:

    def __init__(self, nome:str, sobrenome:str):
        self.nome = nome
        self.sobrenome = sobrenome
    
    def insertPessoa(self):
        pessoa = [self.nome, self.sobrenome]
        cursor = conn.cursor()
        cursor.execute("INSERT INTO PESSOA (nome, sobrenome) VALUES (?,?)", pessoa)
        conn.commit()

    @staticmethod
    def selectPessoas():
        listaDePessoas = conn.execute("""SELECT idTeste, nome, sobrenome FROM PESSOA""")
        return listaDePessoas.fetchall()