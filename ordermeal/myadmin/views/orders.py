#!/usr/bin/env python
# -*- coding:utf-8 -*-
#__author__=v_zhangjunjie02
from django.shortcuts import render
from common.models import Shop,Orders,Member
from django.core.paginator import Paginator


def index(request,pIndex):
    list = Orders.objects.all()
    for vo in list:
        shoplist=Shop.objects.filter(id=vo.shop_id)
        for va in shoplist:
            vo.shopname=va.name
    for vc in list:
        memberlist=Member.objects.filter(id=vc.member_id)
        for vb in memberlist:
            vc.membername=vb.nickname
    p = Paginator(list, 10)
    if pIndex == '':
        pIndex = '1'
    pIndex = int(pIndex)
    list1 = p.page(pIndex)
    plist = p.page_range
    context = {'orderlist': list1, 'plist': plist, 'pIndex': pIndex}
    return render(request,'myadmin/orders/index.html',context)