from datetime import datetime
import psutil
from .extensions import db

class Status(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    time_stamp = db.Column(
        db.DateTime, default=datetime.now, onupdate=datetime.now
    )
    cpu = db.Column(db.Float)
    memory = db.Column(db.Float)
    disk = db.Column(db.Float)

    def __init__(self):
        self.cpu = psutil.cpu_percent(interval=1)
        self.memory = psutil.virtual_memory().available
        self.disk = psutil.disk_usage("/").used
        # self.network = psutil.net_io_counters().bytes_recv
        # self.time = psutil.cpu_times_percent(interval=1)

    def __str__(self):
        return f"cpu:{self.cpu}%, memory:{round(self.memory/(1024**3),2)}G, disk:{round(self.disk/(1024**3),2)}G"


def save_status(status):
    db.session.add(status)
    db.session.commit()
