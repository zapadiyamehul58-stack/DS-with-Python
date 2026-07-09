import Pickle
data={
        "name":"mehul",
        "age":19,
        "course":"data science"
        }
with open ("mehul1.pkl","wb") as file:
    pickle.dump(data,file)

with open ("mehul1.pkl","rb") as file:
    load_data=lickle.load(file)
print(load_data)
