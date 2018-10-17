from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import smtplib

class Email:
    ### Implementar Thread para enviar os emails e processar as imagens
    imagemIdentificada = "" #print da imagem identificada
    nomeUsuario = "" #nome do usuário identificado
    emailUsuario = "" #email do usuário identificado

    def enviarEmail(self):
        
        msg = MIMEMultipart()
        
        # parametros da mensagem
        msg['From'] = "2jl.rfsystem@gmail.com"
        senha = "python2018"
        msg['To'] = self.emailUsuario
        msg['Subject'] = "Você foi identificado no evento!"
    
        # Anexa a imagem no email
        with open(self.imagemIdentificada, 'rb') as f:
            msgImg = MIMEImage(f.read(), name=self.nomeUsuario)
        msg.attach(msgImg)
    
        # Servidor de email e a porta usada
        server = smtplib.SMTP('smtp.gmail.com: 587')
        
        server.starttls()
    
        # Loga com a conta
        server.login(msg['From'], senha)
    
        # Envia a mensagem
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        
        server.quit()