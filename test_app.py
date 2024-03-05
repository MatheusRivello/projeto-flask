import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_hello_without_name(self):
        response = self.app.get('/')
        self.assertEqual(response.data.decode('utf-8'), 'Hello, World!')

    def test_hello_with_name(self):
        response = self.app.get('/?name=John')
        self.assertEqual(response.data.decode('utf-8'), 'Hello, John!')

if __name__ == '__main__':
    unittest.main()
