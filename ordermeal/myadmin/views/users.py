
#!/usr/bin/env python
# -*- coding:utf-8 -*-
#__author__=v_zhangjunjie02
from django.shortcuts import render
from django.http import HttpResponse
from common.models import User,Member
from django.core.paginator import Paginator
from  datetime import datetime
from PIL import Image
import time,os



def index(request,pIndex):
    '''浏览信息'''
    list=User.objects.all()
    p=Paginator(list,10)
    if pIndex == '':
        pIndex = '1'
    pIndex=int(pIndex)
    list1=p.page(pIndex)
    plist=p.page_range
    context={'userlist':list1,'plist':plist,'pIndex':pIndex}
    return render(request,'myadmin/users/index.html',context)

def edit(request,uid):
    '''加载编辑信息页面'''
    try:
        ob = User.objects.get(id=uid)
        context = {"user": ob}
        return render(request, 'myadmin/users/edit.html', context)
    except Exception as err:
        context={"info":"没有要找到编辑信息"}
        return render(request,'myadmin/info.html',context)

def update(request,uid):
    '''执行编辑信息'''
    try:
        ob = User.objects.get(id=uid)
        ob.username = request.POST['username']
        ob.nickname=request.POST['nickname']
        ob.status=request.POST['status']
        ob.update_at=datetime.now()
        ob.save()
        context = {"info": "修改成功"}

    except Exception as err:
        print(err)
        context = {'info': '修改失败！'}

    return render(request, "myadmin/info.html", context)

def delete(request,uid):
    '''删除信息'''
    try:
        ob =User.objects.get(id=uid)
        ob.delete()
        context = {"info": "删除成功"}
    except Exception as err:
        print(err)
        context={"info":"删除失败"}
    return render(request,'myadmin/info.html',context)



def add(request):
    return render(request,'myadmin/users/add.html')


def insert(request):
    '''执行添加信息'''
    try:
        ob = User()
        ob.username = request.POST['username']
        ob.nickname = request.POST['nickname']
        import hashlib
        m = hashlib.md5()
        m.update(bytes(request.POST['password'], encoding="utf8"))
        ob.password_hash = m.hexdigest()

        ob.state = request.POST['status']
        ob.create_at=datetime.now()
        ob.update_at=datetime.now()
        ob.save()
        context = {"info": "添加成功"}

    except Exception as err:

        print(err)
        context = {"info": "添加失败"}
    return render(request, 'myadmin/info.html', context)



def resetpass(request,uid):
    '''加载密码重置页面'''
    try:
        ob = User.objects.get(id=uid)
        context = {"user": ob}
        return render(request, 'myadmin/users/resetpd.html', context)
    except Exception as err:
        context = {"info": "重置密码失败"}
        return render(request, 'myadmin/info.html', context)



def doresetpass(request,uid):
    '''执行编辑信息'''
    try:
        ob = User.objects.get(id=uid)
        import hashlib
        m = hashlib.md5()
        m.update(bytes(request.POST['password'], encoding="utf8"))
        ob.password_hash = m.hexdigest()
        ob.save()
        context = {"info": "修改成功"}

    except Exception as err:
        print(err)
        context = {'info': '修改失败！'}

    return render(request, "myadmin/info.html", context)

















