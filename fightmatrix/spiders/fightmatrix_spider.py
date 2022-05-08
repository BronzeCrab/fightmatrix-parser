import scrapy


class FightmatrixSpiderSpider(scrapy.Spider):
    name = 'fightmatrix_spider'
    allowed_domains = ['fightmatrix.com']
    start_urls = ['http://fightmatrix.com/']

    def parse(self, response):
        pass
