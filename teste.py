#coding:utf-8
import sqlite3
conn = sqlite3.connect('Sistema.db')
cursor = conn.cursor()
cursor.execute("""
INSERT INTO InfoBasica (nome, endereco, tel, email)
VALUES ('Regis', 'Rua 535', 00000000000, 'regis@email.com')
""")
conn.commit()

print('Dados inseridos com sucesso.')

conn.close()
