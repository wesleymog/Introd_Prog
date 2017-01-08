from flask import Flask, render_template, redirect, url_for, request, Response
import sqlite3

app = Flask(__name__)
msg=''
login_manager = LoginManager()
login_manager.init_app(app)

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
@app.route('/form',methods = ['POST', 'GET'])
def form():
   if request.method == 'POST':
      try:
         print 'Eis me aqui'
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
         conn = sqlite3.connect('Sistema.db')
         print 'oi'
         cursor = conn.cursor()
         print 'aqiu'
         cursor.execute("""INSERT INTO Aluno (DRE, DataGrad, LocalGrad, Orientador, Corientadores)
         VALUES (?,?,?,?,?)""",(dre,datagrad,localgrad,orientador,coorientadores) )
         print "ja foi uma"
         cursor.execute("INSERT INTO InfoBasica (nome, endereco, tel, email) VALUES (?,?,?,?)",(nome,endereco,tel,email) )
         print 'esperA'
         conn.commit()

         print('Dados inseridos com sucesso.')

         conn.close()
         print 'deu bom'
         msg = "Adicionado com sucesso!"
      except:
         con.rollback()
         msg="Tem algo de errado"
      finally:
         return render_template("resultado.html",msg = msg)
         con.close()
app.run()
