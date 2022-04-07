import importlib


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

            cls.utils = status_module.SnmpStatus

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
            for status in cls.snmp_agents_status:
                status.save_all()

    @classmethod
    def init_status(cls):
        if not cls.enable_snmp:
            cls.DiskStatus.init_counter()
            cls.NetworkStatus.init_counter()
        #else:
        #    for status in cls.snmp_agents_status:
        #        status.DiskStatus.init_counter(status.agent)

    @classmethod
    def init_agent_list(cls, app):
        cls.snmp_agents_status = cls.utils.get_agent_list(app)

    @classmethod
    def init_agent(cls, app, host, community):
        cls.utils.init_agent(app, host, community)

    def __init__(self, agent=None):
        self.agent = agent
