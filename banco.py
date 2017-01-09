import sqlite3

# conectando...
conn = sqlite3.connect('Sistema.db')
# definindo um cursor
cursor = conn.cursor()

# criando a tabela (schema)
cursor.execute("""
CREATE TABLE InfoBasica (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR,
        endereco VARCHAR,
        tel INTEGER,
        email VARCHAR
);
""")

print('Tabela criada com sucesso.')

cursor.execute("""
CREATE TABLE Aluno (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        DRE INTEGER,
        DataGrad VARCHAR,
        LocalGrad VARCHAR,
        Mestrado VARCHAR,
        Orientador VARCHAR,
        Corientadores VARCHAR,
        Ingresso date,
        Qualificacao VARCHAR,
        CodDisc INTEGER,
        Bolsa VARCHAR,
        Ativo BOOLEAN,
        Paper VARCHAR
);
""")

print('Tabela criada com sucesso.')

cursor.execute("""
CREATE TABLE Professor (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        SIAPE INTEGER,
        Tipo VARCHAR,
        CodOrientados VARCHAR
        );
""")

print('Tabela criada com sucesso.')

# desconectando...
conn.close()
