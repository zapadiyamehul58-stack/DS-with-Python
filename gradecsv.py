import pandas as pd
data=[]
while True:
    name=input("Enter Your Name :")
    m1 = float(input("Enter marks of Subject 1: "))
    m2 = float(input("Enter marks of Subject 2: "))
    m3 = float(input("Enter marks of Subject 3: "))

    total=m1+m2+m3
    avg = (m1 + m2 + m3) / 3

    if 0<= total <= 300 and m1<=100 and m2<=100 and m3<=100:

        print("Average Marks:", avg)
        if avg >= 90:
            g="Grade: A"
        elif avg >= 75:
            g="Grade: B"
        elif avg >= 60:
            g="Grade: C"
        else:
            g="Grade: D"

    else :
            print("Invalild Mark!!, Plis Enter Correct Mark")
            
    data.append([name,m1,m2,m3,total,avg,g])


    df=pd.DataFrame(data,columns=["Name","Sub1","Sub2","Sub3","Total","Avarge","Grade"])
    yash=df.to_csv("yash.csv")

    next_choice=input("Enter Value Again? (yes/no)")
    if next_choice == 'no':
        break


    

    
   


