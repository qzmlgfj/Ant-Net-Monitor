import unittest
import logging
import sys
from time import sleep
from datetime import datetime, timedelta

from ant_net_monitor import create_app
from ant_net_monitor.extensions import db

from ant_net_monitor.status import Status

logger = logging.getLogger()
logger.level = logging.DEBUG
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)


class TestClientMethods(unittest.TestCase):
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

    def date_range(self, start, end, delta):
        current = start.replace(second=0, microsecond=0)
        while current < end.replace(second=0, microsecond=0):
            yield current
            current += delta

    # def test_hello(self):
    #    logging.info(self.app.config["APPLICATION_ENV"])
    #    ret = self.app.test_client().get("/hello")
    #    self.assertEqual(b"Hello, World!", ret.data)

    def test_get_status(self):
        with self.app_context:
            Status.BasicStatus.save()
        ret = self.app.test_client().get("/api/status/basic_status")
        logging.info(ret.data)

    def test_get_last_cpu_status(self):
        with self.app_context:
            Status.CPUStatus.save()
        ret = self.app.test_client().get("/api/status/cpu_status?type=update")
        logging.info(ret.data)

    def test_get_batch_cpu_status(self):
        with self.app_context:
            for i in range(10):
                Status.CPUStatus.save()
        ret = self.app.test_client().get("/api/status/cpu_status?type=init")
        logging.info(ret.data)

    def test_get_last_ram_status(self):
        with self.app_context:
            Status.RAMStatus.save()
        ret = self.app.test_client().get("/api/status/ram_status?type=update")
        logging.info(ret.data)

    def test_get_batch_ram_status(self):
        with self.app_context:
            for i in range(10):
                Status.RAMStatus.save()
                sleep(1)
        ret = self.app.test_client().get("/api/status/ram_status?type=init")
        logging.info(ret.get_json())

    def test_get_ram_status_in_one_day(self):
        with self.app_context:
            start = datetime.utcnow() - timedelta(minutes=15)
            end = datetime.utcnow()
            delta = timedelta(minutes=1)
            for time_stamp in self.date_range(start, end, delta):
                Status.RAMStatus.save(Status.RAMStatus(is_random=True, time_stamp=time_stamp))
        ret = self.app.test_client().get("/api/status/ram_status?type=day")
        logging.info(ret.get_json())

    def test_get_last_disk_status(self):
        with self.app_context:
            Status.DiskStatus.init_counter()
            sleep(1)
            Status.DiskStatus.save()
        ret = self.app.test_client().get("/api/status/disk_status?type=update")
        logging.info(ret.get_json())

    def test_get_batch_disk_status(self):
        with self.app_context:
            Status.DiskStatus.init_counter()
            sleep(1)
            for i in range(10):
                Status.DiskStatus.save()
                sleep(1)
        ret = self.app.test_client().get("/api/status/disk_status?type=init")
        logging.info(ret.get_json())

    def test_get_last_network_status(self):
        with self.app_context:
            Status.NetworkStatus.init_counter()
            sleep(1)
            Status.NetworkStatus.save()
        ret = self.app.test_client().get("/api/status/network_status?type=update")
        logging.info(ret.get_json())

    def test_get_batch_network_status(self):
        with self.app_context:
            Status.NetworkStatus.init_counter()
            sleep(1)
            for i in range(10):
                Status.NetworkStatus.save()
                sleep(1)
        ret = self.app.test_client().get("/api/status/network_status?type=init")
        logging.info(ret.get_json())
