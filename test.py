import unittest
import main


class TestMain(unittest.TestCase):

    # This setup use to print what ever you want before testing new function.
    def setUp(self):
        return ('I want to test this function.')

    def test_do_stuff(self):
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        str = 'Dhruv'
        result2 = main.do_stuff2(str)
        self.assertTrue(result2, 'Dhruv Love Priti')
        print(self)


unittest.main()
