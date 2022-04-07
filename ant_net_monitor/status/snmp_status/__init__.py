from . import basic_status, cpu_status, snmp_agent, ram_status, disk_status

SnmpAgent = snmp_agent.SnmpAgent

# BasicStatus = basic_status.BasicStatus
CPUStatus = cpu_status.CPUStatus
RAMStatus = ram_status.RAMStatus
DiskStatus = disk_status.DiskStatus


class SnmpStatus:
    def __init__(self, agent):
        self.agent = agent
        self.CPUStatus = cpu_status.CPUStatus(agent)
        self.RAMStatus = ram_status.RAMStatus(agent)
        self.DiskStatus = disk_status.DiskStatus(agent)

    def save_all(self):
        self.CPUStatus.save()
        self.RAMStatus.save()
        self.DiskStatus.save()

    @classmethod
    def init_agent(cls, app, host, community):
        snmp_agent.SnmpAgent.init_agent(app, host, community)

    @classmethod
    def get_agent_list(cls, app):
        with app.app_context():
            return [cls(agent) for agent in snmp_agent.SnmpAgent.get_all()]
