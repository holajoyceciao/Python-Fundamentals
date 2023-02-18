import unittest
import numfunc

class TestNumFunc(unittest.TestCase):
    def setUp(self):
        print('about to test a function')

    def test_do_stuff(self):
        '''The result is '''
        test_param = 10
        result = numfunc.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = 'sfges'
        result = numfunc.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        test_param = None
        result = numfunc.do_stuff(test_param)
        self.assertEqual(result, 'Please enter number')

    def test_do_stuff4(self):
        test_param = ''
        result = numfunc.do_stuff(test_param)
        self.assertEqual(result, 'Please enter number')

    def tearDown(self):
        print('cleaning up')

if __name__ == '__main__':
    unittest.main()
