import numpy as np
from tensorflow.keras.models import Sequential # type: ignore
from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPooling2D # type: ignore

def load_mnist_images(filename):
    with open(filename, 'rb') as f:
        f.read(16)
        data = np.frombuffer(f.read(), dtype=np.uint8)
    return data.reshape(-1, 28, 28)

def load_mnist_labels(filename):
    with open(filename, 'rb') as f:
        f.read(8)
        labels = np.frombuffer(f.read(), dtype=np.uint8)
    return labels

training_data = load_mnist_images("./training_data")
training_labels = load_mnist_labels("./training_labels")
test_data = load_mnist_images("./test_data")
test_labels = load_mnist_labels("./test_labels")

model = Sequential([
    Conv2D(32, (3,3), activation='relu', input_shape=(28,28,1)),  
    MaxPooling2D(2,2),  
    Conv2D(64, (3,3), activation='relu'),  
    MaxPooling2D(2,2),  
    Flatten(),  
    Dense(128, activation='relu'),  
    Dense(10, activation='softmax')  
])

model.compile(
    optimizer='adam', 
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)
history = model.fit(training_data, training_labels, epochs=25, batch_size=32, validation_split=0.2)
loss, accuracy = model.evaluate(test_data, test_labels)
print(f"Test Accuracy: {accuracy * 100:.2f}%")

model.save('mnist_digits.keras')