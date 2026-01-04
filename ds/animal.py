import pandas as pd
from sklearn.tree import DecisionTreeClassifier

data=pd.read_csv("aa.csv")

X=data[['leg','fly']]
y=data[['type']]
       
model=DecisionTreeClassifier()
model.fit(X,y)
       
leg=int(input("enter legs:"))
fly=int(input("cat fly ?:"))

result=model.predict([[leg,fly]])
print("pridiction :",result[0])
