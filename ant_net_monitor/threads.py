import threading
from time import sleep
import random

from .extensions import db
from .status import Status

from .alarm.alarm import Alarm

# TODO 整个函数变量进去，进一步封装


def set_basic_status_thread(app):
    """Register basic status thread."""

    def save_status_loop(app):
        with app.app_context():
            Status.DiskStatus.init_counter()
            Status.NetworkStatus.init_counter()
            while True:
                try:
                    # alarm_value = (
                    #    new_basic_status.cpu_percent,
                    #    new_cpu_status.iowait_percent,
                    #    new_cpu_status.steal_percent,
                    # )
                    # Alarm.check_cpu_alarm(*alarm_value)

                    Status.save_all_status()

                    sleep(1)
                except Exception as e:
                    db.session.rollback()
                    sleep(random.random())
                    app.logger.error(e)

                try:
                    if app.config["FINISH_TESTING"]:
                        break
                except KeyError:
                    pass

    save_status_thread = threading.Thread(target=save_status_loop, args=(app,))
    save_status_thread.start()


def set_all_threads(app):
    set_basic_status_thread(app)
