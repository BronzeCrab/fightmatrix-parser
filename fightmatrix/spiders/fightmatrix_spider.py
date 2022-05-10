import scrapy
from fightmatrix.items import FightmatrixItem


class FightmatrixSpider(scrapy.Spider):
    name = 'fightmatrix_spider'
    allowed_domains = ['fightmatrix.com']
    start_urls = ['https://www.fightmatrix.com/mma-ranks/']

    def parse(self, response):
        for division_link in response.xpath('//td/a/@href').extract():
            if (
                'pound' not in division_link.lower() and 
                'division' not in division_link.lower()
            ):  
                div_name = division_link.split('/')[-2]
                yield response.follow(
                    '{0}?PageNum=1'.format(division_link),
                    callback=self.parse_division,
                    meta={
                        'page_num': 1,
                        'div_name': div_name,
                    },
                )

    def parse_division(self, response):
        page_num = response.meta.get('page_num')
        div_name = response.meta.get('div_name')
        fighters_on_page = False
        for fighter_link in response.xpath(
            '//td/a[@class="sherLink"]/@href',
        ).extract():
            fighters_on_page = True
            yield response.follow(
                fighter_link,
                callback=self.parse_fighter,
                meta={
                    'div_name': div_name,
                },
            )
        # go to next page if are some fighters
        if fighters_on_page:
            div_url = response.url
            div_url = div_url[:div_url.index('?PageNum')]
            page_num += 1
            yield response.follow(
                '{0}?PageNum={1}'.format(div_url, page_num),
                callback=self.parse_division,
                meta={
                    'page_num': page_num,
                    'div_name': div_name,
                },
            )


    def parse_fighter(self, response):
        f_m_item = FightmatrixItem()
        name = response.xpath(
            '//div[@class="posttitle"]/h1/a/text()',
        ).extract_first()
        div_name = response.meta.get('div_name')


        current_ranking = ''
        for ind, ranking in enumerate(response.xpath(
            '//td[@class="tdRank"]/div[@class="leftCol"]/a/text()',
        ).extract()):
            if ind == 0:
                current_ranking += ranking
            else:
                current_ranking += ', ' + ranking

        for ranking in response.xpath(
            '//td[@class="tdRank"]/div[@class="rightCol"]/a/text()',
        ).extract():
            current_ranking += ', ' + ranking
   
        some_data = response.xpath(
            '//tr/td[@class="tdRankAlt"]/div[@class="leftCol"]/strong/text()',
        ).extract()
        ufc_record = ''
        for s_d in some_data:
            if s_d.count('-') == 2:
                ufc_record = s_d
                break


        f_m_item['division'] = div_name
        f_m_item['name'] = name
        f_m_item['current_ranking'] = current_ranking
        f_m_item['ufc_record'] = ufc_record
        yield f_m_item