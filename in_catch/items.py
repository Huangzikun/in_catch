# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class InCatchItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

# offer类
class MobiwikOfferItem(scrapy.Item):
    offerId = scrapy.Field()
    verticalName = scrapy.Field()
    isOffline = scrapy.Field()
    lastUpdated = scrapy.Field(serializer=str)

class OfferItem(scrapy.Item):
    typeId = scrapy.Field()#类型id
    offerId = scrapy.Field()#offerid跳转用
    merchantName = scrapy.Field()#产品名字
    productTitle = scrapy.Field()#title
    logoUrl = scrapy.Field()
    couponCode = scrapy.Field()
    endDate = scrapy.Field()
    startDate = scrapy.Field()
    lastUpdated = scrapy.Field(serializer=str)


