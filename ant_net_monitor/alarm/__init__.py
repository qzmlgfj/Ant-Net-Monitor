from ant_net_monitor.alarm.alarm_flag import AlarmFlag
from .alarm import Alarm
from .alarm_item import AlarmItem

from ..extensions import db


def create_cpu_alarm(app):
    with app.app_context():
        cpu_alarm = Alarm(name="CPU")
        db.session.add(cpu_alarm)
        db.session.commit()

        db.session.add(
            AlarmItem(name="cpu_usage", alarm_id=cpu_alarm.id, alarm_value=80)
        )
        db.session.add(
            AlarmItem(name="cpu_iowait", alarm_id=cpu_alarm.id, alarm_value=40)
        )
        db.session.add(
            AlarmItem(name="cpu_steal", alarm_id=cpu_alarm.id, alarm_value=10)
        )
        db.session.commit()


def create_ram_alarm(app):
    with app.app_context():
        ram_alarm = Alarm(name="RAM")
        db.session.add(ram_alarm)
        db.session.commit()

        db.session.add(
            AlarmItem(name="ram_usage", alarm_id=ram_alarm.id, alarm_value=80)
        )
        db.session.commit()


def get_cpu_alarm_items(app):
    with app.app_context():
        try:
            cpu_alarm = Alarm.query.filter_by(name="CPU").first()
            return AlarmItem.query.filter_by(alarm_id=cpu_alarm.id).all()
        except AttributeError:
            return None


def get_ram_alarm_items(app):
    with app.app_context():
        try:
            ram_alarm = Alarm.query.filter_by(name="RAM").first()
            return AlarmItem.query.filter_by(alarm_id=ram_alarm.id).all()
        except AttributeError:
            return None


def get_all_alarm_items(app):
    with app.app_context():
        try:
            cpu_alarm = Alarm.query.filter_by(name="CPU").first()
            ram_alarm = Alarm.query.filter_by(name="RAM").first()
            return AlarmItem.query.filter(
                AlarmItem.alarm_id.in_([cpu_alarm.id, ram_alarm.id])
            ).all()
        except AttributeError:
            return None


def init_alarm(app):
    if get_cpu_alarm_items(app) is None:
        create_cpu_alarm(app)
    if get_ram_alarm_items(app) is None:
        create_ram_alarm(app)

    AlarmFlag.init_flag(get_all_alarm_items(app))
