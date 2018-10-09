import os
import cv2
import numpy as np
from PIL import Image

recognizer = cv2.face.LBPHFaceRecognizer_create()
faceDetector = cv2.CascadeClassifier("../Dependencias/haarcascade_frontalface_default.xml")
#Local onde as imagens foram salvas
path = '../Dados/Imagens'

def getImagensComId(path):
    imagensPaths = [os.path.join(path, f) for f in os.listdir(path)]
    facesAmostras = []
    IDs = []

    for imagemPath in imagensPaths:
        # Converte a imagem para escala de cinza
        faceImg = Image.open(imagemPath).convert('L');
        faceNp = np.array(faceImg, 'uint8')
        ID = int(os.path.split(imagemPath)[-1].split(".")[1])
        faces = faceDetector.detectMultiScale(faceNp)

        for(x, y, w, h) in faces:
            facesAmostras.append(faceNp[y:y+h,x:x+w])
            IDs.append(ID)
            cv2.imshow('Preparando Dados', faceNp)
            cv2.waitKey(10)

    return facesAmostras, np.array(IDs)

facesAmostras, IDs = getImagensComId(path)
recognizer.train(facesAmostras, IDs)
#Salvamos o modelo
recognizer.write('../Dados/Recognizer/dadosPreparados.yml')
#Printamos a quantidade de faces detectadas e preparadas
print("[ INFO:1] {0} faces Preparadas. Encerrando Programa\n".format(len(np.unique(IDs))))
#Encerramos a utilização da tela
cv2.destroyAllWindows()
