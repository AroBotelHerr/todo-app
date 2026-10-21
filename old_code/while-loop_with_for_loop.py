todos = []

while True:
    user_action = input("Type add or show, or exit:  ")

    #This code below get rid of the spaces in input of user
    user_action = user_action.strip()
    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "show":
            for item in todos:
                print(item)

        case "exit":
            print("Goodbye")
        case something:
            print("wrong value")

            break


