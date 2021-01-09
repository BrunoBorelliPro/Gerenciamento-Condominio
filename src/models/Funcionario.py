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
    def selectFuncionario():
        listaDeFuncionario = conn.execute("""SELECT cpf, nome, cargo, salario, terceirizado FROM Funcionarios""")
        return listaDeFuncionario.fetchall()
    
    @staticmethod
    def updateFuncionario(cpf, nome="",cargo="",terceirizado="",salario=""):

        cursor = conn.cursor()
        funcionario = [cpf]
        sql = "UPDATE funcionarios SET cpf = ?,"
        if nome != "":
            sql = sql + "nome = ?,"
            funcionario.append(nome)
        if cargo != "":
            sql = sql + "cargo = ?,"
            funcionario.append(cargo)
        if terceirizado != "":
            sql = sql + "terceirizado = ?,"
            funcionario.append(terceirizado)
        if salario != "":
            sql = sql + "salario = ?,"
            funcionario.append(salario)
        sql = sql[:len(sql)-1]

        sql = sql + " WHERE cpf = ?"

        funcionario.append(cpf)
        cursor = conn.cursor()
        cursor.execute(sql, funcionario)
        conn.commit()

    @staticmethod
    def deleteFuncionario(cpf):
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Funcionarios WHERE cpf = ?",[cpf])
        conn.commit()

    @staticmethod
    def selectFuncionarioByCpf(cpf):
        funcionario = conn.execute("""SELECT cpf, nome, cargo, salario, terceirizado FROM Funcionarios WHERE cpf = ?""",[cpf])
        return funcionario.fetchall()




# funcionario = Funcionario("12345678908", "bruno", "programador",False, 1000)
# funcionario.insertFuncionario()
# print(Funcionario.selectPFuncionario())
# funcionario.updateFuncionario("12345678901","gustavo")
# Funcionario.deleteFuncionario("12345678902")
