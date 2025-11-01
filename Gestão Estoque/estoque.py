from database import *
import json

def adicionar_produto(nome, qtd):
    conn = conectar()
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO produtos (nome, quantidade) VALUES (?, ?)", (nome, qtd))
        conn.commit()
        print("Produto adicionado!")
    except Exception as e:
        print("Erro ao adicionar produto (possivelmente já existe):", e)
    finally:
        conn.close()


def Criar_Tabela():
    
    Criar_tabela()


def listar_produto():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, quantidade FROM produtos")
    produtos = cursor.fetchall()
    conn.close()

    if not produtos:
        print("Nenhum produto cadastrado.")
    else:
        for p in produtos:
            print(f"{p[0]} - {p[1]}: {p[2]}")

    
    return produtos


def atualizar_estoque(nome, qtd):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT quantidade FROM produtos WHERE nome = ?", (nome,))
    result = cursor.fetchone()

    if not result:
        print("Produto não encontrado!")
        conn.close()
        return

    nova_qtd = result[0] + qtd
    if nova_qtd < 0:
        nova_qtd = 0

    cursor.execute("UPDATE produtos SET quantidade = ? WHERE nome = ?", (nova_qtd, nome))
    conn.commit()
    conn.close()
    print("Estoque atualizado!")


