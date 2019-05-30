#!/usr/bin/env python
# -*- coding:utf-8 -*-
#__author__=v_zhangjunjie02
from django.shortcuts import render
from common.models import Orders,OrderDetail,Product
from django.core.paginator import Paginator
from django.http import HttpResponse
from  datetime import datetime
from PIL import Image
import time,os

def index(request,pIndex):
    list = OrderDetail.objects.all()
    p = Paginator(list, 10)
    if pIndex == '':
        pIndex = '1'
    pIndex = int(pIndex)
    list1 = p.page(pIndex)
    plist = p.page_range
    context = {'order_detaillist': list1, 'plist': plist, 'pIndex': pIndex}
    return render(request,'myadmin/orderdetail/index.html',context)