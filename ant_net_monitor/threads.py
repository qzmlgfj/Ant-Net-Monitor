import threading
from time import sleep

from .extensions import db
from .status.basic_status import BasicStatus
from .status.cpu_status import CPUStatus
from .status.ram_status import RAMStatus

# TODO 整个函数变量进去，进一步封装


def set_basic_status_thread(app):
    """Register basic status thread."""

    def save_status_loop(app):
        with app.app_context():
            while True:
                try:
                    BasicStatus.save()
                except Exception as e:
                    db.session.rollback()
                    app.logger.error(e)

    save_status_thread = threading.Thread(target=save_status_loop, args=(app,))
    save_status_thread.start()


def set_cpu_status_thread(app):
    """Register cpu status thread."""

    def save_status_loop(app):
        with app.app_context():
            while True:
                try:
                    CPUStatus.save()
                except Exception as e:
                    db.session.rollback()
                    app.logger.error(e)

    save_status_thread = threading.Thread(target=save_status_loop, args=(app,))
    save_status_thread.start()


def set_ram_status_thread(app):
    """Register ram status thread."""

    def save_status_loop(app):
        with app.app_context():
            while True:
                try:
                    RAMStatus.save()
                    sleep(1)
                except Exception as e:
                    db.session.rollback()
                    app.logger.error(e)

    save_status_thread = threading.Thread(target=save_status_loop, args=(app,))
    save_status_thread.start()


def set_all_threads(app):
    set_basic_status_thread(app)
    set_cpu_status_thread(app)
    set_ram_status_thread(app)
