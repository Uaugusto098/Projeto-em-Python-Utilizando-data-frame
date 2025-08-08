import sqlite3 as sqlite
import pandas as pd





conn=sqlite.connect('BancoDeDados.db')
cursor=conn.cursor()


def dataframe():
    return  pd.read_sql_query('SELECT * FROM usuario',conn)






def deletetable():
    cursor.execute(''' DELETE FROM usuario''')
    cursor.execute(''' DELETE FROM sqlite_sequence WHERE name='usuario' ''')
    conn.commit()


def criartabela():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuario (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL,
        cidade TEXT NOT NULL
                            )
        ''')
    conn.commit()

def registros():
    nome=input("Nome: ")
    idade=input("Idade: ")
    cidade=input("Cidade: ")
    cursor.execute('''INSERT INTO usuario (nome,idade,cidade) VALUES (?,?,?)''',(nome,idade,cidade))
    conn.commit()
    
def excluirlinha():  
    while True:
       
        id=input("Digite o ID que deseja excluir: ")
        escolha=input("Deseja continuar ?: ")
        if escolha=="nao" or escolha=="n":
            break
        cursor.execute('''DELETE FROM usuario WHERE id=?''',(id) )
        conn.commit()
        

def atualizaruser():
    while True:
        print('''
            1-Nome
            2-Idade
            3-Cidade
            0-Sair
            ''')
        escolha=input("Opção: ")

        match escolha:
            case "1":
                id=int(input("Digite o id desejado: "))
                nome=input("Digite o nome a atualizar: ")
                cursor.execute('''UPDATE usuario SET nome=? WHERE id=?''',(nome,id))
                conn.commit()
                cnt=input("Deseja continuar ?: ")
                if cnt=="nao" or cnt=="n":
                    break
            case "2":
                id=int(input("Digite o id desejado: "))
                idade=input("Digite a idade a atualizar: ")
                cursor.execute('''UPDATE usuario SET idade=? WHERE id=?''',(idade,id))
                conn.commit()
                cnt=input("Deseja continuar ?: ")
                if cnt=="nao" or cnt=="n":
                    break
            case "3":
                id=int(input("Digite o id desejado: "))
                cidade=input("Digite o cidade a atualizar: ")
                cursor.execute('''UPDATE usuario SET cidade=? WHERE id = ?''',(cidade,id))
                conn.commit()
                cnt=input("Deseja continuar ?: ")
                if cnt=="nao" or cnt=="n":
                    break
while True:
    print("                  Banco de dados para cadastros")
    print('''
            1-Criar tabela
            2-Registrar cliente
            3-Excluir cliente
            4-Atualizar dados do cliente
            5-Deletar tabela
            6-Exibir DataFrame
            0-Sair''')
    escolha=input("Opção: ")


    match escolha:
        case "1":
            criartabela()
            esc=input("Voltar para o menu ?: ")
            if esc=="nao" or esc=="n":
                break
        case"2":
            registros()
            esc=input("Voltar para o menu ?: ")
            if esc=="nao" or esc=="n":
                break
        case"3":
            excluirlinha()
            esc=input("Voltar para o menu ?: ")
            if esc=="nao" or esc=="n":
                break
        case "4":
            atualizaruser()
            esc=input("Voltar para o menu ?: ")
            if esc=="nao" or esc=="n":
                break
        case "5":
            deletetable()
            esc=input("Voltar para o menu ?: ")
            if esc=="nao" or esc=="n":
                break
        case "6":
            df=dataframe()
            print(df)
            esc=input("Voltar para o menu ?: ")
            if esc=="nao" or esc=="n":
                break
        case "0":
            print("Saindo do sistema...")
            break