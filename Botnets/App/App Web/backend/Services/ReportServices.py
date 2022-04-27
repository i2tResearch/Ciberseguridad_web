from backend.Modules.DB.Database import Database
from backend.Modules.Notification.Notification import Notification


class ReportService():

    def __init__(self):
        self.database = Database.getInstance()
        self.notification = Notification.getInstance()


    def getPredictionsHistory(self):

        send=[]
        history = self.database.getPredictions(self.notification.email())
        if len(history) > 0:
            for x in history:
                temp = list(x.values())[3] + ","+ list(x.values())[1] +","+ list(x.values())[0]
                send.append(temp)
        return send


    def getDataReportChart(self):
        send = []
        b = 0
        m = 0
        history = self.database.getPredictions(self.notification.email())
        if len(history) > 0:
            for x in history:
                if list(x.values())[3] == "Malign":
                    m += 1
                else:
                    b += 1
        send.append("Benign," + str(b))
        send.append("Malign," + str(m))
        return send



