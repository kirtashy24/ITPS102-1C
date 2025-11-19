import os
print("=====================================================")
print("DALUBHASAAN NG LUNGSOD NG LUCENA - INFORMATION SYSTEM")
print("=====================================================")

llist = {}

while True:
    print("A - Adding Student Record")
    print("B - Search Student")
    print("C - Edit Stdent Record")
    print("D - Delete Student Record")
    print("E - Print All Record")
    print("F - Export Data")
    print("G - Exit System")

    choice = input("What do you want to do? ").lower().strip()
    
    if choice == "a":
        os.system("cls")
        print("Add a student record")
        student_id = input("Enter Student Student ID ▶ ")
        first_name = input("Enter Student First Name ▶ ").upper()
        last_name = input("Enter Student Last Name ▶ ").upper()
        course = input("Enter Student Course ▶ ").upper()
        section = input("Enter Student Section ▶ ").upper()
        email = input("Enter Student Email ▶ ")

        llist[student_id] = [first_name, last_name, course, section, email]
        print("DATA SAVED SUCCESSFULLY")

        continue

    elif choice == ("b"):
        os.system("cls")
        print("Printing Student Record")
        print("◌ ◌ ◌")
        
        for id,info in llist.items():
            print(f"Student ID {id} - Record - {info}")

        continue

    elif choice == ("c"):
        print(" Student Record")

    elif choice == ("d"):
        print(" Student Record")

    elif choice == ("e"):
        print(" Student Record")

    elif choice == ("f"):
        print(" Student Record")

    elif choice == ("g"):
        print("Goodbye")