from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

import smtplib
import threading
import time
import sys

threadLock = threading.Lock()
threads = []

class EmailThread(threading.Thread):

    def __init__(self, threadID, nome, email, imagem):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.nome = nome
        self.email = email
        self.imagem = imagem

    def run(self):
        print ("Iniciando " + self.nome)
        #Adiquirindo Lock para sincronizar as Threads
        threadLock.acquire()
        #chamamos a função
        enviarEmail(self.nome, self.email, self.imagem)
        #Liberamos Lock
        threadLock.release()

def enviarEmail(nome, email, imagem):
    msg = MIMEMultipart()
    # parametros da mensagem
    msg['From'] = "2jl.rfsystem@gmail.com"
    senha = "python2018"
    msg['To'] = email
    msg['Subject'] = "Você foi identificado no evento!"
    # Anexa a imagem no email
    with open(imagem, 'rb') as f:
        msgImg = MIMEImage(f.read(), name= nome)
    msg.attach(msgImg)
    # Servidor de email e a porta usada
    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    # Loga com a conta
    server.login(msg['From'], senha)
    # Envia a mensagem
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()

for t in threads:
    t.join()

print ("Finalizado Main Thread")
