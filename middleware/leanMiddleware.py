from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin


class TotalMiddleware(MiddlewareMixin):

    def process_request(self,request):
        print(request.path)
        ip = request.META.get('REMOTE_ADDR')
        print(ip)
        print(request.META.get('HTTP_USER_AGENT'))
        # if request.META.get('HTTP_USER_AGENT') == 'Python-urllib/3.5':
        #     return HttpResponse('小爬虫，别爬了，回家喝奶洗洗睡吧')
        #
        # if request.path == '/myapp/dogetphone/':
        #     if request.GET.get('username') == 'mmp':
        #         return HttpResponse('恭喜你抢到了小米神机，不要999，只要9.8')
        #     elif request.GET.get('username') == 'rock':
        #         return HttpResponse('正在排队，稍后继续')
        # if cache.get(ip):
        #     return HttpResponse('小爬虫，别爬了，该去睡觉了')
        # else:
        #     cache.set(ip,'123',timeout=10)

    # def process_exception(self,request,exception):
    #     return redirect(reverse('myapp:hello'))