# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CpudbItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field(default='')
    href = scrapy.Field(default='')


class CpuDetailItem(scrapy.Item):
    name = scrapy.Field(default='')
    # physical
    socket = scrapy.Field(default='')
    foundry = scrapy.Field(default='')
    process_size = scrapy.Field(default='')
    transistors = scrapy.Field(default='')
    die_size = scrapy.Field(default='')
    package = scrapy.Field(default='')
    t_case_max = scrapy.Field(default='')

    # performance_node
    frequency = scrapy.Field(default='')
    turbo_clock = scrapy.Field(default='')
    base_clock = scrapy.Field(default='')
    multiplier = scrapy.Field(default='')
    multiplier_unlocked = scrapy.Field(default='')
    voltage = scrapy.Field(default='')
    tdp = scrapy.Field(default='')

    # architecture
    market = scrapy.Field(default='')
    production_status = scrapy.Field(default='')

    released = scrapy.Field(default='')
    codename = scrapy.Field(default='')
    generation = scrapy.Field(default='')
    part = scrapy.Field(default='')
    memory_support = scrapy.Field(default='')

    # core
    cores = scrapy.Field(default='')
    threads = scrapy.Field(default='')
    smp_cpus = scrapy.Field(default='')
    integrated_graphics = scrapy.Field(default='')

    # cache
    cache_l1 = scrapy.Field(default='')
    cache_l2 = scrapy.Field(default='')
    cache_l3 = scrapy.Field(default='')
    cache_l4 = scrapy.Field(default='')

    feature = scrapy.Field(default='')
    notes = scrapy.Field(default='')
