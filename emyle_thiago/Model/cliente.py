import sqlite3

conn = sqlite3.connect('mobiliario.db')
cursor = conn.cursor()


#Classe Cliente
class Cliente():
    def __init__(self, id_cliente, nome_cliente, cpf, data_nascimento, telefone, email, cep, logradouro, numero, complemento):
        #Criando o objeto cliente e descrevndo os atributos essencias que definem suas caracteristicas
        self.id_cliente = id_cliente
        self.nome_cliente = nome_cliente
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.telefone = telefone 
        self.email = email
        self.logradouro = logradouro
        self.cep = cep
        self.numero = numero
        self.complemento = complemento
        
    #Funções definem as ações, ou seja, o que a classe faz
    def criar_cliente(nome_cliente, cpf, data_nascimento, telefone, email,  cep, logradouro, numero, complemento):
        try:
            cursor.execute("""
            INSERT INTO CLIENTES (nome, cpf, data_nascimento, telefone, email,  cep, logradouro, numero, complemento)
            VALUES (?,?,?,?,?,?,?),
            """), (nome_cliente, cpf, data_nascimento, telefone, email,  cep, logradouro, numero, complemento)

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
                WHERE id = ?
                """, (cpf_cliente,))

                #Salvando no banco de dados
                conn.commit()
                #Fechando a conexão como banco de dados 
                conn.close()
                print("Dados de 'clientes' atualizados")
            except:
                print("erro")
                conn.close()
        

