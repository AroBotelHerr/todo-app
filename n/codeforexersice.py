file = open("../old_code/todos.txt", "r")
todos = file.readlines()
file.close()

for index, item in enumerate(todos):
    print(item.strip())


