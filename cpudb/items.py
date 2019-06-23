# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CpudbItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    href = scrapy.Field()


class CpuDetailItem(scrapy.Item):
    # physical
    socket = scrapy.Field()
    foundry = scrapy.Field()
    process_size = scrapy.Field()
    transistors = scrapy.Field()
    die_size = scrapy.Field()
    package = scrapy.Field()
    tCaseMax = scrapy.Field()

    # performance_node
    frequency = scrapy.Field()
    turbo_clock = scrapy.Field()
    base_clock = scrapy.Field()
    multiplier = scrapy.Field()
    multiplier_unlocked = scrapy.Field()
    voltage = scrapy.Field()
    tdp = scrapy.Field()

    # architecture
    market = scrapy.Field()
    production_status = scrapy.Field()

    released = scrapy.Field()
    codename = scrapy.Field()
    generation = scrapy.Field()
    part = scrapy.Field()
    memory_support = scrapy.Field()

    # core
    cores = scrapy.Field()
    threads = scrapy.Field()
    smp_cpus = scrapy.Field()
    integrated_graphics = scrapy.Field()

    # cache
    cache_l1 = scrapy.Field()
    cache_l2 = scrapy.Field()
    cache_l3 = scrapy.Field()
    cache_l4 = scrapy.Field()
