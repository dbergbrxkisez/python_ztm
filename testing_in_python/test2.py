# run this file from terminal.
import unittest
import script


class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        '''HIIIII!!!!'''
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


if __name__ == '__main__':
    unittest.main()


# >>>python3 -m unittest        #  This runs all the test.
# >>>python3 -m unittest -v



