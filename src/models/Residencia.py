import sqlite3
conn = sqlite3.connect("src\\Database\\banco.db")   

class Residencia:

    def __init__(self, endereco:str, tamanhoDoTerreno:str, cpfProprietario:str="", preco:float=0):
        self.endereco = endereco
        self.tamanhoDoTerreno = tamanhoDoTerreno
        self.preco = preco
        self.cpfProprietario = cpfProprietario
    
    def insertResidencia(self):
        residencia = [self.endereco, self.tamanhoDoTerreno, self.preco, self.cpfProprietario]
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Residencia (endereco, tamanhoDoTerreno, preco, cpfProprietario) VALUES (?,?,?,?)", residencia)
        conn.commit()

    @staticmethod
    def selectResidencias():
        listaDeResidencias = conn.execute("""SELECT * FROM Residencia""")
        return listaDeResidencias.fetchall()

    @staticmethod
    def updateResidencia(idResidencia, endereco="", tamanhoDoTerreno="", preco = "", cpfProprietario=""):
        cursor = conn.cursor()
        residencia = []
        sql = "UPDATE Residencia SET idResidencia = ?,"
        if endereco != "":
            sql = sql + "endereco = ?,"
            residencia.append(endereco)
        if tamanhoDoTerreno != "":
            sql = sql + "tamanhoDoTerreno = ?,"
            residencia.append(tamanhoDoTerreno)
        if preco != "":
            sql = sql + "preco = ?,"
            residencia.append(preco)
        if cpfProprietario != "":
            sql = sql + "cpfProprietario = ?,"
            residencia.append(cpfProprietario)

        sql = sql[:len(sql)-1]
        sql = sql + "WHERE idResidencia = ?"
        residencia.append(idResidencia)
        cursor = conn.cursor()
        cursor.execute(sql, residencia)
        conn.commit()

    @staticmethod
    def deleteResidencia(idResidencia):
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Residencia WHERE idResidencia = ?", [idResidencia])
        conn.commit()

    @staticmethod
    def selectResidenciaByIdResidencia(idResidencia):
        funcionario = conn.execute("""SELECT idResidencia, endereco, tamanhoDoTerreno, preco, cpfProprietario FROM residencia WHERE idResidencia = ?""",[idResidencia])
        return funcionario.fetchall()



# residencia = Residencia(endereco="Rua Lírio", preco=12.0, tamanhoDoTerreno=25.00, cpfProprietario="12345678901")
# residencia.insertResidencia()
# residencia.updateResidencia(3, endereco="Rua Atualizada")
# Residencia.deleteResidencia(1)
# print(Residencia.selectResidenciaByIdReferencia(3))
# print("=-=-=-=-=-=-=-=-=-=-=-")
# print(Residencia.selectResidencias())

