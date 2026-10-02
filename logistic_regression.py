import numpy as np 
import pandas as pd 


def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def cost_function(X, y, w, b):
    cost_sum = 0 

    for i in range(m):
        z = np.dot(w, X[i] + b)
        g = sigmoid(z)

        cost_sum += -y[i] * np.log(g) - (1 - y[i]) * np.log(1 - g)

    return (1/m) * cost_sum 






