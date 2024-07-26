# Import necessary libraries
import numpy as np

# Activation function: Sigmoid
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivative of the sigmoid function
def sigmoid_derivative(x):
    return x * (1 - x)

# Mean squared error loss function
def mean_squared_error(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

# Initialize the neural network
class NeuralNetwork:
    def __init__(self, input_size, hidden_size1, hidden_size2, output_size):
        self.weights_input_hidden1 = np.random.randn(input_size, hidden_size1)
        self.weights_hidden1_hidden2 = np.random.randn(hidden_size1, hidden_size2)
        self.weights_hidden2_output = np.random.randn(hidden_size2, output_size)
        self.learning_rate = 0.1

    def forward(self, X):
        self.input = X
        self.hidden1 = sigmoid(np.dot(self.input, self.weights_input_hidden1))
        self.hidden2 = sigmoid(np.dot(self.hidden1, self.weights_hidden1_hidden2))
        self.output = sigmoid(np.dot(self.hidden2, self.weights_hidden2_output))
        return self.output

    def backward(self, X, y, output):
        self.output_error = y - output
        self.output_delta = self.output_error * sigmoid_derivative(output)
        
        self.hidden2_error = self.output_delta.dot(self.weights_hidden2_output.T)
        self.hidden2_delta = self.hidden2_error * sigmoid_derivative(self.hidden2)
        
        self.hidden1_error = self.hidden2_delta.dot(self.weights_hidden1_hidden2.T)
        self.hidden1_delta = self.hidden1_error * sigmoid_derivative(self.hidden1)
        
        self.weights_hidden2_output += self.hidden2.T.dot(self.output_delta) * self.learning_rate
        self.weights_hidden1_hidden2 += self.hidden1.T.dot(self.hidden2_delta) * self.learning_rate
        self.weights_input_hidden1 += self.input.T.dot(self.hidden1_delta) * self.learning_rate

    def train(self, X_train, y_train, X_val, y_val, epochs):
        for epoch in range(epochs):
            output = self.forward(X_train)
            self.backward(X_train, y_train, output)
            if (epoch % 1000) == 0:
                train_loss = mean_squared_error(y_train, output)
                val_loss = mean_squared_error(y_val, self.forward(X_val))
                print(f"Epoch {epoch}, Train Loss: {train_loss}, Validation Loss: {val_loss}")

# Define input data and corresponding output
X = np.array([[0, 0, 1],
            [1, 1, 1],
            [1, 0, 1],
            [0, 1, 1]])

y = np.array([[0],
            [1],
            [1],
            [0]])

# Split the data into training and validation sets
X_train, X_val = X[:3], X[3:]
y_train, y_val = y[:3], y[3:]

# Initialize the neural network
nn = NeuralNetwork(input_size=3, hidden_size1=4, hidden_size2=4, output_size=1)

# Train the neural network
nn.train(X_train, y_train, X_val, y_val, epochs=10000)

# Test the trained neural network
def predict(input_data):
    return nn.forward(input_data)

# Test with a new example
new_example = np.array([[1, 0, 0]])
predicted_output = predict(new_example)
print(f"Predicted output for {new_example}: {predicted_output}")
