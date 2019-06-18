# -*- coding: utf-8 -*-
import scrapy
from cpudb.codename import code_name


class CpugetSpider(scrapy.Spider):
    name = 'cpuget'
    allowed_domains = ['www.techpowerup.com/cpudb/']
    start_urls = []

    def __init__(self, *args, **kwargs):
        super(CpugetSpider, self).__init__(*args, **kwargs)

        url = 'https://www.techpowerup.com/cpudb/?codename={}&sort=name'

        for codename in code_name:
            new_codename = codename.replace(' ', '%20')
            new_url = url.replace('{}', new_codename)

            self.start_urls.append(new_url)
            print(new_url)

    def parse(self, response):
        for each in response.xpath('//tbody/tr/td[1]/a'):
            name = each.xpath('./text()')
            href = each.xpath('./@href')
            yield
