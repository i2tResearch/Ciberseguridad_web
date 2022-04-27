import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import backend.Modules.Routes.Routes as Routes


class Notification():
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if Notification.__instance == None:
            Notification()
        return Notification.__instance

    def __init__(self,email):
        if Notification.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Notification.__instance = self
            self._email = email



    def email(self):
        return self._email


    def setEmail(self, email):
        self._email = email


    def sendEmail(self):
        if len(self._email) > 0:
            print("::::::::::::::::::::::::::::")
            print(":::: SENDING EMAIL...... ::::")
            print("::::::::::::::::::::::::::::")
            sender = Routes.returnEmail()
            receiver = self._email

            serverEmail = smtplib.SMTP(host='smtp.gmail.com', port=587)
            serverEmail.ehlo()
            serverEmail.starttls()
            serverEmail.ehlo()
            serverEmail.login(sender, Routes.returnEmailPassword())

            msg = MIMEMultipart()
            message = MIMEText("Este correo ha sido enviado desde - Analysis Of Time Windows To Detect Botnet Behaviour-2")
            msg['From'] = sender
            msg['To'] = receiver
            msg['Subject'] = "Anomalía presentada en el análisis de red"
            msg.attach(MIMEText(message.as_string()))

            print(sender)
            print(receiver)
            serverEmail.sendmail(sender, receiver, msg.as_string())
            serverEmail.close()

