#!/usr/bin/env python
# -*- coding:utf-8 -*-
#__author__=v_zhangjunjie02
from django.shortcuts import render
from django.http import HttpResponse
from common.models import Shop
from django.core.paginator import Paginator
from  datetime import datetime
from PIL import Image
import time,os



def index(request,pIndex):
    '''浏览信息'''
    list = Shop.objects.all()
    p = Paginator(list, 10)
    if pIndex == '':
        pIndex = '1'
    pIndex = int(pIndex)
    list1 = p.page(pIndex)
    plist = p.page_range
    context = {'shoplist': list1, 'plist': plist, 'pIndex': pIndex}
    return render(request, 'myadmin/shop/index.html', context)



def add(request):
    return render(request,'myadmin/shop/add.html')



def insert(request):
    '''执行添加信息'''
    try:
        if None != request.FILES.get("cover_pic") and None != request.FILES.get("banner_pic"):
            myfile1 = request.FILES.get("cover_pic", None)
            myfile2 = request.FILES.get("banner_pic", None)

            if not myfile1 or not myfile2:
                return HttpResponse("没有上传文件信息")
            # 以时间戳命名一个新图片名称
            filename1 = str(time.time()) + "." + myfile1.name.split('.').pop()
            filename2 = str(time.time()) + "." + myfile2.name.split('.').pop()
            destination1 = open(os.path.join("./static/uploads/shop/", filename1), 'wb+')
            destination2 = open(os.path.join("./static/uploads/shop/", filename2), 'wb+')
            for chunk in myfile1.chunks():  # 分块写入文件
                destination1.write(chunk)
            destination1.close()

            for chunk in myfile2.chunks():  # 分块写入文件
                destination2.write(chunk)
            destination2.close()

            # 执行图片缩放
            im1 = Image.open("./static/uploads/shop/" + filename1)
            im2 = Image.open("./static/uploads/shop/" + filename2)
            # 缩放到375*375:
            im1.thumbnail((375, 375))
            im2.thumbnail((375, 375))
            # 把缩放后的图像用jpeg格式保存:
            im1.save("./static/uploads/shop/" + filename1, 'jpeg')
            im2.save("./static/uploads/shop/" + filename1, 'jpeg')

            im1 = Image.open("./static/uploads/shop/" + filename1)
            im2 = Image.open("./static/uploads/shop/" + filename2)
            # 缩放到75*75:
            im1.thumbnail((75, 75))
            im2.thumbnail((75, 75))
            # 把缩放后的图像用jpeg格式保存:
            im1.save("./static/uploads/shop/s_" + filename1, 'jpeg')
            im2.save("./static/uploads/shop/s_" + filename2, 'jpeg')

            cover_pic= filename1
            banner_pic = filename2
        ob = Shop()
        ob.name = request.POST['name']
        ob.cover_pic = cover_pic
        ob.banner_pic = banner_pic
        ob.address=request.POST['address']
        ob.phone=request.POST['phone']
        ob.state = 1
        ob.create_at = datetime.now()
        ob.update_at = datetime.now()
        ob.save()
        context = {"info": "添加成功"}

    except Exception as err:

        print(err)
        context = {"info": "添加失败"}
    return render(request, 'myadmin/info.html', context)


def delete(request,sid):
    '''删除信息'''
    try:
        ob = Shop.objects.get(id=sid)
        ob.delete()
        context = {"info": "删除成功"}
    except Exception as err:
        print(err)
        context = {"info": "删除失败"}
    return render(request, 'myadmin/info.html', context)


def edit(request,sid):
    '''加载编辑信息页面'''
    try:
        ob = Shop.objects.get(id=sid)
        context = {"shop": ob}
        return render(request, 'myadmin/shop/edit.html', context)
    except Exception as err:
        context = {"info": "没有要找到编辑信息"}
        return render(request, 'myadmin/info.html', context)


def update(request,sid):
    '''执行编辑信息'''
    try:
        b = False
        oldcover_pic = request.POST['oldcover_pic']
        oldbanner_pic = request.POST['oldbanner_pic']
        if None != request.FILES.get("cover_pic") and None != request.FILES.get("banner_pic"):
            myfile1 = request.FILES.get("cover_pic", None)
            myfile2 = request.FILES.get("banner_pic", None)

            if not myfile1 or not myfile2:
                return HttpResponse("没有上传文件信息")
            # 以时间戳命名一个新图片名称
            filename1 = str(time.time()) + "." + myfile1.name.split('.').pop()
            filename2 = str(time.time()) + "." + myfile2.name.split('.').pop()
            destination1 = open(os.path.join("./static/uploads/shop/", filename1), 'wb+')
            destination2 = open(os.path.join("./static/uploads/shop/", filename2), 'wb+')
            for chunk in myfile1.chunks():  # 分块写入文件
                destination1.write(chunk)
            destination1.close()

            for chunk in myfile2.chunks():  # 分块写入文件
                destination2.write(chunk)
            destination2.close()

            # 执行图片缩放
            im1 = Image.open("./static/uploads/shop/" + filename1)
            im2 = Image.open("./static/uploads/shop/" + filename2)
            # 缩放到375*375:
            im1.thumbnail((375, 375))
            im2.thumbnail((375, 375))
            # 把缩放后的图像用jpeg格式保存:
            im1.save("./static/uploads/shop/" + filename1, 'jpeg')
            im2.save("./static/uploads/shop/" + filename1, 'jpeg')

            im1 = Image.open("./static/uploads/shop/" + filename1)
            im2 = Image.open("./static/uploads/shop/" + filename2)
            # 缩放到75*75:
            im1.thumbnail((75, 75))
            im2.thumbnail((75, 75))
            # 把缩放后的图像用jpeg格式保存:
            im1.save("./static/uploads/shop/s_" + filename1, 'jpeg')
            im2.save("./static/uploads/shop/s_" + filename2, 'jpeg')
            b = True
            cover_pic= filename1
            banner_pic = filename2

        else:
            cover_pic = oldcover_pic
            banner_pic = oldbanner_pic

        ob = Shop.objects.get(id=sid)
        ob.name = request.POST['name']
        ob.cover_pic = cover_pic
        ob.banner_pic = banner_pic
        ob.address = request.POST['address']
        ob.phone = request.POST['phone']
        ob.status = request.POST['status']
        ob.update_at = datetime.now()
        ob.save()
        context = {"info": "修改成功"}
        if b:
           os.remove("./static/uploads/shop/s_" + oldcover_pic)  # 执行老图片删除
           os.remove("./static/uploads/shop/" + oldcover_pic)  # 执行老图片删除
           os.remove("./static/uploads/shop/s_" + oldbanner_pic)  # 执行老图片删除
           os.remove("./static/uploads/shop/" + oldbanner_pic)  # 执行老图片删除
    except Exception as err:
        print(err)
        context = {'info': '修改失败！'}
        if b:
            os.remove("./static/uploads/shop/s_" + cover_pice)  # 执行新图片删除
            os.remove("./static/uploads/shop/s_" + banner_pic)
            os.remove("./static/uploads/shop/" + cover_pice)  # 执行新图片删除
            os.remove("./static/uploads/shop/" + banner_pic)  # 执行新图片删除
    return render(request, "myadmin/info.html", context)
