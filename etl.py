import pandas as pd

raw_data = [
      {"name": "a", "marks": 85},
    {"name": "b", "marks": None},
    {"name": "c", "marks": 90},
    {"name": "d", "marks": None},
    {"name": "e", "marks": 75},
    {"name": "f", "marks": None},
    {"name": "g", "marks": 95},
    {"name": "h", "marks": 60},
    {"name": "i", "marks": None},
    {"name": "j", "marks": 80},      
    {"name": "k", "marks": 88},
    {"name": "l", "marks": None},
    {"name": "m", "marks": 70},
]


clean_data = []
for record in raw_data:
    if record["marks"] is not None:
        clean_data.append(record)

df = pd.DataFrame(clean_data)
df.to_csv("clean.csv", index=False)


print("--- Stored Data ---")
print(df)
