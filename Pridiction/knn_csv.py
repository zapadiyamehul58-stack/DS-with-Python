from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder  
import pandas as pd
data=pd.read_csv("knn.csv")

X=data[['leg','wieght']]

y = data['nm']

le = LabelEncoder()
y_encoded = le.fit_transform(y) 

knn = KNeighborsClassifier(n_neighbors=3) 
knn.fit(X, y_encoded)  

test_data = [[4,25]]
predict = knn.predict(test_data)

animal = le.inverse_transform(predict)  
print("Predicted animal is:", animal[0])
