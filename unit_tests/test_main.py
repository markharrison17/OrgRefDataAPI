import unittest
from mock import patch, MagicMock
import main
import logging


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    @patch('logging.getLogger')
    def test__main__do_setup__TestNonsense(self, mock_get_logger):
        main.do_setup()

if __name__ == '__main__':
    unittest.main()