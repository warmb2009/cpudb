# -*- coding: utf-8 -*-
import scrapy
from cpudb.codename import code_name
from cpudb.items import CpudbItem


class CpugetSpider(scrapy.Spider):
    name = 'cpuget'
    allowed_domains = ['www.techpowerup.com/cpudb/']
    start_urls = []

    custom_settings = {
        'ITEM_PIPELINES': {'cpudb.pipelines.CpudbPipeline': 300}
    }

    def __init__(self, *args, **kwargs):
        super(CpugetSpider, self).__init__(*args, **kwargs)

        url = 'https://www.techpowerup.com/cpudb/?codename={}&sort=name'

        for codename in code_name:
            new_codename = codename.replace(' ', '%20')
            new_url = url.replace('{}', new_codename)

            self.start_urls.append(new_url)
            print(new_url)

    def parse(self, response):
        for each in response.xpath('//table[@class=\'processors\']/tr/td[1]/a'):
            item = CpudbItem()
            item['name'] = each.xpath('./text()').extract()[0]
            item['href'] = each.xpath('./@href').extract()[0]

            yield item
