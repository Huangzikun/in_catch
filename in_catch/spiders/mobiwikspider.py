# -*- coding: utf-8 -*-
import scrapy
import json
import csv
from in_catch.items import MobiwikOfferItem
from scrapy.shell import inspect_response
import datetime


class MobiwikspiderSpider(scrapy.Spider):
    name = 'mobiwikspider'
    allowed_domains = ['webapi.mobikwik.com']
    start_urls = ['https://webapi.mobikwik.com/walletapis/offers/meta?listSize=9']


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

        pass
