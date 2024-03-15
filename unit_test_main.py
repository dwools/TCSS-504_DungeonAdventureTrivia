import unittest

#


"""
Be careful! Line 91 of test_characters.py calls database_names. If test_characters.py changes directories, line 91
mutates from:
conn = sqlite3.connect("Databases/database_names.db")
to:
conn = sqlite3.connect("../Databases/database_names.db")

You need to remove the ../ from the database path for successful connection and successful testing.
"""


if __name__ == '__main__':
    test_dir = 'unit_tests'
    test_suite = unittest.defaultTestLoader.discover(start_dir=test_dir, pattern="test*.py")
    test_runner = unittest.TextTestRunner()
    test_runner.run(test_suite)