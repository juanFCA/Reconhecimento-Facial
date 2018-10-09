import numpy as np 
import cv2
import sys 
import os 
import sqlite3

#CONSTANTES UTILIZDAS NO CODIGO
FREQ_DIVIDER = 5
REDMEN_FACTOR = 4
NUM_TREINAMENTO = 100

class AdicionaPessoa:
    #Metodo quando a classe e iniciada
    def __init__(self):
        cascPath = "Dependencias/haarcascade_frontalface_default.xml"
        self.face_cascade = cv2.CascadeClassifier(cascPath)
        self.face_dir = "Dados/Imagens"
        self.face_nome = sys.argv[1]
        self.face_idade = sys.argv[2]
        self.insere_ou_atualiza(self.face_nome, self.face_idade)
        self.path = os.path.join(self.face_dir, self.face_nome)
        if not os.path.isdir(self.face_dir):
            os.mkdir(self.face_dir)
        if not os.path.isdir(self.path):
            os.mkdir(self.path)
        self.conta_capturas = 0
        self.conta_tempo = 0
    
    #Função para captura e preparo das imagens
    def captura_treinamento_imagens(self):
        video_capture = cv2.VideoCapture(0)
        while True:
            self.conta_tempo += 1
            ret, frame = video_capture.read()
            imgEntrada = np.array(frame)
            imgSaida = self.processa_imagem(imgEntrada)
            cv2.imshow("Captura de Imagens", imgSaida)
            #Quando tudo estiver pronto, termina a captura quando q for pressionado
            if cv2.waitKey(1) & 0xFF == ord('q'):
                video_capture.release()
                cv2.destroyAllWindows()
                return
    
    #Função para processar imagens
    def processa_imagem(self, imgEntrada):
        frame = cv2.flip(imgEntrada, 1)
        resized_width, resized_height = (112, 92)
        if self.conta_capturas < NUM_TREINAMENTO:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gray_resized = cv2.resize(gray, (int(gray.shape[1] / REDMEN_FACTOR), int(gray.shape[0] / REDMEN_FACTOR)))
            faces = self.face_cascade.detectMultiScale(
                gray_resized,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                flags=cv2.CASCADE_SCALE_IMAGE
            )
            if len(faces) > 0:
                areas = []
                for (x, y, w, h) in faces:
                    areas.append(w * h)
                max_area, idx = max([(val, idx) for idx, val in enumerate(areas)])
                face_sel = faces[idx]

                x = face_sel[0] * REDMEN_FACTOR
                y = face_sel[1] * REDMEN_FACTOR
                w = face_sel[2] * REDMEN_FACTOR
                h = face_sel[3] * REDMEN_FACTOR

                face = gray[y:y + h, x:x + w]
                face_resized = cv2.resize(face, (resized_width, resized_height))
                img_no = sorted([int(fn[:fn.find('.')]) for fn in os.listdir(self.path) if fn[0] != '.'] + [0])[-1] + 1

                if self.conta_tempo % FREQ_DIVIDER == 0:
                    cv2.imwrite('%s/%s.png' % (self.path, img_no), face_resized)
                    self.conta_capturas += 1
                    print ("Imagens Capturadas: ", self.conta_capturas)

                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
                cv2.putText(frame, self.face_nome, (x - 10, y - 10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0))
        elif self.conta_capturas == NUM_TREINAMENTO:
            print ("Dados de treinamento capturados. Pressione 'q' para sair.")
            self.conta_capturas += 1

        return frame

    #Definimos a função que busca a pessoa
    def captura_id_pessoa(self, nomePessoa):
        #Criamos a conexão com o banco de dados
        conn = sqlite3.connect('Dados/FaceDataBase.db')
        #Criamos um cursor para percorrer o Banco
        cursor = conn.cursor()
        #Comando sql
        cmdSeleciona = "SELECT ID FROM Pessoa WHERE NOME="+"'"+str(nomePessoa)+"'"
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
    def insere_ou_atualiza(self, nomePessoa, IdadePessoa):
        #Criamos a conexão com o banco de Dados
        conn = sqlite3.connect('Dados/FaceDataBase.db')
        #Criamos um cursor do sqlite3
        cursor = conn.cursor()
        #Comando SQL
        cmdSeleciona = "SELECT * FROM Pessoa WHERE ID="+"'"+str(self.captura_id_pessoa(nomePessoa))+"'"
        #Executamos o comando
        cursor.execute(cmdSeleciona)
        #Existe cadastro
        existeCadastro = 0
        for linha in cursor:
            existeCadastro = 1
        #Então atualizamos os dados
        if (existeCadastro == 1):
            cmdAtualiza = "UPDATE Pessoa SET NOME="+"'"+str(nomePessoa)+"'"+", IDADE="+"'"+str(IdadePessoa)+"'"+" WHERE ID="+"'"+str(self.captura_id_pessoa(nomePessoa))+"'"
            cursor.execute(cmdAtualiza)
        #Senão inserimos os dados no banco com o comando
        else:
            cmdInsere = "INSERT INTO Pessoa(NOME,IDADE) Values ("+"'"+str(nomePessoa)+"'"+","+"'"+str(IdadePessoa)+"'"+")"
            cursor.execute(cmdInsere)
        #Fazemos o commit
        conn.commit()
        #Fechamos a conexão
        cursor.close()
        conn.close()

if __name__ == '__main__':
    treinar = AdicionaPessoa()
    treinar.captura_treinamento_imagens()
print ("Digite o próximo usuário a treinar ou pressione Reconhecer")   
