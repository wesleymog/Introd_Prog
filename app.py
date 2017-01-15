#coding:utf-8
from flask import Flask, render_template, redirect, url_for, request, Response
import sqlite3

app = Flask(__name__)
msg=''

@app.route('/login', methods=['GET', 'POST'])
def login():
    erro = None
    if request.method == 'POST':
        if request.form['usuario'] != 'admin' or request.form['senha'] != 'admin':
            erro = 'Sai daqui satanas.'
        else:
            return redirect(url_for('registro'))
    return render_template('login.html', erro=erro)

@app.route("/registro")
def registro():
    return render_template("registro.html")

@app.route("/registroProf")
def registroProf():
    return render_template("registroProf.html")

@app.route("/registroDisc")
def registroDisc():
    return render_template("registroDisc")

@app.route('/ativos')
def ativos():
    conn = sqlite3.connect('Sistema.db')
    cursor = conn.cursor()
    cursor.execute("""Select * from InfoBasica,Aluno  where Aluno.IDGERAL=InfoBasica.id and Ativo=1;""" )
    rows = cursor.fetchall();
    return render_template("Ativo.html", rows=rows)

@app.route("/lista")
def lista():
   conn = sqlite3.connect('Sistema.db')
   conn.row_factory = sqlite3.Row
   cur = conn.cursor()
   cur.execute("Select * from Aluno, InfoBasica where Aluno.IDGERAL=InfoBasica.id;")

   rows = cur.fetchall();
   return render_template("tabela_de_edicao.html", rows=rows)

@app.route('/formAlunos',methods = ['POST', 'GET'])
def formAlunos():
   msg=''
   if request.method == 'POST':
      try:

         nome = request.form['nome']
         dre = request.form['dre']
         curso = request.form['curso']
         tel = request.form['telefone']
         email=request.form['email']
         endereco=request.form['endereco']
         bairro=request.form['bairro']
         cidade=request.form['cidade']
         datagrad=request.form['datagrad']
         localgrad=request.form['localgrad']
         orientador=request.form['orientador']
         coorientadores=request.form['coorientadores']
         endereco=endereco+", "+bairro+", "+cidade
         ingresso=request.form['ingresso']
         coddisc=request.form['coddisc']
         ativo=request.form['ativo']
         
         data=ingresso.split("-")
         datafinal=data[0]+data[1]+data[2]

         conn = sqlite3.connect('Sistema.db')
         cursor = conn.cursor()

         cursor.execute("INSERT INTO InfoBasica (nome, endereco, tel, email) VALUES (?,?,?,?)",(nome,endereco,tel,email) )

         conn.row_factory = sqlite3.Row

         cursor.execute("Select Max(id) from InfoBasica")

         rows = cursor.fetchall();
         for row in rows:
             numero=row
         numeros=numero[0]
         if ativo=='Sim':
             ativo=True
         elif ativo=='Não':
             ativo=False
         cursor.execute("""INSERT INTO Aluno (DRE,Curso, DataGrad, LocalGrad, Orientador, Corientadores, Ingresso,CodDisc, Ativo,IDGERAL)
         VALUES (?,?,?,?,?,?,?,?,?,?)""",(dre,curso,datagrad,localgrad,orientador,coorientadores,datafinal,coddisc,ativo,numeros) )

         conn.commit()

         print('Dados inseridos com sucesso.')

         conn.close()
         msg = "Adicionado com sucesso!"
      except:
         con.rollback()
         msg="Tem algo de errado"
      finally:
         return render_template("resultado.html",msg = msg)
         con.close()

@app.route('/formProfessores',methods = ['POST', 'GET'])
def formProfessores():
   msg=''
   if request.method == 'POST':
      try:

         nome = request.form['nome']
         tel = request.form['telefone']
         email=request.form['email']
         endereco=request.form['endereco']
         bairro=request.form['bairro']
         cidade=request.form['cidade']
         SIAPE=request.form['siape']
         tipo=request.form['tipoprof']
         dreAluno=request.form['dre']
         endereco=endereco+", "+bairro+", "+cidade

         conn = sqlite3.connect('Sistema.db')
         cursor = conn.cursor()

         cursor.execute("INSERT INTO InfoBasica (nome, endereco, tel, email) VALUES (?,?,?,?)",(nome,endereco,tel,email) )

         conn.row_factory = sqlite3.Row

         cursor.execute("Select Max(id) from InfoBasica")

         rows = cursor.fetchall();
         for row in rows:
             numero=row
         numeros=numero[0]
         cursor.execute("""INSERT INTO Professor (IDGERAL, SIAPE, Tipo, CodOrientados)
         VALUES (?,?,?,?)""",(numeros,SIAPE,tipo,dreAluno) )

         conn.commit()

         print('Dados inseridos com sucesso.')

         conn.close()
         msg = "Adicionado com sucesso!"
      except:
         con.rollback()
         msg="Tem algo de errado"
      finally:
         return render_template("resultado.html",msg = msg)
         con.close()

#Rotas de deleção
@app.route("/deletar/<nid>")
def delete(nid):
    print nid
    conn = sqlite3.connect('Sistema.db')
    cursor = conn.cursor()
    cursor.execute("""DELETE FROM Aluno WHERE id=?;""",(nid) )
    cursor.execute("""DELETE FROM InfoBasica WHERE id=?;""",(nid) )
    conn.commit()
    conn.close()
    return render_template("resultado.html")

@app.route("/edit/<nid>")
def editar(nid):
    print nid
    conn = sqlite3.connect('Sistema.db')
    cursor = conn.cursor()
    cursor.execute("""Select * from InfoBasica,Aluno  where Aluno.IDGERAL=? and InfoBasica.id=?;""",(nid, nid) )
    rows = cursor.fetchall();
    print rows
    for row in rows:
        inte=str(row[13])
        o=0
        ano=''
        mes=''
        dia=''
        for i in inte:
            o=o+1
            if o<5:
                ano=ano+i
            elif o<7 and o>4:
                mes=mes+i
            else:
                dia=dia+i
        ingresso=ano+"-"+mes+"-"+dia

    return render_template("editarAluno.html",rows=rows,ingresso=ingresso, nid=nid)

@app.route('/editAlunos',methods = ['POST', 'GET'])
def EditAlunos():
   msg=''
   if request.method == 'POST':
      try:
         nome = request.form['nome']
         dre = request.form['dre']
         curso = request.form['curso']
         tel = request.form['telefone']
         email=request.form['email']
         endereco=request.form['endereco']
         datagrad=request.form['datagrad']
         localgrad=request.form['localgrad']
         orientador=request.form['orientador']
         coorientadores=request.form['coorientadores']
         ingresso=request.form['ingresso']
         coddisc=request.form['coddisc']
         ativo=request.form['ativo']
         nid=request.form['id']
         data=ingresso.split("-")
         datafinal=data[0]+data[1]+data[2]

         conn = sqlite3.connect('Sistema.db')
         cursor = conn.cursor()
         cursor.execute("UPDATE InfoBasica SET nome=?,endereco=?,tel=?, email=? WHERE id=? ;",(nome,endereco,tel,email,nid) )


         print 'olha a treta'
         cursor.execute("""UPDATE Aluno SET DRE=?, DataGrad=?,
         LocalGrad=?,Curso=?, Orientador=?, Corientadores=?, Ingresso=?,CodDisc=?
         WHERE IDGERAL=? ;""",(dre,datagrad,localgrad,curso,orientador,coorientadores,datafinal,coddisc,nid) )
         print 'melhor'
         conn.commit()

         print('Dados Editados com sucesso.')

         conn.close()
         msg = "Editado com sucesso!"
      except:
         con.rollback()
         msg="Tem algo de errado"
      finally:
         return render_template("resultado.html",msg = msg)
         con.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Sobre')
def sobre():
    return render_template('Sobre.html')
#Parte visual do cadastro dos professores

app.debug = True
app.run()
