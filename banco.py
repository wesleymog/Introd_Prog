import sqlite3

conn = sqlite3.connect('Sistema.db')
print "Opened database successfully"

conn.execute('CREATE TABLE InfoBasica (id INTEGER AUTO_INCREMENT,nome VARCHAR, endereco VARCHAR, tel INTEGER, email VARCHAR)')
print "Table created successfully"

conn.execute('CREATE TABLE Professor (id INTEGER AUTO_INCREMENT,SIAPE INTEGER,Tipo VARCHAR, CodOrientados VARCHAR)')
print "Table created successfully"

conn.execute('CREATE TABLE Aluno (id INTEGER AUTO_INCREMENT, DRE INTEGER, Graduacao VARCHAR, Mestrado VARCHAR, Orientador VARCHAR,Corientadores VARCHAR, Ingresso VARCHAR,Qualificacao VARCHAR, CodDisc INTEGER, Bolsa VARCHAR, Ativo BOOLEAN, Paper VARCHAR)')
print "Table created successfully"

conn.close()
