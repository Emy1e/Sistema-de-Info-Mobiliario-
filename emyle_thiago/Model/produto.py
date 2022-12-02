import sqlite3

conn = sqlite3.connect('mobiliario.db')
cursor = conn.cursor()

#Classe Produto
class Produto():
    def __init__(self, id_produto, nome_produto, categoria, preco, descricao, estoque, ficha_tecnica):
        #Criando o objeto produto e descrevndo os atributos essencias que definem suas caracteristicas
        self.id_produto = id_produto
        self.nome_produto = nome_produto 
        self.categoria = categoria
        self.preco = preco 
        self.descricao = descricao
        self.estoque = estoque 
        self.ficha_tecnica = ficha_tecnica
        
    
    #Funcoes da classe que são definidas aparticar de açoes do produto 
    #Funções definem as ações, ou seja, o que a classe faz
    def criar_cliente(nome_cliente, cpf, data_nascimento, telefone, email,  cep, logradouro, numero, complemento):

        dados = (nome_cliente, cpf, data_nascimento, telefone, email,  cep, logradouro, numero, complemento)
        try:
            cursor.execute("""
            INSERT INTO FORNECEDOR (nome, cpf, telefone, email,  cep, logradouro, numero, complemento)
            VALUES (?,?,?,?,?,?,?),
            """), (dados)

            #Salvando no banco de dados
            conn.commit()
            print("Cliente Inserido!")

        except:
            print("erro")
            conn.close()
    
    
    def buscar_dados_clientes():
    #Busca todos os dados de todos os clientes e exibe no terminal 
        try:
            #Lendo os dados e apresentando na 
            cursor.execute("""
            SELECT * FROM CLIENTES;
            """)

            for linha in cursor.fetchall():
                print(linha)

            #Salvando no banco de dados
            conn.commit()
            #Fechando a conexão como banco de dados 
            conn.close()
            print("Todos os dados de 'clientes' buscados")
        except:
            print("erro")
            conn.close()
    

    def atualizar_dados_clientes(nome, cpf_cliente):
    #Atualiza os dados daquele cliente especificado pelo cpf 
        try:
            cursor.execute("""
            UPDATE PRODUTOS 
            SET NOME = ? 
            WHERE cpf = ?;
            """, (nome, cpf_cliente))

            #Salvando no banco de dados
            conn.commit()
            #Fechando a conexão como banco de dados 
            conn.close()
            print("Dados de 'clientes' atualizados")
        except:
            print("erro")
            conn.close()


    def deletar_clientes(cpf_cliente):
        #Deleta os dados daquele cliente especificado pelo cpf 
            try:
                cursor.execute("""
                DELETE FROM clientes
                WHERE cpf_cliente = ?
                """, (cpf_cliente))

                #Salvando no banco de dados
                conn.commit()
                #Fechando a conexão como banco de dados 
                conn.close()
                print("Dados de 'clientes' atualizados")
            except:
                print("erro")
                conn.close()
        

