# -*- coding=utf-8 -*-

from flask import render_template,g,request, \
    jsonify,current_app, redirect, flash, url_for
from flask_login import login_required
from xp_mall.admin import admin_module
from xp_mall.extensions import db
from xp_mall.forms.region import RegionForm
from xp_mall.models.region import Region



"""
Region 地区管理
"""
@admin_module.route('/region/manage/', defaults={"parent_id":0}, methods=["GET"])
@admin_module.route('/region/manage/<int:parent_id>', methods=["GET"])
@login_required
def manage_region(parent_id):
    parent_id = parent_id if parent_id else None
    regions = Region.query.filter_by(parent_id=parent_id).order_by(Region.order_id).all()
    return render_template('admin/region/region_list.html', regions=regions)

@admin_module.route('/region/new', methods=['GET', 'POST'])
@login_required
def new_region():
    form = RegionForm()
    if form.validate_on_submit():
        # 第一层级目录的父级为""
        # 使用0会发生约束完整性问题
        parent_id = form.parent_id.data if int(form.parent_id.data) else None
        name = form.name.data
        order_id = form.order_id.data
        region = Region(name=name, parent_id=parent_id,  order_id=order_id)
        db.session.add(region)
        db.session.commit()
        # flash('Category created.', 'success')
        # return redirect(url_for('.manage_category'))
        return str(region.id)
    elif form.errors:
        return jsonify(form.errors)
    return render_template('admin/region/region_add.html', form=form)


@admin_module.route('/region/<int:region_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_region(region_id):
    message = None
    form = RegionForm()
    region = Region.query.get_or_404(region_id)
    g.region_id = region.id
    g.region_name = region.name
    if form.validate_on_submit():
        try:
            region.name = form.name.data
            region.parent_id = form.parent_id.data
            region.order_id = form.order_id.data
            db.session.commit()
        except Exception as e:
            print(e)
            current_app.logge.debug(e)
            message = e
        else:
            return redirect(url_for("admin.manage_region"))
    else:
        print(form.errors)
        current_app.logger.error("表单数据验证错误")
        message = str(form.errors)

    form.name.data = region.name
    form.parent_id.data = region.parent_id
    form.order_id.data = region.order_id
    return render_template('admin/region/region_edit.html', form=form, message=message)

@admin_module.route('/region/delete', methods=['POST'])
@login_required
def delete_region():
    region_id = int(request.form['reg_id'])
    region = Region.query.get_or_404(region_id)
    try:
        region.delete()
    except Exception as e:
        return "fail"
    return "ok"


@admin_module.route('/region', methods=['get'])
@login_required
def get_reg():
    parent_id = request.args.get("region_id", 0, type=int)
    parent_id = parent_id if parent_id else None
    sub_regs = Region.query.filter_by(parent_id=parent_id).all()
    reg_dicts = [(sub_reg.name,sub_reg.id) for sub_reg in sub_regs]
    # print(cate_dicts)
    return jsonify(reg_dicts)
#