import sqlite3
conn = sqlite3.connect("src\\Database\\banco.db")   

class Funcionario:

    def __init__(self, cpf:str, nome:str, cargo:str, terceirizado:bool, salario=None):
        self.cpf = cpf
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
        self.terceirizado = terceirizado
    def insertFuncionario(self):
        pessoa = [self.cpf, self.nome, self.cargo, self.salario, self.terceirizado]
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Funcionarios (cpf, nome, cargo, salario, terceirizado) VALUES (?,?,?,?,?)", pessoa)
        conn.commit()

    @staticmethod
    def selectPFuncionario():
        listaDeFuncionario = conn.execute("""SELECT cpf, nome, cargo, salario, terceirizado FROM Funcionarios""")
        return listaDeFuncionario.fetchall()
    
    def updateFuncionario(self):
        funcionario = [self.cpf, self.nome, self.cargo, self.salario, self.terceirizado, self.cpf]
        cursor = conn.cursor()
        cursor.execute("""UPDATE Funcionarios SET cpf = ?, nome = ?, cargo = ?, salario = ?, terceirizado = ? WHERE cpf = ?""", funcionario)
        conn.commit()

    @staticmethod
    def deleteFuncionario(cpf):
        cursor = conn.cursor()
        cursor.execute("""DELETE Funcionarios WHERE cpf = ?""", cpf)
        conn.commit()

    @staticmethod
    def selectPFuncionarioByCpf(cpf):
        funcionario = conn.execute("""SELECT cpf, nome, cargo, salario, terceirizado FROM Funcionarios WHERE cpf = ?""",cpf)
        return funcionario.fetchall()


funcionario = Funcionario("12345678901", "bruno", "programador",True)
funcionario.insertFuncionario()
#Funcionario.updateFuncionario("12345678901")
