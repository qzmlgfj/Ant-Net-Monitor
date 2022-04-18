from . import (
    basic_status,
    cpu_status,
    snmp_agent,
    ram_status,
    disk_status,
    network_status,
    load_status,
)


class SnmpStatus:
    def __init__(self, agent):
        self.agent = agent
        self.CPUStatus = cpu_status.CPUStatus(agent)
        self.RAMStatus = ram_status.RAMStatus(agent)
        self.DiskStatus = disk_status.DiskStatus(agent)
        self.NetworkStatus = network_status.NetworkStatus(agent)
        self.LoadStatus = load_status.LoadStatus(agent)

    def save_all(self):
        self.CPUStatus.save()
        self.RAMStatus.save()
        self.DiskStatus.save()
        self.NetworkStatus.save()
        self.LoadStatus.save()

    @classmethod
    def init_agent(cls, app, host, community):
        snmp_agent.SnmpAgent.init_agent(app, host, community)

    @classmethod
    def get_agent_list(cls, app):
        with app.app_context():
            return [cls(agent) for agent in snmp_agent.SnmpAgent.get_all()]

    @classmethod
    def get_basic_status(cls):
        agent = snmp_agent.SnmpAgent.query.first()
        return basic_status.BasicStatus.get_last(agent)

    @classmethod
    def get_cpu_status(cls, type):
        agent = snmp_agent.SnmpAgent.query.first()
        if type == "init":
            return cpu_status.CPUStatusInfo.get_batch(agent)
        elif type == "update":
            return cpu_status.CPUStatusInfo.get_last(agent)
        elif type == "day":
            return cpu_status.CPUStatusInfo.get_in_one_day(agent)

    @classmethod
    def get_ram_status(cls, type):
        agent = snmp_agent.SnmpAgent.query.first()
        if type == "init":
            return ram_status.RAMStatusInfo.get_batch(agent)
        elif type == "update":
            return ram_status.RAMStatusInfo.get_last(agent)
        elif type == "day":
            return ram_status.RAMStatusInfo.get_in_one_day(agent)

    @classmethod
    def get_disk_status(cls, type):
        agent = snmp_agent.SnmpAgent.query.first()
        if type == "init":
            return disk_status.DiskStatusInfo.get_batch(agent)
        elif type == "update":
            return disk_status.DiskStatusInfo.get_last(agent)
        elif type == "day":
            return disk_status.DiskStatusInfo.get_in_one_day(agent)

    @classmethod
    def get_network_status(cls, type):
        agent = snmp_agent.SnmpAgent.query.first()
        if type == "init":
            return network_status.NetworkStatusInfo.get_batch(agent)
        elif type == "update":
            return network_status.NetworkStatusInfo.get_last(agent)
        elif type == "day":
            return network_status.NetworkStatusInfo.get_in_one_day(agent)

    @classmethod
    def get_load_status(cls, type):
        agent = snmp_agent.SnmpAgent.query.first()
        if type == "init":
            return load_status.LoadStatusInfo.get_batch(agent)
        elif type == "update":
            return load_status.LoadStatusInfo.get_last(agent)
        elif type == "day":
            return load_status.LoadStatusInfo.get_in_one_day(agent)
