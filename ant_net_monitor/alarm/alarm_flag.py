class AlarmFlag:
    alarm_dict: dict
    alarm_flag: dict

    @classmethod
    def init_flag(cls, all_alarm_items):
        cls.alarm_dict = {item.name: item.alarm_value for item in all_alarm_items}
        cls.alarm_flag = {item.name: False for item in all_alarm_items}

    @classmethod
    def set_flag(cls, name, flag):
        cls.alarm_flag[name] = flag

    @classmethod
    def get_all_flag(cls):
        return cls.alarm_flag
