import pandas
from . import ML_Algorithms
import numpy as np
from scipy import stats
import joblib




def RandomForestClassifierPrediction(routeDataset):
    score = 0
    print("::::::::::::::::::::::::::::")
    print(":::: GENERATING PREDICTION WITH RANDOM FOREST CLASSIFIER...... ::::")
    print("::::::::::::::::::::::::::::")
    rfc = ML_Algorithms.loadRandomForestClassifier()
    dataset = pandas.read_csv(routeDataset, delimiter=",")
    dataset = standarize(dataset)
    dataset = EDA(dataset)
    dataset = convertProtocols(dataset)
    print("::::::::::::::::::::::::::::")
    print(":::: DATASET GENERATED....... ::::")
    print("::::::::::::::::::::::::::::")
    print(dataset.head())
    y_pred = rfc.predict(dataset)
    print("::::::::::::::::::::::::::::")
    print(":::: TIME WINDOWS PREDICTION....... ::::")
    print("::::::::::::::::::::::::::::")
    print(y_pred)
    if 1 in y_pred:
        score = 1
    return score

def KNNPrediction(routeDataset):
    score = 0
    print("::::::::::::::::::::::::::::")
    print(":::: GENERATING PREDICTION WITH GAUSSIAN NAIVE BAYES...... ::::")
    print("::::::::::::::::::::::::::::")
    knn = ML_Algorithms.loadKNN()
    dataset = pandas.read_csv(routeDataset, delimiter=",")
    dataset = standarize(dataset)
    dataset = EDA(dataset)
    dataset = convertProtocols(dataset)
    print("::::::::::::::::::::::::::::")
    print(":::: DATASET GENERATED....... ::::")
    print("::::::::::::::::::::::::::::")
    print(dataset.head())
    y_pred = knn.predict(dataset)
    print("::::::::::::::::::::::::::::")
    print(":::: TIME WINDOWS PREDICTION....... ::::")
    print("::::::::::::::::::::::::::::")
    print(y_pred)
    if 1 in y_pred:
        score = 1
    return score

def decisionTreeClassifier(routeDataset):
    score = 0
    print("::::::::::::::::::::::::::::")
    print(":::: GENERATING PREDICTION WITH DECISION TREE CLASSIFIER...... ::::")
    print("::::::::::::::::::::::::::::")
    dtc = ML_Algorithms.loadDecisionTreeClassifier()
    dataset = pandas.read_csv(routeDataset, delimiter=",")
    dataset = standarize(dataset)
    dataset = EDA(dataset)
    dataset = convertProtocols(dataset)
    print("::::::::::::::::::::::::::::")
    print(":::: DATASET GENERATED....... ::::")
    print("::::::::::::::::::::::::::::")
    print(dataset.head())
    y_pred = dtc.predict(dataset)
    print("::::::::::::::::::::::::::::")
    print(":::: TIME WINDOWS PREDICTION....... ::::")
    print("::::::::::::::::::::::::::::")
    print(y_pred)
    if 1 in y_pred:
        score = 1
    return score

def logisticRegression(routeDataset):
    score = 0
    print("::::::::::::::::::::::::::::")
    print(":::: GENERATING PREDICTION WITH LOGISTIC REGRESSION...... ::::")
    print("::::::::::::::::::::::::::::")
    logreg = ML_Algorithms.loadLogisticRegressionClassifier()
    dataset = pandas.read_csv(routeDataset, delimiter=",")
    dataset = standarize(dataset)
    dataset = EDA(dataset)
    dataset = convertProtocols(dataset)
    print("::::::::::::::::::::::::::::")
    print(":::: DATASET GENERATED....... ::::")
    print("::::::::::::::::::::::::::::")
    print(dataset.head())
    y_pred = logreg.predict(dataset)
    print("::::::::::::::::::::::::::::")
    print(":::: TIME WINDOWS PREDICTION....... ::::")
    print("::::::::::::::::::::::::::::")
    print(y_pred)
    if 1 in y_pred:
        score = 1
    return score




def EDA(dataset):
    dt = dataset
    dt = dt[['Avg_bps', 'Avg_pps', 'Bytes', 'p2_ib', 'number_sp'
        , 'First_Protocol', 'number_dp', 'duration', 'first_sp', 'p1_ib', 'Netflows'
        , 'p3_ib', 'p3_d']]
    return dt

def convertProtocols(dataset):

    dt = dataset
    dt['First_Protocol'] = dt['First_Protocol'].replace(np.nan, "None", regex=True)
    #dt['Second_Protocol'] = dt['Second_Protocol'].replace(np.nan, "None", regex=True)

    le = joblib.load("../Modules/DataScience/Tools/label_encoder_first_protocol.encoder")
    dt.First_Protocol = le.transform(dt.First_Protocol)

    #le = joblib.load("../Modules/DataScience/Tools/label_encoder_second_protocol.encoder")
    #dt.Second_Protocol = le.transform(dt.Second_Protocol)

    return dt

def standarize(dataset):
    dt = dataset
    rs = joblib.load("../Modules/DataScience/Tools/scaler.save")
    dt[['Netflows','p1_d', 'p2_d', 'p3_d', 'duration', 'max_d', 'min_d', 'packets','Avg_bps', 'Avg_pps', 'Avg_bpp', 'Bytes', 'number_sp', 'number_dp','p1_ip', 'p2_ip', 'p3_ip', 'p1_ib', 'p2_ib', 'p3_ib']] = rs.transform(dt[['Netflows','p1_d', 'p2_d','p3_d','duration', 'max_d','min_d', 'packets','Avg_bps','Avg_pps','Avg_bpp', 'Bytes','number_sp','number_dp','p1_ip','p2_ip','p3_ip','p1_ib','p2_ib', 'p3_ib']])
    return dt