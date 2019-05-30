#!/usr/bin/env python
# -*- coding:utf-8 -*-
#__author__=v_zhangjunjie02
from django.conf.urls import url

from myadmin.views import index,member,users,shop,category,product,orders,orderdetail,payment

urlpatterns = [
    # 后台首页
    url(r'^$', index.index, name="myadmin_index"),

    #会员登录和退出路由配置
    url(r'^login$', index.login, name="myadmin_login"),
    url(r'^dologin$', index.dologin, name="myadmin_dologin"),
    url(r'^logout$', index.logout, name="myadmin_logout"),
    url(r'^verify$', index.verify, name="myadmin_verify"),  # 验证码



    # # 会员信息管理
    url(r'^member/(?P<pIndex>[0-9]+)$', member.index, name="myadmin_member_index"),
    url(r'^member/del/(?P<mid>[0-9]+)$', member.delete, name="myadmin_member_del"),
    url(r'^member/edit/(?P<mid>[0-9]+)$', member.edit, name="myadmin_member_edit"),
    url(r'^member/update/(?P<mid>[0-9]+)$', member.update, name="myadmin_member_update"),

    # 员工账号信息管理
    url(r'^user/(?P<pIndex>[0-9]+)$', users.index, name="myadmin_user_index"),
    url(r'^user/add$', users.add, name="myadmin_user_add"),
    url(r'^user/insert$', users.insert, name="myadmin_user_insert"),
    url(r'^user/del/(?P<uid>[0-9]+)$', users.delete, name="myadmin_user_del"),
    url(r'^user/edit/(?P<uid>[0-9]+)$', users.edit, name="myadmin_user_edit"),
    url(r'^user/update/(?P<uid>[0-9]+)$', users.update, name="myadmin_user_update"),
    url(r'^user/resetpass/(?P<uid>[0-9]+)$', users.resetpass, name="myadmin_user_resetpass"),
    url(r'^user/doresetpass/(?P<uid>[0-9]+)$', users.doresetpass, name="myadmin_user_doresetpass"),

    # 店铺信息管理
    url(r'^shop/(?P<pIndex>[0-9]+)$', shop.index, name="myadmin_shop_index"),
    url(r'^shop/add$', shop.add, name="myadmin_shop_add"),
    url(r'^shop/insert$', shop.insert, name="myadmin_shop_insert"),
    url(r'^shop/del/(?P<sid>[0-9]+)$', shop.delete, name="myadmin_shop_del"),
    url(r'^shop/edit/(?P<sid>[0-9]+)$', shop.edit, name="myadmin_shop_edit"),
    url(r'^shop/update/(?P<sid>[0-9]+)$', shop.update, name="myadmin_shop_update"),

    # 菜品分类信息管理
    url(r'^category/(?P<pIndex>[0-9]+)$', category.index, name="myadmin_category_index"),
    # url(r'^category/load/(?P<sid>[0-9]+)$', category.loadCategory, name="myadmin_category_load"),
    url(r'^category/add$', category.add, name="myadmin_category_add"),
    url(r'^category/insert$', category.insert, name="myadmin_category_insert"),
    url(r'^category/del/(?P<cid>[0-9]+)$', category.delete, name="myadmin_category_del"),
    url(r'^category/edit/(?P<cid>[0-9]+)$', category.edit, name="myadmin_category_edit"),
    url(r'^category/update/(?P<cid>[0-9]+)$', category.update, name="myadmin_category_update"),

    # 菜品信息管理
    url(r'^product/(?P<pIndex>[0-9]+)$', product.index, name="myadmin_product_index"),
    url(r'^product/add$', product.add, name="myadmin_product_add"),
    url(r'^product/insert$', product.insert, name="myadmin_product_insert"),
    url(r'^product/del/(?P<pid>[0-9]+)$', product.delete, name="myadmin_product_del"),
    url(r'^product/edit/(?P<pid>[0-9]+)$', product.edit, name="myadmin_product_edit"),
    url(r'^product/update/(?P<pid>[0-9]+)$', product.update, name="myadmin_product_update"),

    # 订单信息管理
    url(r'^orders/(?P<pIndex>[0-9]+)$', orders.index, name="myadmin_orders_index"),
    # 订单详情信息管理
    url(r'^orderdetail/(?P<pIndex>[0-9]+)$', orderdetail.index, name="myadmin_orderdetail_index"),
    # 支付详情管理
    url(r'^payment/(?P<pIndex>[0-9]+)$', payment.index, name="myadmin_payment_index"),











]
