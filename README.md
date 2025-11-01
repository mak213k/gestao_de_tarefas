Sistema de Gestão de Estoque Ninja

Um sistema simples e funcional de controle de estoque desenvolvido em Python, com integração a banco de dados SQLite e suporte para exportação dos dados em CSV, JSON e Parquet.
O projeto foi criado com o objetivo de facilitar o gerenciamento de produtos, permitindo adições, listagens e movimentações de entrada e saída de estoque.

🚀 Funcionalidades

✅ Criar automaticamente a tabela do banco de dados (SQLite)
✅ Adicionar novos produtos ao estoque
✅ Listar todos os produtos cadastrados
✅ Atualizar o estoque (entrada e saída de produtos)
✅ Exportar dados para os formatos .csv, .json e .parquet
✅ Interface interativa via terminal

🧩 Estrutura do Projeto
/Gestão Estoque/
├── estoque1.py          # Módulo com as funções principais (CRUD)
├── main.py              # Menu principal do sistema
├── estoque.db           # Banco de dados SQLite
├── produtos.csv         # Exportação em CSV
├── produtos.json        # Exportação em JSON
├── produtos.parquet     # Exportação em Parquet
└── __pycache__/         # Arquivos compilados do Python

🐍 Tecnologias Utilizadas

Python 3.13+

SQLite (nativo do Python)

Pandas — para manipulação e exportação de dados

OS / Sys — para interação com o terminal
