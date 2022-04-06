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
            cls.SnmpAgent = status_module.SnmpAgent
            cls.BasicStatus = status_module.BasicStatus
            cls.CPUStatus = status_module.CPUStatus


    @classmethod
    def save_all_status(cls):
        if not cls.enable_snmp:
            new_basic_status = cls.BasicStatus()
            new_cpu_status = cls.CPUStatus()
            new_ram_status = cls.RAMStatus()
            new_disk_status = cls.DiskStatus()
            new_network_status = cls.NetworkStatus()

            cls.BasicStatus.save(new_basic_status)
            cls.CPUStatus.save(new_cpu_status)
            cls.RAMStatus.save(new_ram_status)
            cls.DiskStatus.save(new_disk_status)
            cls.NetworkStatus.save(new_network_status)
        else:
            for agent in cls.SnmpAgent.get_all():
                new_cpu_status = cls.CPUStatus(agent)

                cls.CPUStatus.save(new_cpu_status)

    @classmethod
    def init_status(cls):
        if not cls.enable_snmp:
            cls.DiskStatus.init_counter()
            cls.NetworkStatus.init_counter()
