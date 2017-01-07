#coding:utf-8
import sqlite3
conn = sqlite3.connect('Sistema.db')
nome="Joao"
endereco="Queimaods"
tel=21987974217
email="aksksa"
DRE=12212131
datagrad=1998061998
localgrad="Joao"
Orientador="jajaj"
coorientadores='kaasks sakjkjsakas sakjksajkas nksaksajksa'

conn.execute("INSERT INTO InfoBasica (nome, endereco, tel, email) VALUES (?,?,?,?)",(nome,endereco,tel,email) )
print 'deu bom'

conn.execute("INSERT INTO Aluno (DRE, DataGrad, LocalGrad, Orientador, Corientadores) VALUES (?,?,?,?,?)",(DRE,datagrad,localgrad,Orientador,coorientadores) )
print 'deu mais bom'
conn.close()
