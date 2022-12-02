#Importando o banco de dados para utiliza-lo
import sqlite3

#Conectando com banco de dados 
conn = sqlite3.connect('mobiliario.db')

# definindo um cursor, ou seja, um interador que permite navegar e manipular os registros do bd
cursor = conn.cursor()

# criando a tabela
#O comando execute lê e executa comandos SQL puro diretamente no bd.
cursor.execute("""
CREATE TABLE IF NO EXISTS CLIENTES (
        id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_cliente VARCHAR(120) NOT NULL,
        cpf VARCHAR(15) NOT NULL,
        data_nascimento DATE NOT NULL, 
        email VARCHAR(100) NOT NULL,
        telefone VARCHAR(20) NOT NULL,
        logradouro TEXT NOT NULL,
        cep VARCHAR(9) NOT NULL,
        numero INTEGER NOT NULL,
        complemento VARCHAR(50)
);
""")

cursor.execute("""
CREATE TABLE IF NO EXISTS FORNECEDORES (
        id_fornecedor INTEGER PRIMARY KEY AUTOINCREMENT, 
        nome_fornecedor TEXT NOT NULL,
        cnpj_fornecedor VARCHAR(15) NOT NULL, 
        email VARCHAR(100) NOT NULL,
        telefone VARCHAR(20) NOT NULL,
        cep VARCHAR(9) NOT NULL,
        logradouro TEXT NOT NULL,
        numero INTEGER NOT NULL,
        complemento VARCHAR(50)
);
""")

cursor.execute("""
CREATE TABLE IF NO EXISTS PRODUTOS (
        id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_produto VARCHAR(25) NOT NULL,
        categoria TEXT NOT NULL,
        preco FLOAT NOT NULL,
        descricao TEXT NOT NULL, 
        estoque INTEGER NOT NULL, 
        ficha_tecnica TEXT NOT NULL
);
"""
)

cursor.execute("""
CREATE TABLE IF NOT EXISTS PEDIDO(
        id_pedido INTEGER PRIMARY KEY AUTOINCREMENT,
        valor_total FLOAT NOT NULL, 
        qtde_produto INTEGER, 
        status BOOLEAN
        id pagamento 
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS PAGAMENTO(
        id_pagamento INTEGER PRIMARY KEY AUTOINCREMENT,
)
""")


# #Inserindo dados na tabela CLIENTES
# cursor.execute("""
# INSERT INTO CLIENTES (nome, cpf, data_nascimento , email, telefone, cep, logradouro, numero, complemento)
# VALUES ('Reginaldo Andrade', '65487659808', 'regiandrade@email.com', '(11)98765-4321', '12987963', 'Rua Fangundes Romario', 98, 'B'),
#        ('Aldo Rodrigues de Souza', '12345678990', 'aldo09@hotmail.com', '(11)96584-4875', '12957423', 'Rua Borges de Souza', 120),
#        ('Reginaldo Andrade', '65487659808', 'regiandrade@email.com', '(11)97547-6584', '12975470', 'Rua Bruno Menezes', 478),
# """)
# #Salvando no banco de dados
# conn.commit()

# #Inserindo alguns dados na tabela FORNECEDORES
# cursor.execute("""
# INSERT INTO FORNECEDORES (nome_fornecedor, cnpj_fornecedor, email, telefone, cep, logradouro,  numero, complemento)
# VALUES ('Consul', '50987564/0001-23', 'consul@gmail.com', '(11)987564744','18754782', 'Rua das Industrias', 42),
#        ('Eletrolux', '85123654/0001-57', 'eletrolux.moveis@gmail.com', '(11)987564744','12315487', 'Rua Cadantuva', 987),
#        ('Consul', '68654875/0001-65', 'consul@gmail.com', '(11)987564744','12978757', 'Rua Amora', 4312, 'Bloco C' ),
# """)

# #Salvando no banco de dados
# conn.commit()

# #Inserindo alguns dados na tabela PRODUTOS
# cursor.execute("""
# INSERT INTO PRODUTOS (nome_produto, categoria, preco, descricao, estoque, ficha_tecnica, status)
# VALUES ('Geladeira Gelosuper', 'Eletrodomesticos', 11999.99, '', '', 'ativo'),
#        ('Geladeira Gelosuper', 'Eletrodomesticos', 11999.99, '', '', 'ativo'),
#        ('Geladeira Gelosuper', 'Eletrodomesticos', 11999.99, '', '', 'ativo'),
# """)

# #Salvando no banco de dados
# conn.commit()
# #Fechando o banco após as modificações
# conn.close()