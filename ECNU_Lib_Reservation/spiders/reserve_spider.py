# -*- coding: utf-8 -*-
import json
import scrapy
import requests
import webbrowser
from scrapy_splash import SplashRequest, SplashFormRequest


class ReserveSpiderSpider(scrapy.Spider):
    name = 'reserve_spider'
    allowed_domains = ['202.120.82.2:8081']
    lib_urls = ['http://202.120.82.2:8081/ClientWeb/xcus/ic2/Default.aspx/']
    login_urls = ["http://202.120.82.2:8081/ClientWeb/pro/ajax/login.aspx",
                  "http://202.120.82.2:8081/ClientWeb/xcus/ic2/Default.aspx"]
    room_urls = [
        "http://202.120.82.2:8081/ClientWeb/xcus/a/dftdetail.aspx?classKind=1&id=3675132&name=%e4%b8%ad%e5%8c%97%e7%a0%94%e7%a9%b6%e5%ae%a4%ef%bc%88%e6%9c%a8%e9%97%a8%ef%bc%89",
        "http://202.120.82.2:8081/ClientWeb/pro/ajax/device.aspx?dev_order=&kind_order=&classkind=1&display=cld&md=d&class_id=3675132&purpose=&cld_name=default&date=20190111&act=get_rsv_sta&_=1547210020982"]
    test_urls = ["http://pythonscraping.com/pages/cookies/login.html"]
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'

    def start_requests(self):
        yield SplashRequest(url=self.test_urls[0], callback=self.start)
        # yield SplashRequest(url=self.lib_urls[0], callback=self.start)

    def start(self, response):
        session = requests.Session()
        user_info = {"id": "10132510139", "pwd": "Czy_84963496432", "act": "login"}
        login_session = session.post(self.login_urls[0], data=user_info)
        file = open("./login_session.md", "w")
        print(login_session)
        file.write(login_session.text)
        login_session = session.get(self.login_urls[1])
        print(login_session)
        file.write(login_session.text)

        room_info = {"classKind": "1", "id": "3675132", "name": "中北研究室（木门"}
        room_request = requests.post(self.room_urls[0], data=room_info)
        file = open("./room_request.md", "w")
        print(room_request)
        file.write(room_request.text)
        room_request = session.get(self.room_urls[1])
        print(room_request)
        file.write(room_request.text)

        day_request = session.get(
            "http://202.120.82.2:8081/ClientWeb/pro/ajax/device.aspx?dev_order=&kind_order=&classkind=1&display=cld&md=d&class_id=3675132&purpose=&cld_name=default&date=20190112&act=get_rsv_sta&_=1547210377777", )
        file = open("./day_request.md", "w")
        print(day_request)
        file.write(day_request.text)

    def second(self, response):
        pass
