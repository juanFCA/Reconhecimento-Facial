#Importação das bibliotecas necessárias
import cv2
import numpy as np
import sqlite3
import os.path

#Cria as pastas necessárias
if(os.path.isdir('../Dados/Imagens')==False):
    os.makedirs('../Dados/Imagens')
if(os.path.isdir('../Dados/Recognizer')==False):
    os.makedirs('../Dados/Recognizer')

#Lincamos o cascade de detecção de face
faceDetector = cv2.CascadeClassifier('../Dependencias/haarcascade_frontalface_default.xml')
#Capturamos a camera
cam = cv2.VideoCapture(0)

#Definimos a função que busca a pessoa
def capturaIdPessoa(NomePessoa):
    #Criamos a conexão com o banco de dados
    conn = sqlite3.connect('../Dados/FaceDataBase.db')
    #Criamos um cursor para percorrer o Banco
    cursor = conn.cursor()
    #Comando sql
    cmdSeleciona = "SELECT ID FROM Pessoa WHERE NOME="+"'"+str(NomePessoa)+"'"
    #Executamos o comando
    cursor.execute(cmdSeleciona)
    # Inicializamos a variável com o valor default de None que é o equivalente de NULL
    IdPessoa = None
    # Como o cursor é uma tupla retornando os valores temos como resultado
    # cursor[id, nome, idade] logo para recuperar o dado nescessário fazemos um for value in variable:
    for linha in cursor:
        #como o id é a primeira posição na tupla(linha) temos de pegar a posição 0 do vetor
        IdPessoa = linha[0]
    #Fazemos o commit
    conn.commit()
    #Fechamos a conexão
    conn.close()
    #Returnamos o valor
    return IdPessoa

#Definicao da funcao de inserção/atualização do Banco de Dados
def insereOuAtualiza(NomePessoa, IdadePessoa):
    #Criamos a conexão com o banco de Dados
    conn = sqlite3.connect('../Dados/FaceDataBase.db')
    #Criamos um cursor do sqlite3
    cursor = conn.cursor()
    #Comando SQL
    cmdSeleciona = "SELECT * FROM Pessoa WHERE ID="+"'"+str(capturaIdPessoa(NomePessoa))+"'"
    #Executamos o comando
    cursor.execute(cmdSeleciona)
    #Existe cadastro
    existeCadastro = 0
    for linha in cursor:
        existeCadastro = 1
    #Então atualizamos os dados
    if (existeCadastro == 1):
        cmdAtualiza = "UPDATE Pessoa SET NOME="+"'"+str(NomePessoa)+"'"+", IDADE="+"'"+str(IdadePessoa)+"'"+" WHERE ID="+"'"+str(capturaIdPessoa(NomePessoa))+"'"
        cursor.execute(cmdAtualiza)
    #Senão inserimos os dados no banco com o comando
    else:
        cmdInsere = "INSERT INTO Pessoa(NOME,IDADE) Values ("+"'"+str(NomePessoa)+"'"+","+"'"+str(IdadePessoa)+"'"+")"
        cursor.execute(cmdInsere)
    #Fazemos o commit
    conn.commit()
    #Fechamos a conexão
    cursor.close()
    conn.close()

#Criamos os inputes para os Dados
NomePessoa = input('Digite o Nome da Pessoa:  ')
IdadePessoa = input('Digite a Idade da Pessoa:  ')
#Chamamos a Função
insereOuAtualiza(NomePessoa, IdadePessoa)
#Buscamos no banco o id recebido pela pessoa cadastrada
IdPessoa = capturaIdPessoa(NomePessoa)
#Atributo qye conta a quantidade de imagens de amostras do usuário
amostrasNum = 0

#Loop para captura de amostras
while (True):
    ret, img = cam.read();
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceDetector.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        amostrasNum += 1
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        cv2.imwrite('../Dados/Imagens/Pessoa.'+str(IdPessoa)+'.'+str(amostrasNum)+'.jpg', gray[y:y+h,x:x+w])
        cv2.waitKey(100)
        #Enquanto não pararmos o código ele continua a tirar fotos
        cv2.imshow("Captura de Imagens", img)

    #Se aperta a tecla
    if cv2.waitKey(1) == ord('q'):
        break
    #Se tirou 21 (0-20) fotos então para
    elif (amostrasNum > 20):
        break

#Liberamos a câmera
cam.release()
cv2.destroyAllWindows()
