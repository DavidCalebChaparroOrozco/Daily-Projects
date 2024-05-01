# Importing necessary libraries
import numpy as np

class Perceptron:
    def __init__(self, N, alpha=0.1):
        # Initializing weights with random values
        self.W = np.random.randn(N+1) / np.sqrt(N)
        # Setting learning rate
        self.alpha = alpha
    
    def step(self, x):
        # Activation function: step function
        return 1 if x > 0 else 0
    
    def fit(self, X, y, epochs=10):
        # Adding bias term to input data
        X = np.c_[X, np.ones((X.shape[0]))]
        # Training loop over epochs
        for epoch in np.arange(0, epochs):
            # Looping over each data point
            for (x, target) in zip(X, y):
                # Computing prediction
                p = self.step(np.dot(x, self.W))
                # Updating weights if prediction is incorrect
                if p != target:
                    error = p - target
                    self.W += - self.alpha * error * x

    def predict(self, X, addBias=True):
        # Ensuring input is at least 2D
        X = np.atleast_2d(X)
        # Adding bias term if necessary
        if addBias:
            X = np.c_[X, np.ones((X.shape[0]))]
        # Making predictions
        return self.step(np.dot(X, self.W))

# Gate: OR
X_or = np.array([[0,0], [0,1], [1,0], [1,1]])
y_or = np.array([[0], [1], [1], [1]])

# Gate: AND
X_and = np.array([[0,0], [0,1], [1,0], [1,1]])
y_and = np.array([[0], [0], [0], [1]])

# Gate: XOR
X_xor = np.array([[0,0], [0,1], [1,0], [1,1]])
y_xor = np.array([[1], [0], [0], [0]])

# Initializing Perceptron object
p_or = Perceptron(X_or.shape[1], alpha=0.1)
# Training Perceptron for OR gate
p_or.fit(X_or, y_or, epochs=20)

# Initializing Perceptron object
p_and = Perceptron(X_and.shape[1], alpha=0.1)
# Training Perceptron for AND gate
p_and.fit(X_and, y_and, epochs=20)

# Initializing Perceptron object
p_xor = Perceptron(X_xor.shape[1], alpha=0.1)
# Training Perceptron for XOR gate
p_xor.fit(X_xor, y_xor, epochs=20)

# Making predictions and printing results for OR gate
print("OR Gate:")
for (x, target) in zip(X_or, y_or):
    pred = p_or.predict(x)
    print("Result: Inputs = {}; Real Value = {}; Predicted Value = {}".format(x, target[0], pred))

# Making predictions and printing results for AND gate
print("\nAND Gate:")
for (x, target) in zip(X_and, y_and):
    pred = p_and.predict(x)
    print("Result: Inputs = {}; Real Value = {}; Predicted Value = {}".format(x, target[0], pred))

# Making predictions and printing results for XOR gate
print("\nXOR Gate:")
for (x, target) in zip(X_xor, y_xor):
    pred = p_xor.predict(x)
    print("Result: Inputs = {}; Real Value = {}; Predicted Value = {}".format(x, target[0], pred))