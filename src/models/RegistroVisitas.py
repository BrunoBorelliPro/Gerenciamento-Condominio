import sqlite3
from datetime import datetime
conn = sqlite3.connect("src\\Database\\banco.db")

class RegistroVisitas:
    
    def __init__(self, placaCarro: str, horarioEntrada: datetime, horarioSaida: datetime, cpf: str):
        self.placaCarro = placaCarro
        self.horarioEntrada = horarioEntrada
        self.horarioSaida = horarioSaida
        self.cpf = cpf

    def insertRegistroVisitas(self):
        registro = [self.placaCarro, self.horarioEntrada, self.horarioSaida, self.cpf]
        cursor = conn.cursor()
        cursor.execute("INSERT INTO registroVisitas (placaCarro, horarioEntrada, horarioSaida, cpf) VALUES (?,?,?,?)", registro)
        conn.commit()

    @staticmethod
    def selectRegistroVisitas():
        listaDeRegistros = conn.execute("""SELECT * FROM registroVisitas""")
        return listaDeRegistros.fetchall()
    
    @staticmethod
    def updateRegistroVisitas(idVisita, placaCarro="", horarioEntrada="", horarioSaida="", cpf=""):
        cursor = conn.cursor()
        registro = []
        sql = "UPDATE registroVisitas SET idVisita = ?,"

        if placaCarro != "":
            sql = sql + "placaCarro = ?,"
            registro.append(placaCarro)

        sql = sql[:len(sql)-1]

        sql = sql + " WHERE idVisita = ?"

        registro.append(idVisita)
        cursor = conn.cursor()
        cursor.execute(sql, registro)
        conn.commit()

    @staticmethod
    def deleteRegistroVisitas(idVisita):
        cursor = conn.cursor()
        cursor.execute("DELETE FROM RegistroVisitas WHERE idVisita = ?", [idVisita])
        conn.commit()

    @staticmethod
    def selectRegistrosByCpf(cpf):
        registros = conn.execute("""SELECT * FROM RegistroVisitas WHERE cpf = ?""", [cpf])
        return registros.fetchall()

# horarioEntrada = datetime(2020,1,9,8,0,0,0)
# horarioSaida = datetime(2020,2,20,8,0,0,0)

# registro = RegistroVisitas("ABCD123", horarioEntrada, horarioSaida, "12345678900")
# registro.insertRegistroVisitas()
# registro = RegistroVisitas("ABCD123", horarioEntrada, horarioSaida, "12345678901")
# registro.insertRegistroVisitas()
# registro = RegistroVisitas("ABCD123", horarioEntrada, horarioSaida, "12345678902")
# registro.insertRegistroVisitas()

# print(registro.selectRegistroVisitas())

# idRegistro = input()
# placaCarro = input()
# cpf = input()
# horarioEntrada = datetime(2021,1,9,8,0,0,0)
# horarioSaida = datetime(2021,2,20,8,0,0,0)

# registro.updateRegistroVisitas(idRegistro, placaCarro=placaCarro,horarioEntrada=horarioEntrada, horarioSaida=horarioSaida, cpf=cpf)

# cpf = input()
# print(registro.selectRegistrosByCpf(cpf))

# idRegistro = input()
# registro.deleteRegistroVisitas(idRegistro)