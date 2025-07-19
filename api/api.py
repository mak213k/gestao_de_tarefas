import psycopg2
from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)


hostname = 'localhost'
database = 'postgres'  
username = 'postgres'
pwd = '123456'
port_id = 5432

def get_db_connection():
    return psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=port_id
    )

@app.route('/tarefas', methods=['GET'])
def pegar_tarefa():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT id, nome_tarefa, data_tarefa FROM public.todolist ORDER BY id;')
    tarefas = cur.fetchall()
    cur.close()
    conn.close()

    tarefas_json = [{'id': t[0], 'nome_tarefa': t[1], 'data_tarefa': t[2].strftime('%Y-%m-%d')} for t in tarefas]
    return jsonify(tarefas_json)



@app.route('/tarefas', methods=['POST'])
def criar_tarefa():
    data = request.get_json()

    if 'nome_tarefa' not in data or 'data_tarefa' not in data:
        return jsonify({'error': 'Invalid task properties.'}), 400

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        'INSERT INTO public.todolist (nome_tarefa, data_tarefa) VALUES (%s, %s) RETURNING id;',
        (data['nome_tarefa'], data['data_tarefa'])
    )
    new_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()

    return '', 201, {'Location': f'/tarefas/{new_id}'}


@app.route('/tarefas/<int:id>', methods=['DELETE'])
def deletar_tarefa(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM public.todolist WHERE id = %s;', (id,))
    conn.commit()
    cur.close()
    conn.close()
    return '', 204


if __name__ == '__main__':
    app.run(port=5000, debug=True)

