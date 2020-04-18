# python -m unittest to run all the test files in the directory
# python -m unittest -v to see all tests in detail

import unittest
import script


class TestScript(unittest.TestCase):
    def setUp(self):
        print('About to run a test')
        # function which will run before every test usefull to declare any common variable

    def test_func(self):
        test_param = 10
        result = script.func(test_param)
        self.assertEqual(result, 20)

    def test_func_err_string(self):
        test_param = 'string'
        result = script.func(test_param)
        self.assertIsInstance(result, ValueError)

    def test_func_err_none(self):
        test_param = None
        result = script.func(test_param)
        self.assertIsInstance(result, TypeError)

    def tearDown(self):
        print('Cleaning up')


if __name__ == '__main__':
    unittest.main()
