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
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        with self.app_context:
            db.create_all()

    def test_hello(self):
        logging.info(self.app.config["APPLICATION_ENV"])
        ret = self.app.test_client().get("/hello")
        self.assertEqual(b"Hello, World!", ret.data)

    def test_get_status(self):
        ret = self.app.test_client().get("/status")
        logging.info(ret.data)
