import pandas as pd 
import math

from load_data import load_matches
from features import create_features


matches = load_matches()
features = create_features(matches)

df = pd.DataFrame(features)


#finding out difference between a teams away performance and home performance 
df["win_diff"] = (
    df["home_wins"] - df["away_wins"]
)


X = df["win_diff"].tolist()

y = matches["FTHG"].tolist()

#the linear regression 

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

'''
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