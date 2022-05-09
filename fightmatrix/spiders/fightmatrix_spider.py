import scrapy
from fightmatrix.items import FightmatrixItem


class FightmatrixSpiderSpider(scrapy.Spider):
    name = 'fightmatrix_spider'
    allowed_domains = ['fightmatrix.com']
    start_urls = ['https://www.fightmatrix.com/mma-ranks/']

    def parse(self, response):
        for division_link in response.xpath('//td/a/@href').extract():
            if (
                'pound' not in division_link.lower() and 
                'division' not in division_link.lower()
            ):  
                div_name = division_link.split()[-1]
                yield response.follow(
                    '{0}?page=0'.format(response.url),
                    callback=self.parse_div,
                    meta={
                        'page_num': 1,
                        'div_name': div_name,
                    },
                )

    def parse_div(self, response):
        pass


    def parse_fighter(self, response):
        f_m_item = FightmatrixItem()
        f_m_item['division'] = division_link
        yield f_m_item