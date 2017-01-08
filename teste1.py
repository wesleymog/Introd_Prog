import sqlite3

conn = sqlite3.connect('Sistema.db')
cursor = conn.cursor()

nome='Joao'
endereco='skakska'
tel=0
email="soakoasa"
dre=122121
datagrad="12061998"
localgrad="saosiaiopsa"
Orientador="ksakaklala"
coorientadores="ksjjassa sajsja"
cursor.execute("INSERT INTO Aluno (DRE, DataGrad, LocalGrad, Orientador, Corientadores) VALUES (?,?,?,?,?)",(dre,datagrad,localgrad,Orientador,coorientadores) )
cursor.execute("INSERT INTO InfoBasica (nome, endereco, tel, email) VALUES (?,?,?,?)",(nome,endereco,tel,email) )

conn.commit()

print('Dados inseridos com sucesso.')

conn.close()
