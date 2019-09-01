import random

import time
from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin


class HelloMiddle(MiddlewareMixin):

    def process_request(self, request):
        print(request.META.get("REMOTE_ADDR"))

        ip = request.META.get("REMOTE_ADDR")

        # if request.path == "/app/getphone/":
        #
        #     if ip == "127.0.0.1":
        #
        #         if random.randrange(100) > 20:
        #
        #             return HttpResponse("恭喜您免费获取小米8 256G版")
        #
        # if request.path == "/app/getticket/":
        #     if ip.startswith("10.0.122.1"):
        #         return HttpResponse("已抢光")
        #
        # if request.path == "/app/search/":
        #     result = cache.get(ip)
        #     if result:
        #         return HttpResponse("您的访问过于频繁，请10秒之后再次搜索")
        #     cache.set(ip, ip, timeout=10)

        # black_list = cache.get('black',[])
        #
        # if ip in black_list:
        #     return HttpResponse("黑名单用户，凉凉")
        #
        # requests = cache.get(ip, [])
        #
        # while requests and time.time() - requests[-1] > 60:
        #     requests.pop()
        #
        # requests.insert(0, time.time())
        # cache.set(ip, requests, timeout=60)
        #
        # if len(requests) > 30:
        #     black_list.append(ip)
        #     cache.set('black', black_list, timeout=60*60*24)
        #     return HttpResponse("小爬虫小黑屋里呆着吧")
        #
        # if len(requests) > 10:
        #     return HttpResponse("请求次数过于频繁，小爬虫回家睡觉吧")

        pass

    def process_exception(self, request, exception):
        print(request, exception)
        return redirect(reverse('app:index'))


class TwoMiddle(MiddlewareMixin):

    def process_request(self, request):

        print("Two Middleware")