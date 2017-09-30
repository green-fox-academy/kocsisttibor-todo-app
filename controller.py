import sys
from commands import list_todos, add_todo, remove_todo_error_handling, complete_todo_error_handling

def get_arguments():
    return sys.argv


def print_usage():
    print(str("\n\
    \nCommand Line Todo application\
    \n=============================\n\
    \nCommand line arguments:\
    \n-l   Lists all the tasks\
    \n-a   Adds a new task e.g.: -a 'New task'\
    \n-r   Removes a task e.g.: -r 4\
    \n-c   Completes a task e.g.: -c 4"))


def user_command():
    arguments = get_arguments()
    try:
        if len(arguments) == 1:
            print_usage()
        elif len(arguments) == 2 and arguments[1] == "-l":
            list_todos()
        elif len(arguments) == 2 and arguments[1] == "-a":
            print("Unable to add: no task provided")
        elif len(arguments) == 3 and arguments[1] == "-a":
            add_todo(arguments[2])
        elif len(arguments) == 2 and arguments[1] == "-r":
            print("Unable to remove: no index provided")
        elif len(arguments) == 3 and arguments[1] == "-r":
            remove_todo_error_handling(arguments[2])
        elif len(arguments) == 2 and arguments[1] == "-c":
            print("Unable to check: no index provided")
        elif len(arguments) == 3 and arguments[1] == "-c":
            complete_todo_error_handling(arguments[2])
        else:
            print("\nNot proper arguments given. Please check the available arguments.")
            print_usage()
    except ValueError:
        print("Not proper arguments given. Please check the available arguments.")
        print_usage()

user_command()
