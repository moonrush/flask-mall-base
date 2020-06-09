'''
    :auhtor: taki
'''
from flask import request,g
from flask_ckeditor import CKEditorField
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, \
                    IntegerField, FloatField, HiddenField
from wtforms.validators import DataRequired,  Length, ValidationError
from xp_mall.models.region import Region


class RegionForm(FlaskForm):
    parent_id = HiddenField('Parent')
    name = StringField('Name',validators=[DataRequired(),Length(1,30)])
    order_id = IntegerField('OrderNo')
    submit = SubmitField()