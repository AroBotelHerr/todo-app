def write_todos(file_path, todos_arg):
    with open(file_path, "w") as file:
        file.writelines(todos_arg)

todos = ["clean\n", "throw\n"]

write_todos(todos, "todos.txt")
print("Todos saved!")
