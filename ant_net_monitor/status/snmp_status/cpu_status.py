from dataclasses import dataclass
from datetime import datetime, timedelta

from sqlalchemy import extract

from ...extensions import db
from .snmp_utils import get_snmp_value


@dataclass
class CPUStatus(db.Model):
    id: int
    user_percent: int
    system_percent: int
    time_stamp: datetime

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    time_stamp = db.Column(db.DateTime)
    user_percent = db.Column(db.Integer)
    system_percent = db.Column(db.Integer)

    def __init__(self, host, community):
        self.user_percent = get_snmp_value(host, community, "UCD-SNMP-MIB", "ssCpuUser")
        self.system_percent = get_snmp_value(
            host, community, "UCD-SNMP-MIB", "ssCpuSystem"
        )
        self.time_stamp = datetime.utcnow().replace(microsecond=0)

    def __str__(self):
        return f"{self.user_percent}% {self.system_percent}%"

    @staticmethod
    def save(status=None):
        if not status:
            db.session.add(CPUStatus())
        else:
            db.session.add(status)
        db.session.commit()

    @staticmethod
    def get_last():
        start = datetime.utcnow() - timedelta(minutes=1)
        return (
            CPUStatus.query.filter(CPUStatus.time_stamp >= start)
            .order_by(CPUStatus.time_stamp.desc())
            .first()
        )

    @staticmethod
    def get_batch():
        count = CPUStatus.query.count()
        if count > 100:
            count = 100
        return (
            CPUStatus.query.order_by(CPUStatus.time_stamp.desc())
            .limit(count)
            .all()[::-1]
        )
    
    @staticmethod
    def get_in_one_day():
        start = datetime.utcnow() - timedelta(days=1)
        return (
            CPUStatus.query.filter(CPUStatus.time_stamp >= start)
            .filter(extract("minute", CPUStatus.time_stamp) % 5 == 0)
            .filter(extract("second", CPUStatus.time_stamp) == 0)
            .all()
        )
