"""
members = ["john", "sarah", "dora"]

for member in members:
    print(member.capitalize())


country = ["USA", "Germany", "italy"]


while True:

    user_input = input("Enter a country name: ")

    match user_input:
        case "USA" | "United States":
            print("Hello")

        case _:
            print("Invalid input")
            break

employees = ["john smith", "sarah bremen", "dora dawson"]


for employee in employees:
    print(employee.title())



user_action = input("Type add or show: ")


match user_action.strip():

    case "add":
        print("Adding a todo)
    case "show":
        print("Showing the todos")
    case _:
        print("Command is not valid.")
"""
todos = ["clean", "throw", "meet Tom"]

for item in todos:
    print(item)


