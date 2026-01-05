from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder  

x = [
    [4, 30],
    [4, 25],
    [2, 2],
    [2, 1],
    [0, 5]
]
y = ['dog', 'cat', 'duck', 'bird', 'snack']

le = LabelEncoder()
y_encoded = le.fit_transform(y) 

knn = KNeighborsClassifier(n_neighbors=1) 
knn.fit(x, y_encoded)  

test_data = [[4,25]]
predict = knn.predict(test_data)

animal = le.inverse_transform(predict)  
print("Predicted animal is:", animal[0])
