from django.shortcuts import render
from django.utils.deprecation import MiddlewareMixin

ads = ['123','adf','werha','kxfhg']
good = ['该发工资了','我看见你...']
class AdvertisMiddleware(MiddlewareMixin):
    def process_request(self,req):
        path = req.path
        if path=='/t06/test':
            leads = [
                '10.0.120.169',
            ]
            print(req.META.get("REMOTE_ADDR"))
            ip = req.META.get("REMOTE_ADDR")
            if ip in leads:
                return render(req,'advs.html',{'ads':good})
            else:
                return render(req,'advs.html',{'ads':ads})