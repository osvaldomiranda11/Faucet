from . import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    referral_code = db.Column(db.String(150), unique=True)
    referred_by = db.Column(db.String(150))
    coins = db.Column(db.Integer, default=0)
    xp = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'<User {self.username}>'
