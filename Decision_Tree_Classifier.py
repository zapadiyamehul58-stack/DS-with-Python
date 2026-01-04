from sklearn.tree import DecisionTreeClassifier

X = [[4,0], [4,1], [2,2]]
y = [0, 1, 2]

model = DecisionTreeClassifier()
model.fit(X, y)

new_data = [[2,1]]
prediction = model.predict(new_data)

animals = {0: "Dog", 1: "Cat", 2: "Parrot"}
print("Prediction:", animals[prediction[0]])
