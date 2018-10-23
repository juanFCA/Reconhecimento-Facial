import sys
import os
import sqlite3

#Definimos a função que busca ao ID
def captura_id_pessoa(nomePessoa):
    #Criamos a conexão com o banco de dados
    conn = sqlite3.connect('Dados/FaceDataBase.db')
    #Criamos um cursor para percorrer o Banco
    cursor = conn.cursor()
    #Comando sql
    cmdSeleciona = "SELECT ID FROM Pessoa WHERE NOME="+"'"+str(nomePessoa)+"'"
    #Executamos o comando
    cursor.execute(cmdSeleciona)
    # Inicializamos a variável com o valor default de None que é o equivalente de NULL
    Pessoa = None
    # Como o cursor é uma tupla retornando os valores temos como resultado
    # cursor[id, nome, email, presente] logo para recuperar o dado nescessário fazemos um for value in variable:
    for linha in cursor:
        #como o id é a primeira posição na tupla(linha) temos de pegar a posição 0 do vetor
        Pessoa = linha[0]
    #Fazemos o commit
    conn.commit()
    #Fechamos a conexão
    conn.close()
    #Returnamos o valor
    return Pessoa

#Definimos a função que busca a pessoa
def captura_pessoa(nomePessoa):
    #Criamos a conexão com o banco de dados
    conn = sqlite3.connect('Dados/FaceDataBase.db')
    #Criamos um cursor para percorrer o Banco
    cursor = conn.cursor()
    #Comando sql
    cmdSeleciona = "SELECT * FROM Pessoa WHERE NOME="+"'"+str(nomePessoa)+"'"
    #Executamos o comando
    cursor.execute(cmdSeleciona)
    # Inicializamos a variável com o valor default de None que é o equivalente de NULL
    Pessoa = None
    # Como o cursor é uma tupla retornando os valores temos como resultado
    # cursor[id, nome, email, presente] logo para recuperar o dado nescessário fazemos um for value in variable:
    for linha in cursor:
        Pessoa = linha
    #Fazemos o commit
    conn.commit()
    #Fechamos a conexão
    conn.close()
    #Returnamos o valor
    return Pessoa

#Definicao da funcao de inserção/atualização do Banco de Dados
def insere_ou_atualiza(nomePessoa, emailPessoa, presentePessoa):
    #Criamos a conexão com o banco de Dados
    conn = sqlite3.connect('Dados/FaceDataBase.db')

    #Criamos um cursor do sqlite3
    cursor = conn.cursor()
    #Comando SQL
    cmdSeleciona = "SELECT * FROM Pessoa WHERE ID="+"'"+str(captura_id_pessoa(nomePessoa))+"'"
    #Executamos o comando
    cursor.execute(cmdSeleciona)
    #Existe cadastro
    existeCadastro = 0
    for linha in cursor:
        existeCadastro = 1
    #Então atualizamos os dados
    if (existeCadastro == 1):
        cursor.execute("UPDATE Pessoa SET NOME = ?, EMAIL = ?, PRESENTE = ? WHERE id = ?", (nomePessoa, emailPessoa, presentePessoa, captura_id_pessoa(nomePessoa)))
        #cmdAtualiza = "UPDATE Pessoa SET NOME="+"'"+str(nomePessoa)+"'"+", EMAIL="+"'"+str(emailPessoa)+"'"+", PRESENTE="+"'"+str(presentePessoa)+" WHERE ID="+"'"+str(captura_id_pessoa(nomePessoa))+"'"
        #cursor.execute(cmdAtualiza)
    #Senão inserimos os dados no banco com o comando
    else:
        cursor.execute("INSERT INTO Pessoa(NOME,EMAIL,PRESENTE) VALUES ('" + str(nomePessoa) + "' , '" + str(emailPessoa) + "' , '" + str(presentePessoa) +"' )")
    #Fazemos o commit
    conn.commit()
    #Fechamos a conexão
    cursor.close()
    conn.close()

#Definimos a função que busca ao ID
def reseta_valor_presente():
    #Criamos a conexão com o banco de dados
    conn = sqlite3.connect('Dados/FaceDataBase.db')
    #Criamos um cursor para percorrer o Banco
    cursor = conn.cursor()
    #Executamos o comando
    cursor.execute("UPDATE Pessoa SET PRESENTE = 0")
    #Fazemos o commit
    conn.commit()
    #Fechamos a conexão
    cursor.close()
    conn.close()