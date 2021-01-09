import sqlite3
conn = sqlite3.connect("src\\Database\\banco.db")   

class Visitantes:

    def __init__(self, nome:str, cpf:str):
        self.nome = nome
        self.cpf = cpf
    
    def insertVisitantes(self):
        visitante = [self.nome, self.cpf]
        cursor = conn.cursor()
        cursor.execute("INSERT INTO visitantes (nome, cpf) VALUES (?,?)", visitante)
        conn.commit()

    @staticmethod
    def selectVisitantes():
        listaDevisitantes = conn.execute("""SELECT * FROM visitantes""")
        return listaDevisitantes.fetchall()

    @staticmethod
    def updateVisitantes(cpf, nome=""):
        cursor = conn.cursor()
        visitante = [cpf]
        sql = "UPDATE visitantes SET cpf = ?,"
        if nome != "":
            sql = sql + "nome = ?,"
            visitante.append(nome)

        sql = sql[:len(sql)-1]

        sql = sql + " WHERE cpf = ?"

        visitante.append(cpf)
        cursor = conn.cursor()
        cursor.execute(sql, visitante)
        conn.commit()
    
    @staticmethod
    def deleteVisitantes(cpf):
        cursor = conn.cursor()
        cursor.execute("DELETE FROM visitantes WHERE cpf = ?",[cpf])
        conn.commit()

    @staticmethod
    def selectVisitantesByCpf(cpf):
        Morador = conn.execute("""SELECT * FROM visitantes WHERE cpf = ?""",[cpf])
        return Morador.fetchall()


# visitante = Visitantes("gustavoTerraPreta","12345678903")
#visitante.insertVisitantes()
#visitante.deleteVisitantes("12345678902")
#visitante.updateVisitantes("12345678901","bruno")
#print(visitante.selectVisitantesByCpf("12345678901"))