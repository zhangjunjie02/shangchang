#!/usr/bin/env python
# -*- coding:utf-8 -*-
#__author__=v_zhangjunjie02
from django.shortcuts import render
from common.models import Category,Shop
from django.core.paginator import Paginator
from  datetime import datetime



def index(request,pIndex):
    '''浏览信息'''
    list = Category.objects.all()
    for ob in list:
        shoplist=Shop.objects.filter(id=ob.shop_id)
        for vo in shoplist:
            ob.shopname=vo.name
    p = Paginator(list, 10)
    if pIndex == '':
        pIndex = '1'
    pIndex = int(pIndex)
    list1 = p.page(pIndex)
    plist = p.page_range
    context = {'typelist': list1, 'plist': plist, 'pIndex': pIndex}
    return render(request,'myadmin/category/index.html',context)

def add(request):
    list = Shop.objects.all()
    context={'shoplist':list}

    return render(request,'myadmin/category/add.html',context)

def insert(request):
    try:
        ob=Category()
        ob.name=request.POST['name']
        ob.status=1
        ob.shop_id=request.POST['typeid']
        ob.create_at=datetime.now()
        ob.update_at=datetime.now()
        ob.save()
        context={"info":"添加成功"}

    except Exception as err:
        print(err)
        context={"info":"添加失败"}
    return render(request,'myadmin/info.html',context)


def delete(request,cid):
    try:
        ob=Category.objects.get(id=cid)
        ob.delete()
        context={"info":"删除成功"}

    except Exception as err:
        print(err)
        context = {"info": "没有找到要删除的信息"}
    return render(request,'myadmin/info.html',context)


def edit(request,cid):
    list=Category.objects.get(id=cid)
    list2=Shop.objects.all()

    context={"typelist":list,"shoplist":list2}
    return render(request,'myadmin/category/edit.html',context)


def update(request,cid):
    try:
        ob = Category.objects.get(id=cid)
        ob.name=request.POST['name']
        ob.shop_id=request.POST['typeid']
        ob.status=request.POST['status']
        ob.update_at=datetime.now()
        ob.save()
        context = {"info": "修改成功"}
    except Exception as err:
        print(err)
        context = {"info": "没有找到要修改的信息"}
    return render(request, 'myadmin/info.html', context)



