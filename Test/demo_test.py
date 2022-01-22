import imp
import unittest
import logging
import sys
from backend import *

logger = logging.getLogger()
logger.level = logging.DEBUG
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)


class TestClientMethods(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        #self.app = create_app(test_config={"TEST": "TRUE"})
        self.app = create_app()
        super().__init__(methodName)

    def test_hello(self):
        logging.info(self.app.config["APPLICATION_ENV"])
        ret = self.app.test_client().get("/hello")
        self.assertEqual(b"Hello, World!", ret.data)
