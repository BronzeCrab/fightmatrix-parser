import scrapy


class FightmatrixItem(scrapy.Item):
    name = scrapy.Field()
    division = scrapy.Field()
    current_ranking = scrapy.Field()
    ufc_record = scrapy.Field()
