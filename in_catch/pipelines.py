# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv

class InCatchPipeline(object):
    def process_item(self, item, spider):
        return item


class MobiwikOfferPipeline(object):
    def process_item(self, item, spider):
        f = open('./MobiwikOffer.csv','a+', newline='')
        writer = csv.writer(f)
        writer.writerow(
            (item['offerId'], item['verticalName'], item['isOffline'], item['lastUpdated'])
        )

        return item



