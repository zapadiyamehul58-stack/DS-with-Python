def get_student_info():
    name = input("Enter Student Name: ")
    stream = input("Enter Stream: ")
    college = input("Enter College Name: ")
    division = input("Enter Division: ")

    print("\n--- Student Details ---")
    print(f"Name: {name}")
    print(f"Stream: {stream}")
    print(f"College: {college}")
    print(f"Division: {division}")

get_student_info()
