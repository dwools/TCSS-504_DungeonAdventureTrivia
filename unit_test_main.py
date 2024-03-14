import unittest

#




if __name__ == '__main__':
    test_dir = 'unit_tests'
    test_suite = unittest.defaultTestLoader.discover(start_dir=test_dir, pattern="test*.py")
    test_runner = unittest.TextTestRunner()
    test_runner.run(test_suite)