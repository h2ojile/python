# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    salary = scrapy.Field()
    city = scrapy.Field()
    experience = scrapy.Field()
    education  = scrapy.Field()
    employment = scrapy.Field()
    points = scrapy.Field()
    description = scrapy.Field()
    logo = scrapy.Field()
    domain = scrapy.Field()
    scale = scrapy.Field()
    web = scrapy.Field()
    stage = scrapy.Field()
    address = scrapy.Field()
    product = scrapy.Field()
    company = scrapy.Field()
    url=scrapy.Field()