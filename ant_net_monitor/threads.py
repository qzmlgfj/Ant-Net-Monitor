import threading
from time import sleep

from ant_net_monitor.status.cpu_status import CPUStatus, save_cpu_status
from ant_net_monitor.status.ram_status import RAMStatus, save_ram_status
from ant_net_monitor.status.basic_status import BasicStatus, save_basic_status

# TODO 测试情况下的环境变量
def set_basic_status_thread(app):
    """Register basic status thread."""

    def save_status_loop(app):
        with app.app_context():
            while True:
                save_basic_status(BasicStatus())

    save_status_thread = threading.Thread(target=save_status_loop, args=(app,))
    save_status_thread.start()


def set_cpu_status_thread(app):
    """Register cpu status thread."""

    def save_status_loop(app):
        with app.app_context():
            while True:
                save_cpu_status(CPUStatus())

    save_status_thread = threading.Thread(target=save_status_loop, args=(app,))
    save_status_thread.start()


def set_ram_status_thread(app):
    """Register ram status thread."""

    def save_status_loop(app):
        with app.app_context():
            while True:
                save_ram_status(RAMStatus())
                sleep(1)

    save_status_thread = threading.Thread(target=save_status_loop, args=(app,))
    save_status_thread.start()

def set_all_threads(app):
    set_basic_status_thread(app)
    set_cpu_status_thread(app)
    set_ram_status_thread(app)
