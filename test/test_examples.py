import unittest
import to_test


class TestMain(unittest.TestCase):
    def setUp(self):
        print('start testing')

    def test_do_stuff(self):
        test_param = 10
        result = to_test.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = 'shshssh'
        result = to_test.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        test_param = None
        result = to_test.do_stuff(test_param)
        self.assertEqual(result, 'please add a number')

    def test_do_stuff4(self):
        test_param = ''
        result = to_test.do_stuff(test_param)
        self.assertEqual(result, 'please add a number')

    def tearDown(self):
        print('cleaning up')


if __name__ == '__main__':
    unittest.main()
