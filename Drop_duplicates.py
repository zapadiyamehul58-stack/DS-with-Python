import pandas as pd

data = pd.read_csv('data.csv')

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Remove all duplicates recodes
df_unique = df.drop_duplicates()

print("\nAfter removing duplicates:")
print(df_unique)

# Subset parameter in drop_duplicates() method

df_cleaned1 = data.drop_duplicates(subset=["Id"]) # drop using single column
print(df_cleaned1,"\n")

df_cleaned2 = data.drop_duplicates(subset=["Id","Department"]) # drop using multiple columns
print(df_cleaned2,"\n")

df_cleaned3= data.drop_duplicates(subset=["Department","Id"]) # drop using multiple columns with different order
print(df_cleaned3,"\n")

# Keep parameter in drop_duplicates() method

df_cleaned3= df.drop_duplicates(keep="first") # keep first occurrence of duplicate
print(df_cleaned3,"\n\n")

df_cleaned5= df.drop_duplicates(keep="last") # keep last occurrence of duplicate
print(df_cleaned5,"\n\n")

df_cleaned6= df.drop_duplicates(keep=False) # drop all duplicates
print(df_cleaned6,"\n\n")

# inplace parameter in drop_duplicates() method

df.drop_duplicates(inplace=True) # modify the original dataframe
print("After removing duplicates inplace:",df)  