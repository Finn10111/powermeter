from .. import db
from datetime import datetime


class Impulse(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    power = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now, nullable=False)

    def __repr__(self):
        return 'Impulse {} with power of {} watts at {}'.format(self.name, self.power, self.created_at)
