import pickle
import numpy as np

class ModelEvaluator():
    def __init__(self):
        self.model=pickle.load(open("random_forest_v5.pkl", "rb"))
    
    def test(self,var):
        var=np.array(var)
        return self.model.predict(var.reshape(1,-1))

    
