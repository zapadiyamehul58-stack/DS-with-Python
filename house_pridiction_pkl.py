from sklearn.linear_model import LinearRegression
import pandas as pd
import pickle
df = pd.read_csv("H:\sem 5\DS\data.csv")
df=pd.DataFrame(df)

model=LinearRegression()

model.fit(df[['sqft_living']],df['price'])
pickle.dump(model,open('house.pkl','wb'))
model=pickle.load(open('house.pkl','rb'))
new_data=pd.DataFrame({'sqft_living':[2020,3500]})
print(model.predict(new_data))

