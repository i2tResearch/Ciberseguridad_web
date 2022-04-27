"""This module provides a serie of ML ALgorithms"""
import joblib
import sklearn

def loadDecisionTreeClassifier(dtcModelRoute = "../Modules/DataScience/Models/dtc.save"):
    dtc =  joblib.load(dtcModelRoute)
    return dtc


def loadKNN(knnModelROute = "../Modules/DataScience/Models/knn.save"):
    knn = joblib.load(knnModelROute)
    return knn


def loadRandomForestClassifier(rfcModelRoute = "../Modules/DataScience/Models/rfc.save"):
    rfc = joblib.load(rfcModelRoute)
    return rfc


def loadLogisticRegressionClassifier(logregRoute="../Modules/DataScience/Models/logreg.save"):
    logreg = joblib.load(logregRoute)
    return logreg
