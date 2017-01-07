from flask import Flask, render_template, redirect, url_for, request

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
@app.route('/form',methods = ['POST', 'GET'])
def form():
   if request.method == 'POST':
      try:
         print 'Eis me aqui'
         nome = request.form['nome']
         dre = request.form['dre']
         curso = request.form['curso']
         telefone = request.form['telefone']
         email=request.form['email']
         endereco=request.form['endereco']
         bairro=request.form['bairro']
         cidade=request.form['cidade']
         datagrad=request.form['datagrad']
         localgrad=request.form['localgrad']
         orientador=request.form['orientador']
         coorientadores=request.form['coorientadores']
         endereco=endereco+", "+bairro+", "+cidade
         with sql.connect("Sistema.db") as con:
            print 'Estou aqui'
            cur = con.cursor()
            cur.execute("INSERT INTO Aluno (DRE, DataGrad, LocalGrad, Orientador, Corientadores) VALUES (?,?,?,?,?)",(dre,datagrad,localgrad,Orientador,coorientadores) )
            cur.execute("INSERT INTO InfoBasica (nome, endereco, tel, email) VALUES (?,?,?,?)",(nome,endereco,tel,email) )
            print 'Estou aqui"

            con.commit()
            print 'Estou aqui'
            msg = "Record successfully added"
      except:
         print 'eis'
         con.rollback()
         msg = "error in insert operation"

      finally:
         return render_template("resultado.html",msg = msg)
         con.close()
app.run()
