# -*- coding: utf-8 -*-
import scrapy
import requests
import json
from urllib import parse
from cpudb.items import CpuDetailItem
from lxml import etree

name_map = {
    'Socket': 'socket',
    'Foundry': 'foundry',
    'Process Size': 'process_size',
    'Transistors': 'transistors',
    'Die Size': 'die_size',
    'Package': 'package',
    'tCaseMax': 't_case_max',
    'Frequency': 'frequency',
    'Turbo Clock': 'turbo_clock',
    'Base Clock': 'base_clock',
    'Multiplier': 'multiplier',
    'Multiplier Unlocked': 'multiplier_unlocked',
    'Voltage': 'voltage',
    'TDP': 'tdp',
    'Market': 'market',
    'Production Status': 'production_status',
    'Released': 'released',
    'Codename': 'codename',
    'Generation': 'generation',
    'Part#': 'part',
    'Memory Support': 'memory_support',
    '# of Cores': 'core',
    '# of Threads': 'thread',
    'SMP # CPUs': 'smp_cpus',
    'Integrated Graphics': 'integrated_graphics',
    'Cache L1': 'cache_l1',
    'Cache L2': 'cache_l2',
    'Cache L3': 'cache_l3',
    'Cache L4': 'cache_l4',
    'Feature': 'feature',
    'Notes': 'notes',
}


class CputravelSpider(scrapy.Spider):
    name = 'cputravel'
    allowed_domains = ['www.techpowerup.com/cpudb/']
    start_urls = ['https://www.techpowerup.com/cpudb/']
    cpu_lists_url = 'http://127.0.0.1:8000/api/cpu/'
    cpu_get_url = 'http://127.0.0.1:8000/api/getcpu/'

    main_url = 'https://www.techpowerup.com/'
    custom_settings = {
        'ITEM_PIPELINES': {'cpudb.pipelines.CpuTravelPipeline': 300}
    }

    def start_requests(self):
        resp = requests.get(self.cpu_lists_url).content

        print(resp)
        resp_json = json.loads(resp)

        for item in resp_json:
            name = item['name']

            # 检测cpu是否存在数据库中
            final_url = self.cpu_get_url + name + '/'
            resp = requests.get(final_url).content
            print(resp)
            if resp == b'[]':
                print('新的cpu信息')
                url = item['url']
                true_url = parse.urljoin(self.main_url, url)
                # if name == 'Opteron 6376':
                yield scrapy.Request(true_url, meta={'name': name}, callback=self.parse, dont_filter=True)

    def parse(self, response):
        name = response.meta['name']

        item = CpuDetailItem()
        item['name'] = name
        main_node = response.xpath('//section[contains(@class, \'details\')]')

        for sub_node in main_node:
            item_node = sub_node.xpath('./table/tr')
            h1_node = sub_node.xpath('./h1/text()')[0].extract()

            if h1_node in ['Physical', 'Performance', 'Architecture', 'Cores', 'Cache']:
                for selector in item_node:
                    th = ''
                    td = ''

                    th_nodes = selector.xpath('./th/text()')
                    th = ' '.join(map(lambda x: x.extract(), th_nodes)).replace(
                        ':', '').strip()

                    td_nodes = selector.xpath('./td')
                    td = ' '.join(map(lambda x: x.extract(), td_nodes.xpath('string(.)'))
                                  ).strip().replace('\n\t\t\t\t\t', ' ')
                    if name_map[th] == 'memory_support':
                        td = [item.strip() for item in td.split(',')]
                    if name_map[th] == 'process_size':
                        td = td[:-3]
                    if name_map[th] == 'tdp':
                        td = td[:-2]
                    if name_map[th] == 'frequency':
                        td = td[:-4]
                    if name_map[th] == 'base_clock':
                        td = td[:-4]
                    if name_map[th] == 'die_size':
                        td = td[:-4]
                    if name_map[th] == 'voltage':
                        td = td[:-2]
                    if name_map[th] == 'multiplier' and td is not 'unknown':
                        td = td[:-1]
                        if td == 'unknow':
                            td = 'unknown'
                    if name_map[th] == 'frequency':
                        td = td[:-4]
                    # if name_map[th] == 'package' and td == '':
                    # continue

                    item[name_map[th]] = td
            elif h1_node in ['Features', 'Notes']:
                for selector in item_node:
                    if h1_node == 'Features':
                        li_list = selector.xpath('./td/ul/li/text()')
                        item['feature'] = list(
                            map(lambda x: x.extract().replace(': ', '').strip(), li_list))
                        # item['feature'] = ','.join(

                    if h1_node == 'Notes':
                        notes_list = selector.xpath('./td/text()').extract()
                        item['notes'] = ','.join(notes_list)
        print(item.items())
        yield item
