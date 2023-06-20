import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # or any {'0', '1', '2'}
import tensorflow as tf
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.WARN)  # or any {DEBUG, INFO, WARN, ERROR, FATAL}
from tensorflow.keras.layers import *
from tensorflow.keras.models import *
import tensorflow.keras as K

def stack(layers):
    '''
    Using the Functional-API of Tensorflow to build a sequential
    network (stacked layers) from list of layers.
    '''
    layer_stack = None
    for layer in layers:
        if layer_stack is None:
            layer_stack = layer
        else:
            layer_stack = layer(layer_stack)
    return layer_stack

class DeepMALRawPackets:
    def __init__(self, input_size=1024) -> None:
        input_layer = Input(shape=(input_size,1))
        self.model = Model(
            name='DeepMAL-Packets',
            inputs=input_layer,
            outputs=stack([
                input_layer,
                Conv1D(32, 5),
                Conv1D(64, 5),
                MaxPooling1D(8),
                LSTM(200, return_sequences=True),
                Flatten(),
                Dense(200),
                Dense(200),
                Dense(1, activation='sigmoid')
            ])
        )
        
        loss_fn = tf.keras.losses.BinaryCrossentropy()
        
        self.model.compile(
            optimizer='adam',
            loss=loss_fn,
            metrics=[
                tf.keras.metrics.BinaryAccuracy(threshold=0.51),
                #tf.keras.metrics.Accuracy(),
                tf.keras.metrics.Recall(thresholds=0.51),
                tf.keras.metrics.Precision(thresholds=0.51)
            ]
        )
    
class DeepMALRawFlows:
    def __init__(self, input_size=100) -> None:
        input_layer = Input(shape=(input_size, 1, 2))
        self.model = Model(
            name='DeepMAL[-Flows',
            inputs=input_layer,
            outputs=stack([
                input_layer,
                Conv1D(32, 5),
                Flatten(),
                Dense(50),
                Dense(100),
                Dense(1, activation='sigmoid')
            ])
        )
        
        loss_fn = tf.keras.losses.BinaryCrossentropy()
        
        self.model.compile(
            optimizer='adam',
            loss=loss_fn,
            metrics=[tf.keras.metrics.Accuracy(),
                     tf.keras.metrics.Recall(),
                     tf.keras.metrics.Precision()]
        )
    