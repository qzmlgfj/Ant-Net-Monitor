import unittest
from backend import *

class TestClientMethods(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        self.app = create_app()
        super().__init__(methodName)

    def test_hello(self):
        ret = self.app.test_client().get('/hello')
        self.assertEqual(b"Hello, World!", ret.data)
