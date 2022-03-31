from ..extensions import db
from dataclasses import dataclass


@dataclass
class Alarm(db.Model):
    id: int
    name: str
    alarm_value: float
    counter: int
    flag: bool
    activated: bool
    interval_time: int

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64))
    alarm_value = db.Column(db.Float)
    counter = db.Column(db.Integer)
    flag = db.Column(db.Boolean)
    activated = db.Column(db.Boolean)
    interval_time = db.Column(db.Integer)

    def __init__(self, name, alarm_value):
        self.name = name
        self.alarm_value = alarm_value
        self.counter = 0
        self.flag = False
        self.activated = True
        self.interval_time = 300

    @classmethod
    def create_cpu_alarm(cls):
        db.session.add(cls(name="cpu_usage", alarm_value=80))
        db.session.add(cls(name="cpu_iowait", alarm_value=40))
        db.session.add(cls(name="cpu_steal", alarm_value=10))

        db.session.commit()

    @classmethod
    def create_ram_alarm(cls):
        db.session.add(cls(name="ram_usage", alarm_value=80))

        db.session.commit()

    @classmethod
    def set_alarm_flag(cls, name, flag):
        alarm_item = cls.query.filter_by(name=name).first()
        alarm_item.flag = flag

    @classmethod
    def get_all_alarm_items(cls):
        try:
            return cls.query.all()
        except Exception:
            return None

    @classmethod
    def init_alarm(cls, app):
        with app.app_context():
            if len(cls.get_all_alarm_items()) == 0:
                cls.create_cpu_alarm()
                cls.create_ram_alarm()

    @classmethod
    def update_alarm(cls, alarm):
        target = cls.query.filter_by(name=alarm["name"]).first()
        target.alarm_value = alarm["alarmValue"]
        target.activated = alarm["activated"]
        target.interval_time = alarm["intervalTime"]
        db.session.commit()

    @classmethod
    def check_cpu_alarm(cls, cpu_usage, cpu_iowait, cpu_steal):
        cpu_usage_alarm = cls.query.filter_by(name="cpu_usage").first()
        cpu_iowait_alarm = cls.query.filter_by(name="cpu_iowait").first()
        cpu_steal_alarm = cls.query.filter_by(name="cpu_steal").first()

        if cpu_usage > cpu_usage_alarm.alarm_value:
            cpu_usage_alarm.counter = cpu_usage_alarm.counter + 1
        else:
            cpu_usage_alarm.counter = cpu_usage_alarm.counter - 1

        if cpu_iowait > cpu_iowait_alarm.alarm_value:
            cpu_iowait_alarm.counter = cpu_iowait_alarm.counter + 1
        else:
            cpu_iowait_alarm.counter = cpu_iowait_alarm.counter - 1

        if cpu_steal > cpu_steal_alarm.alarm_value:
            cpu_steal_alarm.counter = cpu_steal_alarm.counter + 1
        else:
            cpu_steal_alarm.counter = cpu_steal_alarm.counter - 1

        if cpu_usage_alarm.counter >= 10:
            cls.set_alarm_flag("cpu_usage", True)
            cpu_usage_alarm.counter = 10
        elif cpu_usage_alarm.counter <= 0:
            cls.set_alarm_flag("cpu_usage", False)
            cpu_usage_alarm.counter = 0

        if cpu_iowait_alarm.counter >= 10:
            cls.set_alarm_flag("cpu_iowait", True)
            cpu_iowait_alarm.counter = 10
        elif cpu_iowait_alarm.counter <= 0:
            cls.set_alarm_flag("cpu_iowait", False)
            cpu_iowait_alarm.counter = 0

        if cpu_steal_alarm.counter >= 10:
            cls.set_alarm_flag("cpu_steal", True)
            cpu_steal_alarm.counter = 10
        elif cpu_steal_alarm.counter <= 0:
            cls.set_alarm_flag("cpu_steal", False)
            cpu_steal_alarm.counter = 0

        db.session.commit()
