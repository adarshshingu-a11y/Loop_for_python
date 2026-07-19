while True:
    print("\n===== Student Report Card System =====")
    print("1. Add Student")
    print("2. Show Report")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Name: ")
        age = input("Age: ")

        math = int(input("Math: "))
        science = int(input("Science: "))
        hindi = int(input("Hindi: "))
        sanskrit = int(input("Sanskrit: "))
        computer = int(input("Computer: "))

        total = math + science + hindi + sanskrit + computer
        average = total / 5

        with open("report.txt", "a") as f:
            f.write("Name: " + name + "\n")
            f.write("Age: " + age + "\n")
            f.write("Math: " + str(math) + "\n")
            f.write("Science: " + str(science) + "\n")
            f.write("Hindi: " + str(hindi) + "\n")
            f.write("Sanskrit: " + str(sanskrit) + "\n")
            f.write("Computer: " + str(computer) + "\n")
            f.write("Total: " + str(total) + "\n")
            f.write("Average: " + str(average) + "\n")
            f.write("-------------------------\n")

        print("Student Report Saved Successfully!")

    elif choice == "2":
        with open("report.txt", "r") as f:
            data = f.read()
            print(data)

    elif choice == "3":
        print("Program Closed.")
        break

    else:
        print("Invalid Choice! Try Again.")
