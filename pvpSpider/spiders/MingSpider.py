import scrapy
import json

from pvpSpider.items import MingItem


class MingSpider(scrapy.Spider):

    name = 'mingSpider'
    allowed_domains = ['qq.com']
    start_urls = ['http://pvp.qq.com/web201605/js/ming.json']

    def parse(self, response):

        filename = 'data/' + response.url.split('/')[-1]
        with open(filename, 'wb') as f:
            f.write(response.body)

        minglist = json.loads(response.body)

        for ming in minglist:
            mingItem = MingItem()
            mingItem['ming_id'] = ming['ming_id']
            mingItem['ming_type'] = ming['ming_type']
            mingItem['ming_grade'] = ming['ming_grade']
            mingItem['ming_name'] = ming['ming_name']
            mingItem['ming_des'] = ming['ming_des'].replace("</p><p>", " ").replace("<p>", "").replace("</p>", "")

            yield mingItem
