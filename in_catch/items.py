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


