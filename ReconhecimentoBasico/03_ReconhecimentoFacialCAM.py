import cv2
import numpy as np
import sqlite3

#Criamos um recognizer que lê arquivos salvos
recognizer = cv2.face.LBPHFaceRecognizer_create();
#Carregamos o arquivo com os dados preparados
recognizer.read('../Dados/Recognizer/dadosPreparados.yml')

faceDetector = cv2.CascadeClassifier('../Dependencias/haarcascade_frontalface_default.xml')
#Capturamos a camera
cam = cv2.VideoCapture(0)
cam.set(3, 800) # Set largura
cam.set(4, 600) # Set altura

# Define tamanho minimo de janela para reconhecer como face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

#Setamos a fonte do texto
fontFace = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 1
fontColor = (255, 255, 255)

#Função que recupera dados no banco de acordo com o # IDEA:
def getPessoa(IdPessoa):
    #Conectamos com o banco
    conn = sqlite3.connect('../Dados/FaceDataBase.db')
    #Instanciamos um cursor
    cursor = conn.cursor()
    #Comando para buscar a pessoa
    cmdSeleciona = "SELECT * FROM Pessoa WHERE ID="+"'"+str(IdPessoa)+"'"
    #Executamos o comando
    cursor.execute(cmdSeleciona)
    #Inicializamos a variavel como nula
    pessoa = None
    #Se foram encontrado dados passamos a linha para pessoa
    for linha in cursor:
        pessoa = linha
    #Encerramos a conexão
    cursor.close()
    conn.close()
    #Retornamos o dado necessário
    return pessoa

while (True):
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceDetector.detectMultiScale(
        gray,
        scaleFactor = 1.3,
        minNeighbors = 8,
        minSize = (int(minW), int(minH))
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        ID, confidence = recognizer.predict(gray[y:y+h,x:x+w])
        pessoa = getPessoa(ID)
        #Interceptando os valores
        print(recognizer.predict((gray[y:y+h,x:x+w])))
        #Para principios de probabilidade temos que se a confidence retornar valor 0
        #significa que temos uma correspondencia de 100% ou seja fazemos 100 - confidence
        #para encontrarmos a porentagem de acerto da compinação
        porcentagem = "  {0}%".format(round(100 - confidence))
        #Se a pessoa for diferente de None
        if(confidence <= 60):
            cv2.putText(img, 'Nome: '+str(pessoa[1]), (x,y+h+20), fontFace, fontScale, fontColor, 1)
            cv2.putText(img, 'Idade: '+str(pessoa[2]), (x,y+h+45), fontFace, fontScale, fontColor, 1)
            cv2.putText(img, str(porcentagem), (x,y-5), fontFace, fontScale, fontColor, 1)
        else:
            cv2.putText(img,'Desconhecido', (x,y+h+20), fontFace, fontScale, (255,0,0), 1)

    cv2.imshow('Reconhecimento Facial', img)
    #Fecha a janela quando aperta q
    if(cv2.waitKey(1)==ord('q')):
        break
#Liberamos a câmera
cam.release()
#Destruimos todas as janelas
cv2.destroyAllWindows()
