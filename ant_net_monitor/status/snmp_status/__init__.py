from . import basic_status, cpu_status, snmp_agent, ram_status, disk_status, network_status


class SnmpStatus:
    def __init__(self, agent):
        self.agent = agent
        self.CPUStatus = cpu_status.CPUStatus(agent)
        self.RAMStatus = ram_status.RAMStatus(agent)
        self.DiskStatus = disk_status.DiskStatus(agent)
        self.NetworkStatus = network_status.NetworkStatus(agent)


    def save_all(self):
        self.CPUStatus.save()
        self.RAMStatus.save()
        self.DiskStatus.save()
        self.NetworkStatus.save()

    @classmethod
    def init_agent(cls, app, host, community):
        snmp_agent.SnmpAgent.init_agent(app, host, community)

    @classmethod
    def get_agent_list(cls, app):
        with app.app_context():
            return [cls(agent) for agent in snmp_agent.SnmpAgent.get_all()]
