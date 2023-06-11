from flask import Flask, render_template, request, redirect

app = Flask(__name__)

teams = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/times')
def listar_times():
    return render_template('times.html', times=teams)

@app.route('/cadastro-times', methods=['GET', 'POST'])
def cadastrar_time():
    if request.method == 'POST':
        nome = request.form['nome']
        cidade = request.form['cidade']
        estado = request.form['estado']
        novo_time = {"id": len(teams) + 1, "nome": nome, "cidade": cidade, "estado": estado}
        teams.append(novo_time)
        return redirect('/times')
    return render_template('cadastro_times.html')

@app.route('/ver-time/<int:id>')
def ver_time(id):
    time = next((time for time in teams if time['id'] == id), None)
    if time:
        return render_template('ver_time.html', time=time)
    else:
        return "Time não encontrado."

@app.route('/editar-time/<int:id>', methods=['GET', 'POST'])
def editar_time(id):
    time = next((time for time in teams if time['id'] == id), None)
    if request.method == 'POST':
        if time:
            time['nome'] = request.form['nome']
            time['cidade'] = request.form['cidade']
            time['estado'] = request.form['estado']
            return redirect('/times')
        else:
            return "Time não encontrado."
    return render_template('editar_time.html', time=time)

@app.route('/excluir-time/<int:id>', methods=['POST'])
def excluir_time(id):
    time = next((time for time in teams if time['id'] == id), None)
    if time:
        teams.remove(time)
        return redirect('/times')
    else:
        return "Time não encontrado."
    
if __name__ == '__main__':
    app.run(debug=True)
