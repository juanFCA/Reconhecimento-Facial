import os
import cv2
import numpy as np
from PIL import Image

recognizer = cv2.face.LBPHFaceRecognizer_create()
path = 'Dados/Imagens'

def getImagensComId(path):
    imagensPaths = [os.path.join(path, f) for f in os.listdir(path)]
    faces = []
    IDs = []

    for imagemPath in imagensPaths:
        faceImg = Image.open(imagemPath).convert('L');
        faceNp = np.array(faceImg, 'uint8')
        ID = int(os.path.split(imagemPath)[-1].split('.')[1])
        faces.append(faceNp)
        IDs.append(ID)
        cv2.imshow('Preparando Dados', faceNp)
        cv2.waitKey(10)

    return np.array(IDs), faces

IDs, faces = getImagensComId(path)
recognizer.train(faces, IDs)
recognizer.write('Dados/Recognizer/dadosPreparados.yml')

cv2.destroyAllWindows()
