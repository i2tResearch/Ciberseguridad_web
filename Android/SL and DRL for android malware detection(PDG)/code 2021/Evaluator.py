import joblib as jb
import numpy as np

class ModelEvaluator():
    def __init__(self):
        self.model=jb.load('rfDefense2021.sav')
    
    def test(self,var):
        var=np.array(var)
        return self.model.predict(var.reshape(1,-1))
    


    
