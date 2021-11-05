import os
import numpy as np
import subprocess
from sklearn.metrics import f1_score, accuracy_score
from .utils_model import *

def predict():
    os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID" 
    os.environ["CUDA_VISIBLE_DEVICES"] = "0"

    data_dir = "media/audios/"
    mode = "unlabeled"  # real, fake, or unlabeled
    pretrained_model_name = 'FinalModel.h5'
    print(f"Loading inference data from {os.path.join(data_dir,mode)}")
    print(f"Loading pretrained model {pretrained_model_name}")

    # preprocess the files
    processed_data = preprocess_from_ray_parallel_inference(
        data_dir, mode, use_parallel=False)
    processed_data = sorted(processed_data, key=lambda x: len(x[0]))

    # Load trained model
    discriminator = Discriminator_Model(
        load_pretrained=True, saved_model_name=pretrained_model_name, real_test_mode=False)

    # Do inference
    if mode == 'unlabeled':

        print("The probability of the clip being real is: {:.2%}".format(
            discriminator.predict_labels(processed_data, raw_prob=True, batch_size=20)[0][0]))
        
        return round(discriminator.predict_labels(processed_data, raw_prob=True, batch_size=20)[0][0], 3)


