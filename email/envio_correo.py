import smtplib #Importación para representar una conexión con el servidor de correo smtp: Gmail
import os #Simular la extracción de datos desde variables de entorno
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart #MIMEMultipart Indica que el correo va a estar compuesto de varias partes como texto, html, imagenes, adjuntos, etc. Estructura, clase del correo 
from email.mime.text import MIMEText #Sería una de esas partes como imagenes, adjuntos etc

load_dotenv() #Carga las variables de entorno para el script

remitente = os.getenv('USER')
destinatario = 'juanpaguzman14@gmail.com'
asunto = 'Test'

msg = MIMEMultipart()
msg['Subject'] = asunto
msg['From'] = remitente
msg['To'] = destinatario

with open('email.html', 'r') as archivo:
    html = archivo.read()

#Adjuntar contenido HTML
msg.attach(MIMEText(html, 'html'))

#Representa una conexión con un servidor de correo saliente (SMTP Server)
server = smtplib.SMTP('smtp.gmail.com', 587)
#Conexión segura
server.starttls()
server.login(remitente, os.getenv('PASS'))

#Envío de correo electrónico
server.sendmail(remitente,
                destinatario,
                msg.as_string())

server.quit()