import scrapy
import json

from pvpSpider.items import SummonerItem


class SummonerSpider(scrapy.Spider):

    name = 'summonerSpider'
    allowed_domains = ['qq.com']
    start_urls = ['http://pvp.qq.com/web201605/js/summoner.json']

    def parse(self, response):

        filename = 'data/' + response.url.split('/')[-1]
        with open(filename, 'wb') as f:
            f.write(response.body)

        summonerlist = json.loads(response.body)

        for summoner in summonerlist:
            summonerItem = SummonerItem()
            summonerItem['summoner_id'] = summoner['summoner_id']
            summonerItem['summoner_name'] = summoner['summoner_name']
            summonerItem['summoner_rank'] = summoner['summoner_rank']
            summonerItem['summoner_description'] = summoner['summoner_description']

            yield summonerItem
