from estoque1 import *

def menu():
    Criar_Tabela()  

    while True:
        print("\n===== Controle de Estoque Ninja =====")
        print("1 - Adicionar Produto")
        print("2 - Listar Produtos")
        print("3 - Entrada de Estoque")
        print("4 - Saída de Estoque")
        print("0 - Sair")

        op = input("Escolha: ")

        if op == "1":
            nome = input("Digite o nome do produto: ").strip()
            try:
                qtd = int(input("Quantidade do produto: "))
                adicionar_produto(nome, qtd)
            except ValueError:
                print("Erro: a quantidade deve ser um número inteiro.")

        elif op == "2":
            listar_produto() 

        elif op == "3":
            nome = input("Produto: ").strip()
            try:
                qtd = int(input("Quantidade a adicionar: "))
                atualizar_estoque(nome, qtd)
            except ValueError:
                print("Erro: a quantidade deve ser um número inteiro.")

        elif op == "4":
            nome = input("Produto: ").strip()
            try:
                qtd = int(input("Quantidade a remover: "))
                atualizar_estoque(nome, -qtd)
            except ValueError:
                print("Erro: a quantidade deve ser um número inteiro.")

        elif op == "0":
            print("Saindo... até a próxima!")
            break

        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()
