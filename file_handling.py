database = "todos.txt"

def open_database():
    with open(database) as f:
        content = f.read().splitlines()
        todos = []
        if content[0] != "":        # empty file results []
            for line in content:
                if line[1] == "X":
                    todos.append(["1",line[4:]])
                else:
                    todos.append(["0", line[4:]])
    return todos


def save_database(todos):
    with open(database, "w") as f:
        for todo in todos:
            if todo[0] == "0":
                line = "[ ] " + todo[1] + "\n"
            else: 
                line = "[X] " + todo[1] + "\n"
            f.write(line)
