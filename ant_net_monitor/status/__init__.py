import importlib


class Status:
    @classmethod
    def init_app(cls):
        status_module = importlib.import_module(
            "ant_net_monitor.status.psutil_status"
        )
        cls.utils = status_module.PsutilStatus

        alarm_module = importlib.import_module("ant_net_monitor.alarm")
        cls.Alarm = alarm_module.Alarm

    @classmethod
    def save_all_status(cls):
        new_basic_status = cls.utils.BasicStatus()
        new_cpu_status = cls.utils.CPUStatus()
        new_ram_status = cls.utils.RAMStatus()
        new_disk_status = cls.utils.DiskStatus()
        new_network_status = cls.utils.NetworkStatus()
        new_load_status = cls.utils.LoadStatus()
        new_swap_status = cls.utils.SwapStatus()
        new_interrupt_status = cls.utils.InterruptStatus()

        cls.utils.BasicStatus.save(new_basic_status)
        cls.utils.CPUStatus.save(new_cpu_status)
        cls.utils.RAMStatus.save(new_ram_status)
        cls.utils.DiskStatus.save(new_disk_status)
        cls.utils.NetworkStatus.save(new_network_status)
        cls.utils.LoadStatus.save(new_load_status)
        cls.utils.SwapStatus.save(new_swap_status)
        cls.utils.InterruptStatus.save(new_interrupt_status)

        alarm_value = (
            new_basic_status.cpu_percent,
            new_cpu_status.iowait,
            new_cpu_status.steal,
        )
        cls.Alarm.check_cpu_alarm(*alarm_value)
        cls.Alarm.check_ram_alarm(new_basic_status.ram_percent)
        cls.Alarm.check_swap_alarm(new_basic_status.swap_percent)

    @classmethod
    def init_status(cls):
        cls.utils.DiskStatus.init_counter()
        cls.utils.NetworkStatus.init_counter()
        cls.utils.InterruptStatus.init_counter()
