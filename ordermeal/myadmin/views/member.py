
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
    list=Member.objects.all()
    p=Paginator(list,10)
    if pIndex == '':
        pIndex = '1'
    pIndex=int(pIndex)
    list1=p.page(pIndex)
    plist=p.page_range
    context={'memberlist':list1,'plist':plist,'pIndex':pIndex}
    return render(request,'myadmin/member/index.html',context)

def edit(request,mid):
    '''加载编辑信息页面'''
    try:
        ob = Member.objects.get(id=mid)
        context = {"member": ob}
        return render(request, 'myadmin/member/edit.html', context)
    except Exception as err:
        context={"info":"没有要找到编辑信息"}
        return render(request,'myadmin/info.html',context)

def update(request,mid):
    '''执行编辑信息'''
    try:
        b = False
        oldpicname = request.POST['oldpicname']
        if None != request.FILES.get("pic"):
            myfile = request.FILES.get("pic", None)

            if not myfile:
                return HttpResponse("没有上传文件信息！")
            # 以时间戳命名一个新图片名称
            filename = str(time.time()) + "." + myfile.name.split('.').pop()
            destination = open(os.path.join("./static/uploads/member/", filename), 'wb+')
            for chunk in myfile.chunks():  # 分块写入文件
                destination.write(chunk)
            destination.close()

            # 执行图片缩放
            im = Image.open("./static/uploads/member/" + filename)
            # 缩放到375*375:
            im.thumbnail((375, 375))
            # 把缩放后的图像用jpeg格式保存:
            im.save("./static/uploads/member/" + filename, 'jpeg')

            im = Image.open("./static/uploads/member/" + filename)
            # 缩放到75*75:
            im.thumbnail((75, 75))
            # 把缩放后的图像用jpeg格式保存:
            im.save("./static/uploads/member/s_" + filename, 'jpeg')
            b = True
            picname = filename
        else:
            picname = oldpicname

        ob = Member.objects.get(id=mid)

        ob.nickname = request.POST['nickname']
        ob.avatar=picname
        ob.mobile=request.POST['mobile']
        ob.status=request.POST['status']
        ob.update_at=datetime.now()
        ob.save()
        context = {"info": "修改成功"}
        # if b:
        #    os.remove("./static/uploads/member/s_" + oldpicname)  # 执行老图片删除
        #    os.remove("./static/uploads/member/" + oldpicname)  # 执行老图片删除
    except Exception as err:
        print(err)
        context = {'info': '修改失败！'}
        if b:
            os.remove("./static/uploads/member/s_" + picname)  # 执行新图片删除
            os.remove("./static/uploads/member/" + picname)  # 执行新图片删除
    return render(request, "myadmin/info.html", context)

def delete(request,mid):
    '''删除信息'''
    try:
        ob = Member.objects.get(id=mid)
        ob.delete()
        context = {"info": "删除成功"}
    except Exception as err:
        print(err)
        context={"info":"删除失败"}
    return render(request,'myadmin/info.html',context)

















