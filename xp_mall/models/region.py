# -*- coding=utf-8 -*-

from xp_mall.extensions import db
from datetime import datetime


class Region(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)
    order_id = db.Column(db.Integer)
    parent_id = db.Column(db.Integer, db.ForeignKey('region.id'), default=None)

    parent = db.relationship('Region', back_populates="sub_regs", remote_side=[id])
    sub_regs = db.relationship('Region', back_populates="parent", cascade='all, delete-orphan', order_by=order_id)

    def delete(self):
        default_region = Region.query.get(1)
        db.session.delete(self)
        db.session.commit()

