#!/usr/bin/env python
# -*- coding:utf-8 -*-
#__author__=v_zhangjunjie02
from django.shortcuts import render
from common.models import Category,Shop,Product
from django.core.paginator import Paginator
from django.http import HttpResponse
from  datetime import datetime
from PIL import Image
import time,os



def index(request,pIndex):
    '''浏览信息'''
    list = Product.objects.all()
    for ob in list:
        shoplist = Shop.objects.filter(id=ob.shop_id)
        for vo in shoplist:
            ob.shopname = vo.name
        typelist = Category.objects.filter(id=ob.category_id)
        for va in typelist:
            ob.typename= va.name
    p = Paginator(list, 10)
    if pIndex == '':
        pIndex = '1'
    pIndex = int(pIndex)
    list1 = p.page(pIndex)
    plist = p.page_range
    context = {'typelist': list1, 'plist': plist, 'pIndex': pIndex}
    return render(request,'myadmin/product/index.html',context)

def add(request):
    shoplist=Shop.objects.all()
    typelist=Category.objects.all()
    context={"shoplist":shoplist,"typelist":typelist}
    return render(request,'myadmin/product/add.html',context)

def insert(request):
    try:
        myfile = request.FILES.get("pic", None)

        if not myfile:
            return HttpResponse("没有上传文件信息！")
        # 以时间戳命名一个新图片名称
        filename = str(time.time()) + "." + myfile.name.split('.').pop()
        destination = open(os.path.join("./static/uploads/product/", filename), 'wb+')
        for chunk in myfile.chunks():  # 分块写入文件
            destination.write(chunk)
        destination.close()

        # 执行图片缩放
        im = Image.open("./static/uploads/product/" + filename)
        # 缩放到375*375:
        im.thumbnail((375, 375))
        # 把缩放后的图像用jpeg格式保存:
        im.save("./static/uploads/product/" + filename, 'jpeg')

        im = Image.open("./static/uploads/product/" + filename)
        # 缩放到75*75:
        im.thumbnail((75, 75))
        # 把缩放后的图像用jpeg格式保存:
        im.save("./static/uploads/product/s_" + filename, 'jpeg')

        picname = filename

        ob=Product()
        ob.name=request.POST['name']
        ob.shop_id=request.POST['shoptypeid']
        ob.category_id=request.POST['typeid']
        ob.cover_pic=picname
        ob.price=request.POST['price']
        ob.status=1
        ob.create_at=datetime.now()
        ob.update_at=datetime.now()
        ob.save()
        context={"info":"添加成功"}

    except Exception as err:
        print(err)
        context={"info":"添加失败"}
    return render(request,'myadmin/info.html',context)

def delete(request,pid):
    try:
        ob=Product.objects.get(id=pid)
        picname=ob.cover_pic
        #执行图片删除
        os.remove("./static/uploads/product/s_" + picname)
        os.remove("./static/uploads/product/" + picname)
        ob.delete()
        context={"info":"删除成功"}
    except Exception as err:
        print(err)
        context={"info":"未找到要删除的信息"}
    return render(request,'myadmin/info.html',context)


def edit(request,pid):
    list=Product.objects.get(id=pid)
    ctype=Category.objects.get(id=pid)
    ctypelist=Category.objects.all()
    stype=Shop.objects.get(id=pid)
    stypelist=Shop.objects.all()
    context={"prolist":list,"ctype":ctype,"ctypelist":ctypelist,"stype":stype,"stypelist":stypelist}
    return render(request,'myadmin/product/edit.html',context)




def update(request,pid):
    try:
        b = False
        oldpicname = request.POST['oldpicname']
        if None != request.FILES.get("pic"):
            myfile = request.FILES.get("pic", None)
            if not myfile:
                return HttpResponse("没有上传文件信息！")
            # 以时间戳命名一个新图片名称
            filename = str(time.time()) + "." + myfile.name.split('.').pop()
            destination = open(os.path.join("./static/uploads/product/", filename), 'wb+')
            for chunk in myfile.chunks():  # 分块写入文件
                destination.write(chunk)
            destination.close()
            # 执行图片缩放
            im = Image.open("./static/uploads/product/" + filename)
            # 缩放到375*375:
            im.thumbnail((375, 375))
            # 把缩放后的图像用jpeg格式保存:
            im.save("./static/uploads/product/" + filename, 'jpeg')
            # 缩放到75*75:
            im.thumbnail((75, 75))
            # 把缩放后的图像用jpeg格式保存:
            im.save("./static/uploads/product/s_" + filename, 'jpeg')
            b = True
            picname = filename
        else:
            picname = oldpicname
        ob=Product.objects.get(id=pid)
        ob.name=request.POST['name']
        ob.shop_id=request.POST['shopid']
        ob.category_id=request.POST['categoryid']
        ob.cover_pic=picname
        ob.price=request.POST['price']
        ob.status = request.POST['status']
        ob.update_at=datetime.now()
        ob.save()
        context = {'info': '修改成功！'}
        if b:
            print("A")

    except Exception as err:
        print(err)
        context = {'info': '修改失败！'}
        if b:
            os.remove("./static/uploads/product/s_" + picname)  # 执行新图片删除
            os.remove("./static/uploads/product/" + picname)  # 执行新图片删除
    return render(request,'myadmin/info.html',context)


