import threading
import backend.Modules.DataMining.PcapTools as PcapTools
import backend.Modules.DataMining.NfpcapTools as NfpcapTools
import backend.Modules.DataMining.TimeWindowTools as TimeWindowTools
import backend.Modules.DataScience.MachineLearningPrediction as predictionML
import backend.Modules.Routes.Routes as Routes
from backend.Modules.DB.Database import Database
from backend.Modules.Notification.Notification import Notification


class ScanServices():

    def __init__(self):
        self._isRunning = False
        self.notification = Notification("")
        self.database = Database()


    def setIsRunning(self, isRunning):
        self._isRunning = isRunning

    def run(self):
        thread = threading.Thread(target=self.scan())
        thread.start()

    def scan(self):
        while(self._isRunning):
            PcapTools.pcapGenerator(Routes.returnRoutePcap() + Routes.returnNamePcap())
            NfpcapTools.nfpcapGenerator(Routes.returnRouteNFpcap(), Routes.returnRoutePcap(), Routes.returnNamePcap())
            NfpcapTools.renameNfpcaps(Routes.returnRouteNFpcap())
            TimeWindowTools.nfpcapsToCSV(Routes.returnRouteTw(), Routes.returnRouteNFpcap())
            TimeWindowTools.datasetGenerator(Routes.returnRouteDataset(), Routes.returnRouteTw(),
                                            Routes.returnNameDataset())

            #score = predictionML.RandomForestClassifierPrediction(Routes.returnRouteDataset() + Routes.returnNameDataset())
            score = predictionML.decisionTreeClassifier(Routes.returnRouteDataset() + Routes.returnNameDataset())
            #score = predictionML.logisticRegression(Routes.returnRouteDataset() + Routes.returnNameDataset())
            #score = predictionML.KNNPrediction(Routes.returnRouteDataset() + Routes.returnNameDataset())
            print("::::::::::::::::::::::::::::")
            print(":::: SCORE : " + str(score) +"...... :::: ")
            print("::::::::::::::::::::::::::::")
            if score == 1:
                self.notification.sendEmail()

            self.database.saveInDatabase(self.notification._email, score)
            PcapTools.deletePcapFIle(Routes.returnRoutePcap() + Routes.returnNamePcap())
            NfpcapTools.deleteNFpcaps(Routes.returnRouteNFpcap())
            TimeWindowTools.deleteTW(Routes.returnRouteTw())
            TimeWindowTools.deleteDataset(Routes.returnRouteDataset() + Routes.returnNameDataset())


    def configureEmail(self,email):
        self.notification.setEmail(email)


    @classmethod
    def getEmail(self):
       return self.notification.email()