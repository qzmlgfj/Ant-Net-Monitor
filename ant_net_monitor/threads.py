import threading
from time import sleep

from sqlalchemy.orm import scoped_session, sessionmaker

from .extensions import db
from .status.basic_status import BasicStatus, save_basic_status
from .status.cpu_status import CPUStatus, save_cpu_status
from .status.ram_status import RAMStatus, save_ram_status

# TODO 整个函数变量进去，进一步封装


def set_basic_status_thread(session_factory, app):
    """Register basic status thread."""

    def save_status_loop(app):
        with app.app_context():
            while True:
                save_basic_status(thread_session, BasicStatus())

    thread_session = scoped_session(session_factory)
    save_status_thread = threading.Thread(target=save_status_loop, args=(app,))
    save_status_thread.start()


def set_cpu_status_thread(session_factory, app):
    """Register cpu status thread."""

    def save_status_loop(app):
        with app.app_context():
            while True:
                save_cpu_status(thread_session, CPUStatus())

    thread_session = scoped_session(session_factory)
    save_status_thread = threading.Thread(target=save_status_loop, args=(app,))
    save_status_thread.start()


def set_ram_status_thread(session_factory, app):
    """Register ram status thread."""

    def save_status_loop(app):
        with app.app_context():
            while True:
                save_ram_status(thread_session, RAMStatus())
                sleep(1)

    thread_session = scoped_session(session_factory)
    save_status_thread = threading.Thread(target=save_status_loop, args=(app,))
    save_status_thread.start()


def set_session_factory(app):
    with app.app_context():
        engine = db.get_engine()
        return sessionmaker(bind=engine)


def set_all_threads(app):
    session_factory = set_session_factory(app)
    set_basic_status_thread(session_factory, app)
    set_cpu_status_thread(session_factory, app)
    set_ram_status_thread(session_factory, app)
