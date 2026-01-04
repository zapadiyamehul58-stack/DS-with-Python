import pandas as pd

# Take input from user
math = float(input("Enter marks in Math: "))
science = float(input("Enter marks in Science: "))
english = float(input("Enter marks in English: "))

# Validate marks
if (math > 100 or math < 0) or (science > 100 or science < 0) or (english > 100 or english < 0):
    print("Subject marks should be between 0 and 100")
else:
    # Calculate average
    average = (math + science + english) / 3

    # Determine grade
    if average >= 90:
        grade = 'A'
    elif average >= 75:
        grade = 'B'
    elif average >= 60:
        grade = 'C'
    elif average >= 40:
        grade = 'D'
    else:
        grade = 'F'

    # Display results
    print(f"\nAverage Marks: {average:.2f}")
    print(f"Grade: {grade}")

    # Create DataFrame
    df = pd.DataFrame({
        'Math': [math],
        'Science': [science],
        'English': [english],
        'Average': [average],
        'Grade': [grade]
    })

    # Save (overwrite) CSV
    df.to_csv("student_grades.csv", index=False)

    # Read the CSV and display
    saved_data = pd.read_csv("student_grades.csv")
    print("\nData saved successfully!\n")
    print(saved_data)
