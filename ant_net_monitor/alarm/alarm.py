from ..extensions import db


class Alarm(db.Model):
    id: int
    name: str

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64))
    items = db.relationship('AlarmItem', backref='alarm', lazy='dynamic')

    def __init__(self, name):
        self.name = name
