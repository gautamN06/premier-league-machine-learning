import numpy as np 

class LinearRegression:

    def __init__(self, learning_rate=0.01, epochs=1000):
        self.learning_rate = learning_rate 
        self.epochs = epochs 

        self.w = None 
        self.b = 0 

    def predict(self, X):
        return self.w * X + self.b 

    def fit(self, X, y):
        self.w =0 
        self.b = 0 

        for epoch in range(self.epochs):
            y_pred = self.predict(X)

            error = y_pred - y

            
            dw = (2/len(X)) * np.sum(X*error)
            db = (2/len(X)) * np.sum(error)

            #Gradient descent adjusting weights 
            self.w -= self.learning_rate * dw 
            self.b -= self.learning_rate * db 


