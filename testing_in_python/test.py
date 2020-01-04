# run this file from terminal.
import unittest
import script


class TestMain(unittest.TestCase):
    # useful for some default variables or something which has to be done before every function starts
    def setUp(self):
        print('about to test a function')


    def test_do_stuff(self):
        test_param = 10
        result = script.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = 'ksjdfksaf'
        result = script.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        test_param = None
        result = script.do_stuff(test_param)
        self.assertEqual(result, 'please enter number')

    def test_do_stuff4(self):
        test_param = ''
        result = script.do_stuff(test_param)
        self.assertEqual(result, 'please enter number')

    def test_do_stuff5(self):
        test_param = 0
        result = script.do_stuff(test_param)
        self.assertEqual(result, 'please enter number')

    # usually we do to maybe clean up some variables, reset some variables.
    # not much used. we can use when we use more complex like a database.
    def tearDown(self):
        print('cleaning uo')

if __name__ == '__main__':
    unittest.main()
