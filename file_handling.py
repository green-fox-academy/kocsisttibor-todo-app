database = "todos.txt"

def open_database():
    with open(database) as f:
        content = f.read().splitlines()
        todos = []
        if content[0] != "":        # empty file results []
            for line in content:
                todos.append(line)
    return todos


def save_database(todos):
    with open(database, "w") as f:
        for todo in todos:
            f.write(todo + "\n")
