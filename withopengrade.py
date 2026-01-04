#writing CSV File
import csv

no=int(input("Enter Total Student No  :"))

with open ("yash.csv","w",newline="")as f:

    for i in range (no):
        name=input(f"Enter Student Name :")
        m1=int(input(f"Enter {name} Os Mark  :"))
        m2=int(input(f"Enter {name} Php Mark :"))
        m3=int(input(f"Enter {name} Python Mark :"))
        index=i

        total=m1+m2+m3
        avg = (m1 + m2 + m3) / 3


        if avg >= 90:
            grade=("Grade: A")
        elif avg >= 75:
            grade=("Grade: B")
        elif avg >= 60:
            grade=("Grade: C")
        else:
            grade=("Grade: D")

        

        write=csv.writer(f)
        write.writerow([index,name,m1,m2,m3,total,avg,grade])

"""#Reading CSV File
import csv
with open("yash.csv","r")as f:
    read=csv.reader(f)

    for row in read:
        print(row)"""
