from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)
app.secret_key = 'cuidar_secret_key_2026'

DB_CONFIG = {
    'host': '192.168.18.75',
    'user': 'cuidar_user',
    'password': 'cuidar_pass',
    'database': 'hospital_cuidar'
}

def get_connection():
    return mysql.connector.connect(**DB_CONFIG)

# ─── LISTAR ───────────────────────────────────────────────
@app.route('/')
def index():
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM pacientes ORDER BY id DESC")
        pacientes = cursor.fetchall()
        cursor.close()
        conn.close()
    except Error as e:
        flash(f'Erro ao conectar ao banco de dados: {e}', 'error')
        pacientes = []
    return render_template('index.html', pacientes=pacientes)

# ─── CADASTRAR ────────────────────────────────────────────
@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        nome      = request.form['nome'].strip()
        cpf       = request.form['cpf'].strip()
        nascimento = request.form['nascimento']
        unidade   = request.form['unidade']

        if not nome or not cpf or not nascimento or not unidade:
            flash('Todos os campos são obrigatórios.', 'error')
            return render_template('cadastrar.html')

        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO pacientes (nome, cpf, data_nascimento, unidade) VALUES (%s, %s, %s, %s)",
                (nome, cpf, nascimento, unidade)
            )
            conn.commit()
            cursor.close()
            conn.close()
            flash('Paciente cadastrado com sucesso!', 'success')
            return redirect(url_for('index'))
        except Error as e:
            flash(f'Erro ao cadastrar paciente: {e}', 'error')

    return render_template('cadastrar.html')

# ─── EDITAR ───────────────────────────────────────────────
@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        if request.method == 'POST':
            nome       = request.form['nome'].strip()
            cpf        = request.form['cpf'].strip()
            nascimento = request.form['nascimento']
            unidade    = request.form['unidade']

            cursor.execute(
                "UPDATE pacientes SET nome=%s, cpf=%s, data_nascimento=%s, unidade=%s WHERE id=%s",
                (nome, cpf, nascimento, unidade, id)
            )
            conn.commit()
            cursor.close()
            conn.close()
            flash('Paciente atualizado com sucesso!', 'success')
            return redirect(url_for('index'))

        cursor.execute("SELECT * FROM pacientes WHERE id = %s", (id,))
        paciente = cursor.fetchone()
        cursor.close()
        conn.close()

        if not paciente:
            flash('Paciente não encontrado.', 'error')
            return redirect(url_for('index'))

    except Error as e:
        flash(f'Erro: {e}', 'error')
        return redirect(url_for('index'))

    return render_template('editar.html', paciente=paciente)

# ─── DELETAR ──────────────────────────────────────────────
@app.route('/deletar/<int:id>', methods=['POST'])
def deletar(id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM pacientes WHERE id = %s", (id,))
        conn.commit()
        cursor.close()
        conn.close()
        flash('Paciente removido com sucesso.', 'success')
    except Error as e:
        flash(f'Erro ao remover paciente: {e}', 'error')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
