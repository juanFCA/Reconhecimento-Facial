import cv2
import numpy as np
import sqlite3

faceDetect = cv2.CascadeClassifier('Dependencias/haarcascade_frontalface_default.xml')
#Capturamos a camera
cam = cv2.VideoCapture(0)
cam.set(3, 800) # Set largura
cam.set(4, 600) # Set altura

# Define tamanho minimo de janela para reconhecer como face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

#Criamos um recognizer que lê arquivos salvos
recognizer = cv2.face.LBPHFaceRecognizer_create();
#Carregamos o arquivo com os dados preparados
recognizer.read('Dados/Recognizer/dadosPreparados.yml')
#Setamos a fonte do texto
fontFace = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 1
fontColor = (255, 255, 255)

#Função que recupera dados no banco de acordo com o # IDEA:
def getPessoa(IdPessoa):
    #Conectamos com o banco
    conn = sqlite3.connect('Dados/FaceDataBase.db')
    #Instanciamos um cursor
    cursor = conn.cursor()
    #Comando para buscar a pessoa
    cmdSeleciona = "SELECT * FROM Pessoa WHERE ID="+"'"+str(IdPessoa)+"'"
    #Executamos o comando
    cursor.execute(cmdSeleciona)
    #Inicialmente setamos a pessoa como None
    pessoa = None
    #Se for encontrada passamos a linha para pessoa
    for linha in cursor:
        pessoa = linha
    #Encerramos a conexão
    conn.close()
    #Retornamos o dado necessário
    return pessoa

while (True):
    ret, img = cam.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH))
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        ID, confidence = recognizer.predict(gray[y:y+h,x:x+w])
        pessoa = getPessoa(ID)
        porcentagem = "  {0}%".format(round(100 - confidence))
        #Se a pessoa for diferente de None
        if (pessoa != None):
            cv2.putText(img, 'Nome: '+str(pessoa[1]), (x,y+h+20), fontFace, fontScale, fontColor, 1)
            cv2.putText(img, 'Idade: '+str(pessoa[2]), (x,y+h+45), fontFace, fontScale, fontColor, 1)
            cv2.putText(img, str(porcentagem), (x,y-5), fontFace, fontScale, fontColor, 1)
        else:
            cv2.putText(img,'Desconhecido', (x,y+h+20), fontFace, fontScale, fontColor, 1)

    cv2.imshow('Reconhecimento Facial', img)
    #Fecha a janela quando aperta q
    if(cv2.waitKey(1)==ord('q')):
        break;
#Liberamos a câmera
cam.release()
#Destruimos todas as janelas
cv2.destroyAllWindows()
