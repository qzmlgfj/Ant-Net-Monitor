import importlib

class Status:
    @classmethod
    def init_app(cls,app):
        if not app.config["ENABLE_SNMP"]:
            status_module = importlib.import_module("ant_net_monitor.status.psutil_status")
            cls.BasicStatus = status_module.BasicStatus
            cls.CPUStatus = status_module.CPUStatus
            cls.RAMStatus = status_module.RAMStatus
            cls.DiskStatus = status_module.DiskStatus
            cls.NetworkStatus = status_module.NetworkStatus
        else:
            status_module = importlib.import_module("ant_net_monitor.status.snmp_status")
            cls.BasicStatus = status_module.BasicStatus