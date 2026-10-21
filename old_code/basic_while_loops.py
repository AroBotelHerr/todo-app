todos = []

while 2 > 1:
    todo = input("Enter a todo: ")
    todos.append(todo)
    print(todos)

user_prompt = "Enter a todo:"

todos = []

while True:
    todo = input(user_prompt)
    print(todo.capitalize())
    todos.append(todo)
