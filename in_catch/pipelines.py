# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv
from in_catch.items import MobiwikOfferItem
from in_catch.items import OfferItem

class InCatchPipeline(object):
    def process_item(self, item, spider):
        return item


class MobiwikOfferPipeline(object):
    def process_item(self, item, spider):
        if(isinstance(item, MobiwikOfferItem)) :
            f = open('./MobiwikOffer.csv','a+', newline='')
            writer = csv.writer(f)
            writer.writerow(
                (item['offerId'], item['verticalName'], item['isOffline'], item['lastUpdated'])
            )

        return item

class OfferPipeline(object):
    def process_item(self, item, spider):
        if(isinstance(item, OfferItem)) :
            f = open('./Offer.csv','a+', newline='')
            writer = csv.writer(f)

            pcJumpUrl = 'https://www.mobikwik.com/offers/' + item['typeId'] + '/' + item['offerId']
            mJumpUrl = 'https://m.mobikwik.com/offers/' + item['typeId'] +  '/' + item['offerId']
            writer.writerow(
                (item['typeId'], 
                item['offerId'],
                item['merchantName'], 
                item['productTitle'],
                item['logoUrl'],
                item['couponCode'],
                pcJumpUrl,
                mJumpUrl,
                item['startDate'],
                item['endDate'],
                item['lastUpdated']
                )
            )

        return item



