import numpy as np 

X = np.array([1,2,3,4,5])
y = np.array([3,5,7,9,11])

w = 0 
b = 0 

learning_rate = 0.01 
epochs = 1000 

for epoch in range(epochs):

    y_pred = w * X + b 
    error = y_pred - y 


    #mean squared error calcualtion 
    mse = np.mean(error**2)


    #gradient 
    dw = (2/len(X)) * np.sum(X*error)
    db = (2/len(X)) * np.sum(error)


    #graident descent 
    w = w - learning_rate * dw 
    b = b - learning_rate * db 


print(w)
print(b)