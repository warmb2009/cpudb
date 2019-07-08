# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import requests
import json


class CpudbPipeline(object):
    def process_item(self, item, spider):
        data = {'name': item['name'], 'url': item['href']}

        posturl = 'http://127.0.0.1:8000/api/cpu/'

        proxy = ''
        proxies = {}

        r = requests.post(posturl, data=json.dumps(data), headers={
                          'Content-Type': 'application/json'})
        print(r.json())
        return item


class CpuTravelPipeline(object):
    def process_item(self, item, spider):
        for field in item.fields:
            item.setdefault(field, 'NULL')

        item_dict = dict(item)
        print(item_dict)

        posturl = 'http://127.0.0.1:8000/api/travelcpu/'
        r = requests.post(posturl, data=json.dumps(item_dict), headers={
                          'Content-Type': 'application/json'})
        json_text = json.dumps(item_dict) + ', \n'
        return json_text
