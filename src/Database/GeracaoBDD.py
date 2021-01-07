import sqlite3
conn = sqlite3.connect("src\\Database\\banco.db")
def CriarBanco(conn):
    conn.execute("""
        CREATE TABLE IF NOT EXISTS Funcionarios(
            cpf varchar(11) primary key,
            nome varchar(45),
            cargo varchar(45),
            salario float(2) null,
            terceirizado boolean
        );""")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS residencia(
            idResidencia integer primary key,
            endereco varchar(200),
            tamanhoDoTerreno  float,
            preco float(2) null,
            cpfProprietario varchar(11) null
        );""")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS moradores(
            idMorador integer primary key,
            nomeMorador varchar(45),
            cpfMorador varchar(45),
            idResidencia int,
            
            CONSTRAINT fk_residencia FOREIGN KEY (idResidencia) REFERENCES Residencia (idResidencia)
        );""")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS visitantes(
            cpf varchar(11) primary key,
            nome varchar(45)
        );""")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS registroVisitas(
            idVisita integer primary key,
            placaCarro varchar(7),
            horarioEntrada datetime,
            horarioSaida datetime,
            cpf varchar(11),
            constraint fk_visitante foreign key (cpf) references visitantes (cpf)
        );
        """)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS AreaDeLazer(
            idArea integer primary key,
            descricao varchar(45)
        );
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS registroLazer(
            idRegistro integer primary key,
            horarioEntrada datetime,
            horarioSaida datetime,
            idArea int,
            constraint fk_area foreign key(idArea) references AreaDeLazer(idArea)
        );
    """)
    conn.commit()

CriarBanco(conn)