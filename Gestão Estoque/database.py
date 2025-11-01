import sqlite3

DB_NAME = "estoque.db"

def conectar():
    return sqlite3.connect(DB_NAME)

def Criar_tabela():  
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT UNIQUE NOT NULL,
            quantidade INTEGER NOT NULL  -- ✅ Corrigido "INTERGER" para "INTEGER"
        );
    """)
    conn.commit()
    conn.close()
