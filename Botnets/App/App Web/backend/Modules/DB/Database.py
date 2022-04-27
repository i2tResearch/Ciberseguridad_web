from firebase import firebase
import backend.Modules.Routes.Routes as Routes
import datetime


class Database():

    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if Database.__instance == None:
            Database()
        return Database.__instance

    def __init__(self):

        if Database.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Database.__instance = self
            self.firebase = firebase
            self.firebaseApp = Routes.returnFirebaseApp()
            self.dbName = Routes.returnDBName()
            self.UserTableName = Routes.returnUsersTableName()


    # email must be j@correob
    def saveInDatabase(self, email, prediction):
        if len(email) > 0:
            print("::::::::::::::::::::::::::::")
            print(":::: SAVING IN DATABASE...... ::::")
            print("::::::::::::::::::::::::::::")
            email = email.replace(".com","")
            firebase = self.firebase.FirebaseApplication(self.firebaseApp, None)

            data = None

            if prediction == 0:
                data= {
                    'email': email.replace("/",""),
                    'prediction': 'Benign',
                    'Message': 'You are secure!',
                    'datetime': datetime.datetime.today()
                }
            else:
                data = {
                    'email': email.replace("/",""),
                    'prediction': 'Malign',
                    'Message': 'Dangerous!! You have malicious behaviour... Probably you are a zombie of a botnet!',
                    'datetime': datetime.datetime.today()
                }

            firebase.post(self.UserTableName + email, data)

    # email must be j@correo
    def getPredictions(self, email):
        pred = []
        if len(email) > 0:
            pred = []
            email = email.replace(".com", "")
            firebase = self.firebase.FirebaseApplication(self.firebaseApp, None)
            result = firebase.get(self.UserTableName + email,'')
            if result != None:
                pred = list(result.values())
        return pred



