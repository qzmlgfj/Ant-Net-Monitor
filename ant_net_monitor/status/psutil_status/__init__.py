from . import basic_status, cpu_status, ram_status, disk_status, network_status


class PsutilStatus:
    BasicStatus = basic_status.BasicStatus
    CPUStatus = cpu_status.CPUStatus
    RAMStatus = ram_status.RAMStatus
    DiskStatus = disk_status.DiskStatus
    NetworkStatus = network_status.NetworkStatus

    @classmethod
    def get_basic_status(cls):
        return cls.BasicStatus.get_last()

    @classmethod
    def get_cpu_status(cls, type):
        if type == "init":
            return cls.CPUStatus.get_batch()
        elif type == "update":
            return cls.CPUStatus.get_last()
        elif type == "day":
            return cls.CPUStatus.get_in_one_day()

    @classmethod
    def get_ram_status(cls, type):
        if type == "init":
            return cls.RAMStatus.get_batch()
        elif type == "update":
            return cls.RAMStatus.get_last()
        elif type == "day":
            return cls.RAMStatus.get_in_one_day()

    @classmethod
    def get_disk_status(cls, type):
        if type == "init":
            return cls.DiskStatus.get_batch()
        elif type == "update":
            return cls.DiskStatus.get_last()
        elif type == "day":
            return cls.DiskStatus.get_in_one_day()

    @classmethod
    def get_network_status(cls, type):
        if type == "init":
            return cls.NetworkStatus.get_batch()
        elif type == "update":
            return cls.NetworkStatus.get_last()
        elif type == "day":
            return cls.NetworkStatus.get_in_one_day()
