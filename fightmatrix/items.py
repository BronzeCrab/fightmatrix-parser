# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FightmatrixItem(scrapy.Item):
    name = scrapy.Field()
    division = scrapy.Field()
    current_ranking = scrapy.Field()
    ufc_record = scrapy.Field()
