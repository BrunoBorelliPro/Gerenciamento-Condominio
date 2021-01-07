import sqlite3
conn = sqlite3.connect("src\\Database\\banco.db")   

class Morador:

    def __init__(self, nome:str, cpf:str, idResidencia:int):
        self.nome = nome
        self.cpf = cpf
        self.idResidencia = idResidencia
    
    def insertMorador(self):
        pessoa = [self.nome, self.cpf, self.idResidencia]
        cursor = conn.cursor()
        cursor.execute("INSERT INTO moradores (nomeMorador, cpfMorador, idResidencia) VALUES (?,?,?)", pessoa)
        conn.commit()

    @staticmethod
    def selectMorador():
        listaDePessoas = conn.execute("""SELECT * FROM moradores""")
        return listaDePessoas.fetchall()

    def updateMorador(self, idMorador, nome="", cpf="", idResidencia = ""):
        cursor = conn.cursor()
        morador = []
        sql = "UPDATE moradores SET "
        if nome != "":
            sql = sql + "nomeMorador = ?,"
            morador.append(nome)
        if cpf != "":
            sql = sql + "cpfMorador = ?,"
            morador.append(cpf)
        if idResidencia != "":
            sql = sql + "idResidencia = ?,"
            morador.append(idResidencia)

        sql = sql[:len(sql)-1]

        sql = sql + " WHERE idMorador = ?"

        morador.append(idMorador)
        cursor = conn.cursor()
        cursor.execute(sql, morador)
        conn.commit()
    
    @staticmethod
    def deleteMorador(idMorador):
        cursor = conn.cursor()
        cursor.execute("""DELETE Moradores WHERE idMorador = ?""", idMorador)
        conn.commit()

    @staticmethod
    def selectPMoradorByCpf(cpf):
        Morador = conn.execute("""SELECT * FROM Morador WHERE cpf = ?""",cpf)
        return Morador.fetchall()
morador = Morador("gustavoTerraPreta","12345678901",2)
#morador.insertMorador()

nome = input()
cpf = input()
idResidencia = input()
morador.updateMorador(idMorador=5, nome=nome, cpf=cpf, idResidencia=idResidencia)
