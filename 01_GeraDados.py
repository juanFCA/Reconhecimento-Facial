#Importação das bibliotecas necessárias
import cv2
import numpy as np
import sqlite3

#Lincamos o cascade de detecção de face
faceDetect = cv2.CascadeClassifier('Dependencias/haarcascade_frontalface_default.xml')
#Capturamos a camera
cam = cv2.VideoCapture(0)

#Definicao da funcao de inserção/atualização do Banco de Dados
def insereOuAtualiza(IdPessoa, NomePessoa, IdadePessoa):
    #Criamos a conexão com o banco de Dados
    conn = sqlite3.connect('Dados/FaceDataBase.db')
    #Criamos um cursor do sqlite3
    cursor = conn.cursor()
    #Comando SQL
    cmdSeleciona = "SELECT * FROM Pessoa WHERE ID="+"'"+str(IdPessoa)+"'"
    #Executamos o comando
    cursor.execute(cmdSeleciona)
    #Existe cadastro
    existeCadastro = 0
    for linha in cursor:
        existeCadastro = 1
    #Então atualizamos os dados
    if (existeCadastro == 1):
        cmdAtualiza = "UPDATE Pessoa SET NOME="+"'"+str(NomePessoa)+"'"+", IDADE="+"'"+str(IdadePessoa)+"'"+" WHERE ID="+"'"+str(IdPessoa)+"'"
        cursor.execute(cmdAtualiza)
    #Senão inserimos os dados no banco com o comando
    else:
        cmdInsere = "INSERT INTO Pessoa(ID,NOME,IDADE) Values ("+"'"+str(IdPessoa)+"'"+","+"'"+str(NomePessoa)+"'"+","+"'"+str(IdadePessoa)+"'"+")"
        cursor.execute(cmdInsere)
    #Fazemos o commit
    conn.commit()
    #Fechamos a conexão
    conn.close()

#Criamos os inputes para os Dados
IdPessoa = input('Digite o ID da Pessoa:  ')
NomePessoa = input('Digite o Nome da Pessoa:  ')
IdadePessoa = input('Digire a Idade da Pessoa:  ')
#Chamamos a Função
insereOuAtualiza(IdPessoa, NomePessoa, IdadePessoa)
#Atributo qye conta a quantidade de imagens de amostras do usuário
amostrasNum = 0

#Loop para captura de amostras
while (True):
    ret, img = cam.read();
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        amostrasNum += 1
        cv2.imwrite('Dados/Imagens/Pessoa.'+str(IdPessoa)+'.'+str(amostrasNum)+'.jpg', gray[y:y+h,x:x+w])
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        cv2.waitKey(100)
    #Enquanto não pararmos o código ele continua a tirar fotos
    cv2.imshow("Captura de Imagens", img)
    cv2.waitKey(1)
    #Se aperta a tecla
    if cv2.waitKey(1)==ord('q'):
        break
    #Se tirou 20 fotos então para
    elif (amostrasNum > 20):
        break;

#Liberamos a câmera
cam.release()
cv2.destroyAllWindows()
