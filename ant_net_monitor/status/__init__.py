from cgitb import enable
import importlib


# TODO 再解耦一下
class Status:
    @classmethod
    def init_app(cls, app):
        cls.enable_snmp = app.config["ENABLE_SNMP"]

        if not cls.enable_snmp:
            status_module = importlib.import_module(
                "ant_net_monitor.status.psutil_status"
            )
            cls.BasicStatus = status_module.BasicStatus
            cls.CPUStatus = status_module.CPUStatus
            cls.RAMStatus = status_module.RAMStatus
            cls.DiskStatus = status_module.DiskStatus
            cls.NetworkStatus = status_module.NetworkStatus
        else:
            status_module = importlib.import_module(
                "ant_net_monitor.status.snmp_status"
            )
            cls.BasicStatus = status_module.BasicStatus

    @classmethod
    def save_all_status(cls):
        if not cls.enable_snmp:
            new_basic_status = Status.BasicStatus()
            new_cpu_status = Status.CPUStatus()
            new_ram_status = Status.RAMStatus()
            new_disk_status = Status.DiskStatus()
            new_network_status = Status.NetworkStatus()

            Status.BasicStatus.save(new_basic_status)
            Status.CPUStatus.save(new_cpu_status)
            Status.RAMStatus.save(new_ram_status)
            Status.DiskStatus.save(new_disk_status)
            Status.NetworkStatus.save(new_network_status)
        else:
            cls.save_basic_status()

    def __init__(self, host=None, community=None):
        self.host = host
        self.community = community
