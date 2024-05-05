import psycopg2
from Main import *

db_params = {
    'dbname':'Clientes',
    'user':'postgres',
    'password':'study',
    'host':'localhost',
    'port':'5432'
    
}

def Cadastrar_clientes(CodCliente,CpfCliente,NomeCliente,EnderecoCliente,NCasaCliente,BairroCliente,CepCliente,TellCliente, Descricao):
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()

    try:
        insert_query = "INSERT INTO clientesedna(CodCliente, CpfCliente, NomeCliente, EnderecoCliente, NCasaCliente, BairroCliente, CepCliente , TellCliente , Descricao) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(insert_query,(CodCliente,CpfCliente,NomeCliente,EnderecoCliente,NCasaCliente,BairroCliente,CepCliente,TellCliente, Descricao))
        conn.commit()
        print("Cliente cadastrado com sucesso!")    
    except (Exception, psycopg2.Error) as error:
        conn.rollback()
        print("Erro ao cadastrar cliente:",error)
    finally:
        cursor.close()
        conn.close()

def Buscar_ClienteEnd(EnderecoCliente,NCasaCliente):
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()
    

    select_query = "SELECT IdCliente, CodCliente, CpfCliente, NomeCliente, EnderecoCliente, NCasaCliente, BairroCliente, CepCliente , TellCliente , Descricao FROM clientesedna WHERE EnderecoCliente = %s AND NCasaCliente = %s "
    cursor.execute(select_query,(EnderecoCliente,NCasaCliente))
    nome = cursor.fetchone()

    cursor.close()
    conn.close()

    return nome

def Alterar_dados_cliente(novo_telefone,nova_descricao,EnderecoCliente,NCasaCliente):
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()

    try:
        update_query = "UPDATE clientesedna SET TellCliente =  %s, Descricao = %s WHERE EnderecoCliente = %s AND NCasaCliente = %s "
        cursor.execute(update_query, (novo_telefone,nova_descricao,EnderecoCliente,NCasaCliente))
        conn.commit()
    except (Exception, psycopg2.Error) as error:
        conn.rollback()
        print("Erro ao alterar dados do cliente:",error)
    finally:
        cursor.close()
        conn.close()

def Excluir_cliente(EnderecoCliente,NCasaCliente):
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()

    try:
        """DELETE FROM clientesedna WHERE EnderecoCliente = 'casa do caralho' AND NCasaCliente = '120A'"""
        delete_query = "DELETE FROM clientesedna WHERE EnderecoCliente = %s AND NCasaCliente = %s"
        cursor.execute(delete_query, (EnderecoCliente,NCasaCliente,))
        conn.commit()
        print("Cliente excluído com sucesso")
    except (Exception, psycopg2.Error)as error:
        conn.rollback()
        print("Erro ao excluir cliente:",error)
    finally:
        cursor.close()
        conn.close()

#Verificação
def check_value(EnderecoCliente,NCasaCliente):
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()

    check = "SELECT IdCliente, CodCliente, CpfCliente, NomeCliente, EnderecoCliente, NCasaCliente, BairroCliente, CepCliente , TellCliente , Descricao FROM clientesedna WHERE EnderecoCliente = %s AND NCasaCliente = %s"
    cursor.execute(check, (EnderecoCliente,NCasaCliente,))
    result = cursor.fetchone()
    conn.close()
    return result is not None

#puxar resultado do banco 
def busca_TDClientes():
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()
    

    cursor.execute("SELECT IdCliente, CodCliente, CpfCliente, NomeCliente, EnderecoCliente, NCasaCliente, BairroCliente, CepCliente , TellCliente , Descricao FROM clientesedna ")
    
    resultado = cursor.fetchone()

    conn.close()

    return resultado[0] if resultado else None
