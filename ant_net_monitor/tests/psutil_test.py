import logging
import sys
import unittest
from datetime import datetime, timedelta
from time import sleep

from ant_net_monitor import create_app
from ant_net_monitor.extensions import db
from ant_net_monitor.status import Status

logger = logging.getLogger()
logger.level = logging.DEBUG
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)


class TestPsutilMethods(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app.config["FINISH_TESTING"] = False
        with self.app_context:
            db.create_all()

    def tearDown(self):
        with self.app_context:
            db.session.remove()
            db.drop_all()
        self.app.config["FINISH_TESTING"] = True
        logging.info("Finish testing.")

    def test_get_status(self):
        with self.app_context:
            Status.utils.BasicStatus.save()
        ret = self.app.test_client().get("/api/status/basic_status")
        logging.info(ret.data)

    def test_get_last_cpu_status(self):
        with self.app_context:
            Status.utils.CPUStatus.save()
        ret = self.app.test_client().get("/api/status/cpu_status?type=update")
        logging.info(ret.data)

    def test_get_batch_cpu_status(self):
        with self.app_context:
            for i in range(10):
                Status.utils.CPUStatus.save()
        ret = self.app.test_client().get("/api/status/cpu_status?type=init")
        logging.info(ret.data)
