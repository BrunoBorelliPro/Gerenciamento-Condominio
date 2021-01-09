import sqlite3
conn = sqlite3.connect("src\\Database\\banco.db")   

class AreaDeLazer:

    def __init__(self, descricao:str):
        self.descricao = descricao
    
    def insertAreaDeLazer(self):
        area = [self.descricao]
        cursor = conn.cursor()
        cursor.execute("INSERT INTO AreaDeLazer (descricao) VALUES (?)", area)
        conn.commit()

    @staticmethod
    def selectAreaDeLazer():
        listaDeArea = conn.execute("""SELECT * FROM AreaDeLazer""")
        return listaDeArea.fetchall()
    
    @staticmethod
    def updateAreaDeLazer(idArea, descricao = ""):
        cursor = conn.cursor()
        area = []
        sql = "UPDATE AreaDeLazer SET "
        if descricao != "":
            sql = sql + "descricao = ?,"
            area.append(descricao)
        if idArea != "":
            sql = sql + "idArea = ?,"
            area.append(idArea)

        sql = sql[:len(sql)-1]

        sql = sql + " WHERE idArea = ?"

        area.append(idArea)
        cursor = conn.cursor()
        cursor.execute(sql, area)
        conn.commit()
    
    @staticmethod
    def deleteAreaDeLazer(idArea):
        cursor = conn.cursor()
        cursor.execute("""DELETE FROM AreaDeLazer WHERE idArea = ?""", [idArea])
        conn.commit()

    @staticmethod
    def selectAreaByDescricao(descricao):
        AreaDeLazer = conn.execute("""SELECT * FROM AreaDeLazer WHERE descricao LIKE ?""", ["%"+descricao+"%"])
        return AreaDeLazer.fetchall()

# area = AreaDeLazer("Academia pro bruno malhar os biceps")
# # area.insertAreaDeLazer()

# print(area.selectAreaDeLazer())

# idArea = input()
# descricao = input()
# area.updateAreaDeLazer(idArea, descricao)
# descricao = input()
# print(area.selectPAreaByDescricao(descricao))

# idArea = input()
# area.deleteAreaDeLazer(idArea)
