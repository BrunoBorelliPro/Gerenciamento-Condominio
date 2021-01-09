import sqlite3
from datetime import datetime
conn = sqlite3.connect("src\\Database\\banco.db")   

class RegistroLazer:

    def __init__(self,horarioEntrada:datetime.time, horarioSaida:datetime.time, idArea):
        self.horarioEntrada = horarioEntrada
        self.horarioSaida = horarioSaida
        self.idArea = idArea
   
    def insertRegistro(self):
        registro = [self.horarioEntrada, self.horarioSaida, self.idArea]
        cursor = conn.cursor()
        cursor.execute("INSERT INTO registroLazer (horarioEntrada, horarioSaida, idArea) VALUES (?,?,?)", registro)
        conn.commit()

    @staticmethod
    def selectRegistro():
        listaDeFuncionario = conn.execute("""SELECT idRegistro, horarioEntrada, horarioSaida, idArea FROM registroLazer""")
        return listaDeFuncionario.fetchall()
    
    @staticmethod
    def updateRegistro(idRegistro, horarioEntrada="", horarioSaida="", idArea=""):

        cursor = conn.cursor()
        registro = [idRegistro]
        sql = "UPDATE registroLazer SET idRegistro = ?,"
        if horarioEntrada != "":
            sql = sql + "horarioEntrada = ?,"
            registro.append(horarioEntrada)
        if horarioSaida != "":
            sql = sql + "horarioSaida = ?,"
            registro.append(horarioSaida)
        if idArea != "":
            sql = sql + "idArea = ?,"
            registro.append(idArea)

        sql = sql[:len(sql)-1]

        sql = sql + " WHERE idRegistro = ?"

        registro.append(idRegistro)
        cursor = conn.cursor()
        cursor.execute(sql, registro)
        conn.commit()

    @staticmethod
    def deleteRegistro(idRegistro):
        cursor = conn.cursor()
        cursor.execute("DELETE FROM registroLazer WHERE idRegistro = ?",[idRegistro])
        conn.commit()

    @staticmethod
    def selectRegistroById(idRegistro):
        funcionario = conn.execute("""SELECT idRegistro, horarioEntrada, horarioSaida, idArea FROM registroLazer WHERE idRegistro = ?""",[idRegistro])
        return funcionario.fetchall()

# entrada = datetime(2020,1,9,8,0,0,0)
# saida = datetime(2020,1,9,9,0,0,0)
# registoLazer = RegistoLazer(entrada,saida,1)
#print(RegistoLazer.selectRegistro())
#print(RegistoLazer.selectRegistroById(1))
#registoLazer.updateRegistro(1,saida)
#registoLazer.deleteRegistro(2)
