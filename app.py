#coding:utf-8
from flask import Flask, render_template, redirect, url_for, request, Response
import sqlite3
from datetime import date

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
@app.route('/consulta')
def consulta():
    hj = date.today()
    lista=str(hj).split("-")
    data=lista[0]+lista[1]+lista[2]
    print data
    conn = sqlite3.connect('Sistema.db')
    cursor = conn.cursor()
    cursor.execute("""Select * from InfoBasica,Aluno  where Aluno.IDGERAL=InfoBasica.id and (Aluno.ingresso+30000)<? ;""",(data,) )
    rows = cursor.fetchall();
    print rows
    return render_template("Consulta.html",rows=rows)
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
   msg='Há algo de errado, tente novamente'
   if request.method == 'POST':
      try:
         print 'oi'
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
         print 'oi'
         ativo=request.form['ativo']
         bolsa=request.form['bolsa']
         pagbolsa=request.form['pagbolsa']
         iniciobolsa=request.form['iniciobolsa']
         duracaobolsa=request.form['duracaobolsa']
         vquali=request.form['VQualificacao']
         dataquali=request.form['dataquali']
         paper=request.form['paper']
         datapub=request.form['datapub']
         ondepub=request.form['ondepub']
         datamest=request.form['datamest']
         localmest=request.form['localmest']
         mestrado=datamest+","+localmest
         if datamest=='' or localmest=='':
             mestrado=None
             print mestrado

         print bolsa
         print 'caralho'+paper
         print vquali
         if bolsa=='sim':
             bolsaFinal=pagbolsa+','+duracaobolsa
             print bolsaFinal
         elif bolsa=='nao':
             bolsaFinal=None
         if paper=='Sim':
             paperFinal=datapub+","+ondepub
             print paperFinal
         elif paper=='Nao':
             paperFinal=None
             print paperFinal
             print 4
         if vquali=='Sim':
             qualificacao=dataquali
             print qualificacao
         elif vquali=='Nao':
             qualificacao=None
             print qualificacao
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
         elif ativo=='Nao':
             ativo=False
         cursor.execute("""INSERT INTO Aluno (DRE,Curso, DataGrad, LocalGrad, Orientador, Corientadores, Ingresso,Qualificacao,CodDisc,Bolsa, Ativo,Paper,Mestrado,IDGERAL)
         VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",(dre,curso,datagrad,localgrad,orientador,coorientadores,datafinal,qualificacao,coddisc,bolsaFinal,ativo,paperFinal,mestrado,numeros) )

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
    try:
        conn = sqlite3.connect('Sistema.db')
        cursor = conn.cursor()
        cursor.execute("""DELETE FROM Aluno WHERE IDGERAL=?;""",(nid, ) )
        cursor.execute("""DELETE FROM InfoBasica WHERE id=?;""",(nid, ) )
        conn.commit()
        msg='Deletado com sucesso!'
    except:
       con.rollback()
       msg="Tem algo de errado"
    finally:
       return render_template("resultado.html",msg = msg)
       con.close()

@app.route("/edit/<nid>")
def editar(nid):
    print nid
    conn = sqlite3.connect('Sistema.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("""Select * from InfoBasica,Aluno  where Aluno.IDGERAL=? and InfoBasica.id=?;""",(nid, nid) )
    rows = cursor.fetchall();
    print rows
    for row in rows:
        bolsa=str(row['Bolsa'])
        bolsa=bolsa.split(',')
        mestrado=str(row['Mestrado'])
        mestrado=mestrado.split(',')
        paper=str(row['Paper'])
        paper=paper.split(',')
        print paper
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
        ingressofinal=''

    return render_template("editarAluno.html",rows=rows,ingresso=ingresso, nid=nid,bolsa=bolsa, mestrado=mestrado, paper=paper)

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
         bolsa=request.form['bolsa']
         pagbolsa=request.form['pagbolsa']
         duracaobolsa=request.form['duracaobolsa']
         vquali=request.form['VQualificacao']
         dataquali=request.form['dataquali']
         paper=request.form['paper']
         datapub=request.form['datapub']
         ondepub=request.form['ondepub']
         datamest=request.form['datamest']
         localmest=request.form['localmest']
         mestrado=datamest+","+localmest
         if datamest=='' or localmest=='':
             mestrado=None
         if bolsa=='Sim':
             bolsaFinal=pagbolsa+','+duracaobolsa
         elif bolsa=='nao':
             bolsaFinal=None
         print 'oi'
         if paper=='Sim':
             paperFinal=datapub+","+ondepub
             print paperFinal
         elif paper=='nao':
             paperFinal=None
             print paperFinal
         if vquali=='Sim':
             qualificacao=dataquali
             print qualificacao
         elif vquali=='nao':
             qualificacao=None
             print qualificacao
         nid=request.form['id']
         data=ingresso.split("-")
         datafinal=data[0]+data[1]+data[2]
         conn = sqlite3.connect('Sistema.db')
         cursor = conn.cursor()
         cursor.execute("UPDATE InfoBasica SET nome=?,endereco=?,tel=?, email=? WHERE id=? ;",(nome,endereco,tel,email,nid) )
         cursor.execute("""UPDATE Aluno SET DRE=?, DataGrad=?,
         LocalGrad=?,Curso=?, Orientador=?, Corientadores=?, Ingresso=?,CodDisc=?,Bolsa=?,Ativo=?,Paper=?, Mestrado=?
         WHERE IDGERAL=? ;""",(dre,datagrad,localgrad,curso,orientador,coorientadores,datafinal,coddisc,bolsaFinal,ativo,paperFinal,mestrado,nid) )
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
@app.route('/pesquisa')
def pesquisa():
    return render_template('Pesquisa.html')
@app.route('/disciplina')
def disciplina():
    return render_template('registroDisc.html')
@app.route('/cadastroDisc')
def cadastroDisc():
    return render_template("resultado.html")
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Sobre')
def sobre():
    return render_template('Sobre.html')
#Parte visual do cadastro dos professores

app.debug = True
app.run()
