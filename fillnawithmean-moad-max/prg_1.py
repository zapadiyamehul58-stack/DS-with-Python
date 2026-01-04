import pandas as pd

#Read Data
df=pd.read_csv("Titanic_dataset.csv")
#Shape The Data
print(df.shape)

#Find The Null Value
null=pd.isnull(df)
#Sum Of Null Value 
n_sum=null.sum()

#For Information 
print(df.info())

#Data Filna With Mode
mode=df["deck"].mode()[0]
df["deck"]=df["deck"].fillna(mode)
print(df["deck"])

#find Mean
mean=df["age"].mean()
print(mean)

#Fillna with Median
median=df["age"].median()
df["age"]=df["age"].fillna(median)
print(df["age"])

#Fillna With Mode
mode=df["embarked"].mode()[0]
df["embarked"]=df["embarked"].fillna(mode)
print(df["embarked"])

#Fillna With Mode
mode=df["embark_town"].mode()[0]
df["embark_town"]=df["embark_town"].fillna(mode)
print(df["embark_town"])


expt=df.to_csv("Titanic_dataset.csv")















