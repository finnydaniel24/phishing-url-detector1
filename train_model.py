import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle
from feature_extraction import extract_features

data = pd.read_csv("dataset.csv")

X = []
y = []

for i in range(len(data)):
    url = data['url'][i]
    label = data['label'][i]

    features = extract_features(url)

    X.append(features)
    y.append(label)

model = RandomForestClassifier()
model.fit(X, y)

pickle.dump(model, open("model.pkl", "wb"))

print("Model trained successfully!")
