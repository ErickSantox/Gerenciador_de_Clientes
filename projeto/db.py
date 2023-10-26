import psycopg2
from mainteste import *

db_params = {
    'dbname':'postgres',
    'user':'postgres',
    'password':'!Efraim032427',
    'host':'db.lbewbxclzsyynrgrwfll.supabase.co',
    'port':'5432'
}

def Cadastrar_clientes(codigo,cpf,nome,endereco,cep,bairro,telefone,descricao, numero):
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()

    try:
        insert_query = "INSERT INTO clientes(codigo,cpf,nome,endereco,bairro,cep,telefone,descricao, numero) VALUES(%s, %s, %s, %s,%s,%s,%s,%s, %s)"
        cursor.execute(insert_query,(codigo,cpf,nome,endereco,cep,bairro,telefone,descricao,numero))
        conn.commit()
        print("Cliente cadastrado com sucesso!")    
    except (Exception, psycopg2.Error) as error:
        conn.rollback()
        print("Erro ao cadastrar cliente:",error)
    finally:
        cursor.close()
        conn.close()

def Buscar_ClienteEnd(endereco):
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()
    

    select_query = "SELECT * FROM clientes WHERE endereco = %s"
    cursor.execute(select_query,(endereco,))
    nome = cursor.fetchone()

    cursor.close()
    conn.close()

    return nome

def Alterar_dados_cliente(endereco,novo_endereco,novo_bairro,novo_cep,novo_telefone,novo_numero,nova_descricao):
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()

    try:
        update_query = "UPDATE clientes SET endereco = %s, bairro = %s, cep = %s, telefone = %s, numero = %s, descricao = %s WHERE endereco = %s"
        cursor.execute(update_query, (novo_endereco,novo_bairro,novo_cep,novo_telefone,novo_numero,nova_descricao,endereco))
        conn.commit()
    except (Exception, psycopg2.Error) as error:
        conn.rollback()
        print("Erro ao alterar dados do cliente:",error)
    finally:
        cursor.close()
        conn.close()

def Excluir_cliente(endereco):
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()

    try:
        delete_query = "DELETE FROM clientes WHERE endereco = %s"
        cursor.execute(delete_query, (endereco,))
        conn.commit()
        print("Cliente excluído com sucesso")
    except (Exception, psycopg2.Error)as error:
        conn.rollback()
        print("Erro ao excluir cliente:",error)
    finally:
        cursor.close()
        conn.close()

#Verificação
def check_value(endereco):
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()

    check = "SELECT * FROM clientes WHERE endereco = %s"
    cursor.execute(check, (endereco,))
    result = cursor.fetchone()
    conn.close()
    return result is not None


#puxar resultado do banco 

def busca_TDClientes():
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()
    

    cursor.execute("SELECT codigo, cpf, nome, endereco, cep, bairro, telefone, descricao, numero FROM clientes")
    
    resultado = cursor.fetchone()

    conn.close()

    return resultado[0] if resultado else None
