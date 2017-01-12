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
@app.route("/registroDisc")
def registroDisc():
    return render_template("registroDisc")
@app.route("/lista")
def lista():
   conn = sqlite3.connect('Sistema.db')
   conn.row_factory = sqlite3.Row
   cur = conn.cursor()
   cur.execute("Select * from Aluno, InfoBasica where Aluno.id=InfoBasica.id;")

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
         data=ingresso.split("-")
         datafinal=data[0]+data[1]+data[2]

         conn = sqlite3.connect('Sistema.db')
         cursor = conn.cursor()
         cursor.execute("""INSERT INTO Aluno (DRE, DataGrad, LocalGrad, Orientador, Corientadores, Ingresso,CodDisc)
         VALUES (?,?,?,?,?,?,?)""",(dre,datagrad,localgrad,orientador,coorientadores,datafinal,coddisc) )
         cursor.execute("INSERT INTO InfoBasica (nome, endereco, tel, email) VALUES (?,?,?,?)",(nome,endereco,tel,email) )
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
@app.route('/cadastroprof')
def cadastroprof():
    return render_template('cadastroprof.html')
@app.route('/formProfessores',methods = ['POST', 'GET'])
def formProfessores():
   msg=''
   if request.method == 'POST':
      try:

         nome = request.form['nome']
         endereco=request.form['endereco']
         bairro=request.form['bairro']
         cidade=request.form['cidade']
         endereco=endereco+", "+bairro+", "+cidade
         tipoprof=tipoprof.form["tipoprof"]
         conn = sqlite3.connect('Sistema.db')
         cursor = conn.cursor()
         ##colocar execute
         conn.commit()

         print('Dados inseridos com sucesso.')

         conn.close()
         msg = "Adicionado com sucesso!"
      except:
         con.rollback()
         msg="ERRO"
      finally:
         return render_template("resultado.html",msg = msg)
         con.close()
app.debug = True
app.run()
