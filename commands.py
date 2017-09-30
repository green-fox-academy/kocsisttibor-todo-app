from file_handling import open_database, save_database

def list_todos():
    todos = open_database()
    if len(todos) == 0:
        print("\nNo todos for today! :)")
    else:
        print("\nTodos\n")
        for i in range(len(todos)):
            if todos[i][0] == "0":
                print(str(i + 1) + " - [ ]" + todos[i][1])
            else:
                print(str(i + 1) + " - [X]" + todos[i][1])

def add_todo(todo):
    todos = open_database()
    todos.append(["0", todo])
    save_database(todos)


def remove_todo(num):
    todos = open_database()
    todos.remove(todos[int(num) - 1])
    save_database(todos)


def remove_todo_error_handling(num):
    todos = open_database()
    if  isinstance(num, int):
        if len(todos) >= int(num):
            remove_todo(num)
        else:
            print("\nUnable to remove: index is out of bound")
    else:
        print("\nUnable to remove: index is not a number")


def complete_todo(num):
    todos = open_database()
    todos[int(num) - 1][0] = "1"
    save_database(todos)
