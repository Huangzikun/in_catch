# -*- coding: utf-8 -*-
import scrapy
import json
import csv
from in_catch.items import MobiwikOfferItem
from in_catch.items import OfferItem
from scrapy.shell import inspect_response
import datetime
from scrapy import Request
import urllib.parse
from in_catch.settings import USER_AGENT_LIST
import random


class MobiwikspiderSpider(scrapy.Spider):
    name = 'mobiwikspider'
    allowed_domains = ['webapi.mobikwik.com']
    start_urls = ['https://webapi.mobikwik.com/walletapis/offers/meta?listSize=9']

    headers = {
                'User-Agent': random.choice(USER_AGENT_LIST),
                "Host":"webapi.mobikwik.com",
                "Connection":"keep-alive",
                "X-MClient":0,
                "Accept":"application/json, text/plain, */*",
                "Sec-Fetch-Dest":"empty",
                "DNT":1,
                "Origin":"https://www.mobikwik.com",
                "Sec-Fetch-Site":"same-site",
                "ec-Fetch-Mode":"cors",
                "Referer":"https://www.mobikwik.com/",
                "Accept-Encoding":"gzip, deflate, br",
                "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8"
            }

    def start_requests(self):
        item = []
        for url in self.start_urls:
            item.append(Request(url=url,headers=self.headers))
        
        return item

    def parse(self, response):
        if(response.status != 200) :
            return

        offerItem = MobiwikOfferItem()
        rs = json.loads(response.text)
        if(rs['success'] != True) :
            return

        verticalList = rs['data']['verticalList']
        
        for vertical in verticalList:
            offerItem['offerId'] = vertical['id']
            offerItem['verticalName'] = vertical['verticalName']
            offerItem['isOffline'] = vertical['isOffline']
            offerItem['lastUpdated'] = datetime.datetime.now()

            yield offerItem

            url = 'https://webapi.mobikwik.com/walletapis/offers/offersForVerticals?' + urllib.parse.urlencode({
                    "vertical":vertical['id'],
                    "page":1,
                    "listSize":12
                    })

            
            
            yield Request(url=url, callback=self.parseOffer, headers=self.headers)

        pass


    def parseOffer(self, response):
        if(response.status != 200) :
            return

        offerItem = OfferItem()
        rs = json.loads(response.text)
        if(rs['success'] != True) :
            return
        
        data = rs['data']
        typeId = data['id']

        offers = data['offers']
        for offer in offers:
            offerItem['typeId'] = typeId
            offerItem['offerId'] = offer['offerId']
            offerItem['merchantName'] = offer['merchantName']
            offerItem['productTitle'] = offer['productTitle']
            offerItem['logoUrl'] = offer['logoUrl']
            offerItem['lastUpdated'] = datetime.datetime.now()
            offerItem['couponCode'] = offer['couponCode']
            offerItem['endDate'] = offer['endDate']
            offerItem['startDate'] = offer['startDate']

            yield offerItem
        
        pagination = rs['pagination']
        curPage = pagination['page']
        count = pagination['count']
        size = pagination['size']


        usePage = curPage+1
        if(size * curPage < count) :
            url = 'https://webapi.mobikwik.com/walletapis/offers/offersForVerticals?' + urllib.parse.urlencode({
                    "vertical":typeId,
                    "page":usePage,
                    "listSize":size
                    })
            
            yield Request(url=url, callback=self.parseOffer, headers=self.headers)

        pass
