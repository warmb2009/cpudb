# -*- coding: utf-8 -*-
import scrapy
import requests
import json
from urllib import parse
from cpudb.items import CpuDetailItem


class CputravelSpider(scrapy.Spider):
    name = 'cputravel'
    allowed_domains = ['www.techpowerup.com/cpudb/']
    start_urls = ['https://www.techpowerup.com/cpudb/']
    cpu_lists_url = 'http://127.0.0.1:8000/api/cpu/'

    main_url = 'https://www.techpowerup.com/'

    def start_requests(self):
        resp = requests.get(self.cpu_lists_url).content
        print(resp)
        resp_json = json.loads(resp)

        for item in resp_json:
            name = item['name']
            url = item['url']
            true_url = parse.urljoin(self.main_url, url)
            yield Request(true_url, meta={'name': name}, call_back=self.parse, dont_filter=True)

    def parse(self, response):
        name = response.meta['name']
        item = CpuDetailItem()

        physical_node = response.xpath('//section[@class=\'details\'][1]')
        performance_node = response.xpath('//section[@class=\'details\'][2]')
        architecture_node = response.xpath('//section[@class=\'details\'][3]')
        cores_node = response.xpath('//section[@class=\'details\'][4]')
        cache_node = response.xpath('//section[@class=\'details\'][5]')
        features_node = response.xpath('//section[@class=\'details\'][6]')

        # physical
        item['socket'] = physical_node.xpath(
            './table/tbody/tr[1]/td/text()')  # 针数
        item['foundry'] = physical_node.xpath(
            './table/tbody/tr[2]/td/text()')  # 厂家
        item['process_size'] = physical_node.xpath(
            './table/tbody/tr[3]/td/text()')  # 封装面积
        item['transistors'] = physical_node.xpath(
            './table/tbody/tr[4]/td/text()')  # 晶体管数量
        item['die_size'] = physical_node.xpath(
            './table/tbody/tr[5]/td/text()')  # 芯片尺寸
        item['package'] = physical_node.xpath(
            './table/tbody/tr[6]/td/text()')  # 封装模式
        item['tCaseMax'] = physical_node.xpath(
            './table/tbody/tr[7]/td/text()')  # 稳定运行的最大温度

        # performance_node
        item['frequency'] = performance_node.xpath(
            './table/tbody/tr[1]/td/text()')  # 频率
        item['turbo_clock'] = performance_node.xpath(
            './table/tbody/tr[2]/td/text()')  # 睿频
        item['base_clock'] = performance_node.xpath(
            './table/tbody/tr[3]/td/text()')  # 基础频率
        item['multiplier'] = performance_node.xpath(
            './table/tbody/tr[4]/td/text()')  # 倍频
        item['multiplier_unlocked'] = performance_node.xpath(
            './table/tbody/tr[5]/td/text()')  # 解锁倍频
        item['voltage'] = performance_node.xpath(
            './table/tbody/tr[6]/td/text()')  # 电压
        item['tdp'] = performance_node.xpath(
            './table/tbody/tr[7]/td/text()')  # 功率

        # architecture
        item['market'] = architecture_node.xpath(
            './table/tbody/tr[1]/td/text()')  # 面向市场
        item['production_status'] = architecture_node.xpath(
            './table/tbody/tr[2]/td/text()')  # 生产状态
        item['released'] = architecture_node.xpath(
            './table/tbody/tr[3]/td/text()')  # 发布时间
        item['codename'] = architecture_node.xpath(
            './table/tbody/tr[4]/td/text()')  # 代号
        item['generation'] = architecture_node.xpath(
            './table/tbody/tr[5]/td/text()')  # 代
        item['part'] = architecture_node.xpath('./table/tbody/tr[6]/td/text()')
        item['memory_support'] = architecture_node.xpath(
            './table/tbody/tr[7]/td/text()')  # 支持的内存

        # core
        item['cores'] = cores_node.xpath(
            './table/tbody/tr[1]/td/text()')  # 核心数
        item['threads'] = cores_node.xpath(
            './table/tbody/tr[2]/td/text()')  # 线程数
        item['smp_cpus'] = cores_node.xpath('./table/tbody/tr[3]/td/text()')
        item['integrated_graphics'] = cores_node.xpat(
            './table/tbody/tr[4]/td/text()')  # 核显

        # cache
        item['cache_l1'] = cache_node.xpath(
            './table/tbody/tr[1]/td/text()')  # 一级缓存
        item['cache_l2'] = cache_node.xpath(
            './table/tbody/tr[2]/td/text()')  # 二级缓存
        item['cache_l3'] = cache_node.xpath(
            './table/tbody/tr[3]/td/text()')  # 三级缓存
        item['cache_l4'] = cache_node.xpath(
            './table/tbody/tr[4]/td/text()')  # 四级缓存
