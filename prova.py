from flask import Flask, render_template,request
from flaskext.mysql import MySQL
from bd import *

app = Flask(__name__)
mysql =MySQL()

mysql.init_app(app)

app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']='root'
app.config['MYSQL_DATABASE_DB']='prova'


@app.route('/')
def inicio ():
    return render_template('first.html')

@app.route('/cadastro', methods=['GET','POST'])
def cadastro():
    if request.method == 'POST':
        url=request.form.get('url')
        codigo=request.form.get('codigo')

        cursor = mysql.get_db().cursor()
        idcadastro = get_idcadastro(cursor, url, codigo)
        if idcadastro is None:
            return render_template('first.html')
        else:
            return render_template('cadastrar.html')
    else:
        return render_template('first.html')



if __name__ == '__main__':
    app.run(debug=True)