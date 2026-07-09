import pickle

record = []

while True:
    data = {
        "name": input("enter your name:"),
        "age": int(input("enter  your age :")),
        "course": input("enter your course:")
    }
    record.append(data)
    
    if input("Add more record ? (y/n)") != 'y':
        break


with open("mehul1.pkl", "wb") as file:
    pickle.dump(record, file)


with open("mehul1.pkl", "rb") as file:
    load_data = pickle.load(file)

print(load_data)
