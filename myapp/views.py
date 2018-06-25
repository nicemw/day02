import random
from time import sleep

from django import template


from django.core.cache import cache
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader

from django.views.decorators.cache import cache_page

from myapp.models import joke


def index(request):
    # print(request.META.get('REMOTE_ADDR'))
    return render(request,'index.html')



@cache_page(20)
def get_phone(request):

    sleep(5)
    print('从数据库加载')
    return render(request, 'GetXiaoMiPhone.html')

def get_telephone(request):
    # 去缓存中查找，缓存中有，直接返回；缓存中没有去数据库中查找，添加到缓存中并返回
    result = cache.get('get_telephone')
    if result:
        return HttpResponse(result)
    else:
        sleep(10)
        template = loader.get_template('GetXiaoMiPhone.html')
        result = template.render()
        print(result)

        cache.set('get_telemphone',result)
        return HttpResponse(result)

def genrate_response(request):
    result = """
        <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>抢购</title>
</head>
<body>
<form action="/myapp/dogetphone/">
    <span>用户名：</span><input type="text" name="username" placeholder="亲输入用户名">
    <br>
    <input type="submit">
</form>
</body>
</html>

    """
    return HttpResponse(result)

def do_get_phone(request):

    username = request.GET.get('username')
    if random.randrange(100)>85:
        return HttpResponse('恭喜，%s抢购小米mix2成功'%username)
    return HttpResponse('正在排队')

def get_error(request):
    if random.randrange(100)>80:
        num = 1/0
    return HttpResponse('错误去哪了')





def jokes(request,page):
    joke_list = joke.objects.all()
    paginator = Paginator(joke_list,3)
    # 获取某一页的数据
    page_object = paginator.page(page)

    page_range = paginator.page_range
    return render(request, 'jokelist.html', context={'page_object': page_object, "page_range": page_range})