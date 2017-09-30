import unittest
from controller import user_command, print_usage, list_todos

tested_file = "controller.py"

class TestUserCommand(unittest.TestCase):

    def test_user_command_empty(self):
        self.assertEqual(user_command(), print_usage())


    def test_user_command_list(self):
        self.arguments = [tested_file, "-l"]
        self.assertEqual(user_command(), list_todos())


    def test_user_command_add_task_index_not_specified(self):
        self.arguments = [tested_file, "-a"]
        self.assertEqual(user_command(), print("Unable to add: no task provided"))
        

if __name__ == "__main__":
    unittest.main()
