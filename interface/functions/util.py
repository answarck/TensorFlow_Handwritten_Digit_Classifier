import tensorflow as tf
import json 
import numpy as np

model = tf.keras.models.load_model("../training/mnist_digits.keras")

def predict(json_data):
    input_data = np.array(json.loads(json_data)).astype(np.float32).reshape((1, 28, 28))
    input_data *= 225
    prediction = np.argmax(model.predict(input_data))
    return int(prediction)