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
    def selectMoradores():
        listaDePessoas = conn.execute("""SELECT * FROM moradores""")
        return listaDePessoas.fetchall()

    def updateMorador(self, cpf, nome="", idResidencia = ""):
        cursor = conn.cursor()
        morador = [cpf]
        sql = "UPDATE moradores SET cpfMorador = ?,"
        if nome != "":
            sql = sql + "nomeMorador = ?,"
            morador.append(nome)
        if idResidencia != "":
            sql = sql + "idResidencia = ?,"
            morador.append(idResidencia)

        sql = sql[:len(sql)-1]

        sql = sql + " WHERE cpfMorador = ?"
        morador.append(cpf)
        cursor = conn.cursor()
        cursor.execute(sql, morador)
        conn.commit()
    
    @staticmethod
    def deleteMorador(cpf):
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Moradores WHERE cpfMorador = ?",[cpf])
        conn.commit()

    @staticmethod
    def selectMoradorByCpf(cpf):
        Morador = conn.execute("""SELECT * FROM Moradores WHERE cpfMorador = ?""",[cpf])
        return Morador.fetchall()


# morador = Morador("gustavoTerraPreta","12345678901",2)
# morador.insertMorador()
#Morador.deleteMorador("1")
# morador.updateMorador(idMorador=5, nome=nome, cpf=cpf, idResidencia=idResidencia)
#print(Morador.selectPMoradorByCpf("12345678901"))e