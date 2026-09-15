import pandas as pd 
import numpy as np 

from load_data import load_matches
from features import create_features
from linear_regression import LinearRegression 

matches = load_matches()
features = create_features(matches)

df = pd.DataFrame(features)


#finding out difference between a teams away performance and home performance 
df["win_diff"] = (
    df["home_wins"] - df["away_wins"]
)


X = df["win_diff"].to_numpy()

y = matches["FTHG"].to_numpy()


# Split the data into training and testing 
# 80% is training 

split = int(len(X) * 0.8)
X_train = X[:split]
X_test = X[split:]

y_train = y[:split]
y_test = y[split:]

print("Traning Matches: ", len(X_train))
print("Testing Matches: ", len(X_test))




#the linear regression 

model = LinearRegression(
    learning_rate=0.001, 
    epochs=1000
)

loss_history = model.fit(X_train, y_train)

predictions = model.predict(X_test)

errors = predictions - y_test 

mae = np.mean(np.abs(errors))
mse = np.mean(errors**2)
rmse = np.sqrt(mse)

print("-----MODEL OUTPUT-----")
print("Weight:", model.w)
print("Bias:", model.b)

print("-----Final Training Loss-----")
print(loss_history[-1])

print("-----Testing Results-----")
print("MAE: ", mae)
print("MSE: ", mse)
print("RMSE: ", rmse)


'''
def predict(x, m,b):
    return m * x + b 


def mean(values):
    return sum(values) / len(values)

def std(values):
    avg = mean(values)

    total = 0 
    for v in values: 
        total += (v - avg) ** 2 

    return math.sqrt(total / len(values))


numerator = 0
denominator = 0 

for x, actual_y in zip(X,y):
    numerator += (x - x_mean) * (actual_y - y_mean)

    denominator += (x - x_mean) ** 2 

m = numerator/denominator 

b = y_mean - m * x_mean 

print("Slope: ", m)
print("Intercept: ", b)


predictions = []

for x in X:
    prediction = predict(x, m,b)
    predictions.append(prediction)


print("\n First 10 predictions: ")

for actual, predicted in zip(y[:10], predictions[:10]):
    print(f"Actual: {actual} | Predicted: {predicted:.2f}")
'''