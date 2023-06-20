from tensorflow import keras
from keras.models import load_model
import numpy as np

class ModelEvaluator():
    def __init__(self):
        self.model=load_model('deep_mal_v8.h5')
    
    def test(self,var):
        var=np.array(var)
        return self.model.predict(var.reshape(1,-1))
    


    
