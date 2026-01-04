from sklearn.tree import DecisionTreeClassifier

from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)

model = DecisionTreeClassifier()
model.fit(X, y)

new_data = [[5.8, 2.7, 5.1, 1.9]]
prediction = model.predict(new_data)

labels = {0: "Setosa", 1: "Versicolor", 2: "Virginica"}
print("Prediction:", labels[prediction[0]])

