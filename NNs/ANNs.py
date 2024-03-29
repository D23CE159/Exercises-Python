import numpy as np
from keras.models import Sequential
from keras.layers import Dense

# Sample dataset
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

# Define the neural network architecture
model = Sequential()
model.add(Dense(4, input_dim=2, activation='relu'))  # Hidden layer with 4 neurons and ReLU activation
model.add(Dense(1, activation='sigmoid'))           # Output layer with 1 neuron and Sigmoid activation

# Compile the model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model
model.fit(X, y, epochs=1000, batch_size=4)

# Predictions
predictions = model.predict(X)
print(predictions)
