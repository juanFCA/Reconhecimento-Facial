import numpy as np
import cv2
import sys
import os
from PIL import Image

class PreparaDadosLBPH:
    def __init__(self):
        cascPath = "Dependencias/haarcascade_frontalface_default.xml"
        self.face_cascade = cv2.CascadeClassifier(cascPath)
        self.face_dir = 'Dados/Imagens'
        if not os.path.isdir('Dados/Recognizer'):
            os.mkdir('Dados/Recognizer')
        #self.model = cv2.face.LBPHFaceRecognizer_create()  
        self.model = cv2.face.createLBPHFaceRecognizer()

    def lbph_treina_data(self):
        imgs = []
        tags = []
        index = 0

        for (subdirs, dirs, files) in os.walk(self.face_dir):
            for subdir in dirs:
                img_path = os.path.join(self.face_dir, subdir)
                for fn in os.listdir(img_path):
                    path = img_path + '/' + fn
                    tag = index
                    imgs.append(cv2.imread(path, 0))
                    tags.append(int(tag))
                index += 1
        (imgs, tags) = [np.array(item) for item in [imgs, tags]]

        self.model.train(imgs, tags)
        self.model.save('Dados/Recognizer/dadosPreparadosLBPH.yml')
        print ("Treinamento dos dados completados com sucesso")
        return


if __name__ == '__main__':
    treinar = PreparaDadosLBPH()
    treinar.lbph_treina_data()
    print ("Digite o próximo usuário a treinar ou pressione Reconhecer")
