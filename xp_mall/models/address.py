'''
    author:taki
'''

from xp_mall.extensions import db

class Address(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('member.user_id'), default=None)
    receiver = db.Column(db.String(20))
    mobile = db.Column(db.String(30))
    address = db.Column(db.String(100))

    