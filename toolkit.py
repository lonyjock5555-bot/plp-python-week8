
# Personal Mini-Toolkit
# A simple program with three useful tools.

def show_menu():
    print("\n=================================")
    print("       PERSONAL MINI-TOOLKIT")
    print("=================================")
    print("1. Simple Calculator")
    print("2. Shopping List")
    print("3. Study Task Manager")
    print("4. Quit")


# Main menu loop
print("Welcome to your Personal Mini-Toolkit!")

while True:
    show_menu()

    choice = input("Enter your choice (1-4): ")


    if choice == "1":
        print("\n--- SIMPLE CALCULATOR ---")

        num1 = float(input("Enter the first number: "))
        operator = input("Enter operation (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                print("Sorry, division by zero is not allowed.")
                continue
        else:
            print("Invalid operation. Please try again.")
            continue

        print(f"The answer is: {result}")



    elif choice == "2":
        print("\n--- SHOPPING LIST ---")

        shopping_list = []

        while True:
            print("\n1. Add item")
            print("2. View items")
            print("3. Back to main menu")

            option = input("Choose an option (1-3): ")

            if option == "1":
                item = input("Enter shopping item: ")
                shopping_list.append(item)
                print(f"{item} has been added to your shopping list.")

            elif option == "2":
                if len(shopping_list) == 0:
                    print("Your shopping list is empty.")
                else:
                    print("\nYour Shopping Items:")
                    for item in shopping_list:
                        print(f"- {item}")

            elif option == "3":
                break

            else:
                print("Invalid option. Please try again.")


    elif choice == "3":
        print("\n--- STUDY TASK MANAGER ---")

        study_tasks = []

        while True:
            print("\n1. Add study task")
            print("2. View study tasks")
            print("3. Back to main menu")

            option = input("Choose an option (1-3): ")

            if option == "1":
                task = input("Enter your study task: ")
                study_tasks.append(task)
                print(f"Task '{task}' has been added successfully.")

            elif option == "2":
                if len(study_tasks) == 0:
                    print("You have no study tasks yet.")
                else:
                    print("\nYour Study Tasks:")
                    for task in study_tasks:
                        print(f"- {task}")

            elif option == "3":
                break

            else:
                print("Invalid option. Please try again.")


    elif choice == "4":
        print("Thank you for using Personal Mini-Toolkit. Goodbye!")
        break

    else:
        print(f"Sorry, '{choice}' is not a valid choice. Please try again.")
