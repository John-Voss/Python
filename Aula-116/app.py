from flask import Flask, render_template

# criando um objeto da classe flask
app = Flask(__name__)

@app.route('/')
def firstFlask():
    return 'Meu primeiro programa flask'

@app.route('/flask2')
def secondFlask():
    return 'Segundo flask'

@app.route('/flask3', methods = ['POST'])
def thirdFlask():
    return 'Terceiro flask'

@app.route('/index')
def firstWebPage():
    name = 'flask'
    student_name = 'João Vitor'
    return render_template('index.html', index_variable = name, student_name = student_name)


app.run(debug = True)