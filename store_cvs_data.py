import pandas as pd

# 50 records formatted as a list of dictionaries
raw_data = [
    {"ID": 1, "Name": "John Doe", "Salary": 65000, "City": "New York"},
    {"ID": 2, "Name": "Jane Smith", "Salary": 72000, "City": "Los Angeles"},
    {"ID": 3, "Name": "Michael Brown", "Salary": 58000, "City": "Chicago"},
    {"ID": 4, "Name": "Emily Davis", "Salary": 85000, "City": "Houston"},
    {"ID": 5, "Name": "David Wilson", "Salary": 90000, "City": "Phoenix"},
    {"ID": 6, "Name": "Sarah Miller", "Salary": None, "City": "Philadelphia"},
    {"ID": 7, "Name": "James Taylor", "Salary": 110000, "City": "San Antonio"},
    {"ID": 8, "Name": "Linda Anderson", "Salary": 62000, "City": "San Diego"},
    {"ID": 9, "Name": "Robert Thomas", "Salary": 78000, "City": "Dallas"},
    {"ID": 10, "Name": "Barbara Jackson", "Salary": 95000, "City": "San Jose"},
    {"ID": 11, "Name": "William White", "Salary": 52000, "City": "Austin"},
    {"ID": 12, "Name": "Mary Harris", "Salary": 67000, "City": "Jacksonville"},
    {"ID": 13, "Name": "Anthony Martin", "Salary": 81000, "City": "Fort Worth"},
    {"ID": 14, "Name": "Patricia Thompson", "Salary": 74000, "City": "Columbus"},
    {"ID": 15, "Name": "Charles Garcia", "Salary": 60000, "City": "Charlotte"},
    {"ID": 16, "Name": "Jennifer Martinez", "Salary": 105000, "City": "San Francisco"},
    {"ID": 17, "Name": "Christopher Robinson", "Salary": 88000, "City": "Indianapolis"},
    {"ID": 18, "Name": "Elizabeth Clark", "Salary": 55000, "City": "Seattle"},
    {"ID": 19, "Name": "Matthew Rodriguez", "Salary": 70000, "City": "Denver"},
    {"ID": 20, "Name": "Susan Lewis", "Salary": 92000, "City": "Washington"},
    {"ID": 21, "Name": "Mark Lee", "Salary": 63000, "Boston": "Boston"},
    {"ID": 22, "Name": "Jessica Walker", "Salary": None, "City": "El Paso"},
    {"ID": 23, "Name": "Donald Hall", "Salary": 51000, "City": "Nashville"},
    {"ID": 24, "Name": "Sarah Allen", "Salary": 83000, "City": "Detroit"},
    {"ID": 25, "Name": "Paul Young", "Salary": 120000, "City": "Oklahoma City"},
    {"ID": 26, "Name": "Karen King", "Salary": 66000, "City": "Portland"},
    {"ID": 27, "Name": "Steven Wright", "Salary": 71000, "City": "Las Vegas"},
    {"ID": 28, "Name": "Nancy Scott", "Salary": 59000, "City": "Memphis"},
    {"ID": 29, "Name": "Andrew Torres", "Salary": 86000, "City": "Louisville"},
    {"ID": 30, "Name": "Lisa Nguyen", "Salary": 94000, "City": "Baltimore"},
    {"ID": 31, "Name": "Kevin Hill", "Salary": 53000, "City": "Milwaukee"},
    {"ID": 32, "Name": "Betty Flores", "Salary": 68000, "City": "Albuquerque"},
    {"ID": 33, "Name": "Brian Green", "Salary": 76000, "City": "Tucson"},
    {"ID": 34, "Name": "Helen Adams", "Salary": 102000, "City": "Fresno"},
    {"ID": 35, "Name": "George Nelson", "Salary": 49000, "City": "Sacramento"},
    {"ID": 36, "Name": "Sandra Baker", "Salary": 84000, "City": "Kansas City"},
    {"ID": 37, "Name": "Edward Hall", "Salary": 91000, "City": "Mesa"},
    {"ID": 38, "Name": "Donna Rivera", "Salary": 57000, "City": "Atlanta"},
    {"ID": 39, "Name": "Ronald Campbell", "Salary": 73000, "City": "Omaha"},
    {"ID": 40, "Name": "Carol Mitchell", "Salary": 64000, "City": "Colorado Springs"},
    {"ID": 41, "Name": "Edward Carter", "Salary": 80000, "City": "Raleigh"},
    {"ID": 42, "Name": "Ruth Roberts", "Salary": 97000, "City": "Long Beach"},
    {"ID": 43, "Name": "Sharon Gomez", "Salary": 46000, "City": "Virginia Beach"},
    {"ID": 44, "Name": "Michelle Ortiz", "Salary": 89000, "City": "Miami"},
    {"ID": 45, "Name": "Laura Stewart", "Salary": 61000, "City": "Oakland"},
    {"ID": 46, "Name": "Daniel Morris", "Salary": 75000, "City": "Minneapolis"},
    {"ID": 47, "Name": "Kimberly Nguyen", "Salary": 115000, "City": "Tulsa"},
    {"ID": 48, "Name": "Joshua Murphy", "Salary": 54000, "City": "Wichita"},
    {"ID": 49, "Name": "Margaret Rivera", "Salary": 69000, "City": "New Orleans"},
    {"ID": 50, "Name": "David Cook", "Salary": 82000, "City": "Arlington"}
]

df = pd.DataFrame()

df.reset_index(drop=True).to_csv("clean1.csv", index=False)

print("--- Stored Data ---")
