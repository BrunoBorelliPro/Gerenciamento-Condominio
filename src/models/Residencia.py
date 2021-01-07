import sqlite3
conn = sqlite3.connect("src\\Database\\banco.db")   

class Residencia:

    def __init__(self, endereco:str, tamanhoDoTerreno:str, cpfProprietario:str, preco:float=0):
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

    def updateResidencia(self):
        funcionario = [self.endereco, self.tamanhoDoTerreno, self.preco, self.cpfProprietario, idResidencia]
        cursor = conn.cursor()
        cursor.execute("""UPDATE Residencia SET endereco = ?, tamanhoDoTerreno = ?, preco = ?, cpfProprietario = ? WHERE idResidencia = ?""", idResidencia)
        conn.commit()

    @staticmethod
    def deleteResidencia(idResidencia):
        cursor = conn.cursor()
        cursor.execute("""DELETE Residencia WHERE idResidencia = ?""", idResidencia)
        conn.commit()

    @staticmethod
    def selectResidenciaByIdReferencia(idResidencia):
        funcionario = conn.execute("""SELECT endereco, tamanhoDoTerreno, preco, cpfProprietario, FROM Residencia WHERE idResidencia = ?""",idResidencia)
        return funcionario.fetchall()