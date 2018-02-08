#encoding=utf-8
import scrapy
import json

from pvpSpider.items import HeroAttributeItem


class HeroAttributeSpider(scrapy.Spider):
    name = "HeroAttributeSpider"
    allowed_domains = ["17173.com"]
    start_urls = ["http://news.17173.com/z/pvp/yxtj/index.shtml"]

    def parse(self, response):

        filename = 'data/17173/' + response.url.split('/')[-1]
        with open(filename, 'wb') as f:
            f.write(response.body)

        text = response.xpath("/html/body/script[2]/text()").extract()[0].replace("var herosConfig = ", "").replace("window.herosConfig = window.herosConfig? window.herosConfig : herosConfig;", "").strip()[0:-1].replace("'", "\"")

        herolist = json.loads(text)

        for hero in herolist:
            yield scrapy.Request(url=hero['href'], callback=self.parseHeroAttribute)

    def parseHeroAttribute(self, response):

        filename = 'data/17173/' + response.url.split('/')[-2] + ".shtml"
        with open(filename, 'wb') as f:
            f.write(response.body)

        try:

            heroAttributeItem = HeroAttributeItem()
            heroAttributeItem['hero_name'] = response.xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/p/span[1]/text()").extract()[0]

            if cmp('sb', response.url.split('/')[-2]) == 0:

                heroAttributeItem['max_lift'] = response.xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div/div[1]/span/text()").extract()[0]
                heroAttributeItem['max_magic'] = response.xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div/div[2]/span/text()").extract()[0]
                heroAttributeItem['physical_attack'] = response.xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div/div[3]/span/text()").extract()[0]
                heroAttributeItem['magic_attack'] = response.xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div/div[4]/span/text()").extract()[0]
                heroAttributeItem['physical_defence'] = response.xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div/div[5]/span/text()").extract()[0]
                heroAttributeItem['physical_reduce_rate'] = response.xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div/div[6]/span/text()").extract()[0].replace("%", "")
                heroAttributeItem['magic_defence'] = response.xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div/div[7]/span/text()").extract()[0]
                heroAttributeItem['magic_reduce_rate'] = response.xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div/div[8]/span/text()").extract()[0].replace("%", "")
                heroAttributeItem['mobility'] = response.xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div/div[9]/span/text()").extract()[0]
                heroAttributeItem['physical_guard_break'] = response.xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div/div[10]/span/text()").extract()[0]
                heroAttributeItem['magic_guard_break'] = response.xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div/div[11]/span/text()").extract()[0]
                heroAttributeItem['attack_velocity_increase'] = response.xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div/div[12]/span/text()").extract()[0]
                heroAttributeItem['heavy_attack_rate'] = response.xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div/div[13]/span/text()").extract()[0].replace("%", "")
                heroAttributeItem['heavy_attack_affect'] = response.xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div/div[14]/span/text()").extract()[0].replace("%", "")
                heroAttributeItem['physical_blood_sucking'] = response.xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div/div[15]/span/text()").extract()[0]
                heroAttributeItem['magic_blook_sucking'] = response.xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div/div[16]/span/text()").extract()[0]
                heroAttributeItem['cool_down_reduce'] = response.xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div/div[17]/span/text()").extract()[0].replace("%", "")
                heroAttributeItem['attack_scope'] = response.xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div/div[18]/span/text()").extract()[0]
                heroAttributeItem['toughness'] = response.xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div/div[19]/span/text()").extract()[0]
                heroAttributeItem['lift_refresh'] = response.xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div/div[20]/span/text()").extract()[0].replace("%", "")
                heroAttributeItem['magic_refresh'] = response.xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div/div[21]/span/text()").extract()[0]

            else:

                heroAttributeItem['max_lift'] = response.xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/span/text()").extract()[0]
                heroAttributeItem['max_magic'] = response.xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/span/text()").extract()[0]
                heroAttributeItem['physical_attack'] = response.xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/span/text()").extract()[0]
                heroAttributeItem['magic_attack'] = response.xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[4]/span/text()").extract()[0]
                heroAttributeItem['physical_defence'] = response.xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[5]/span/text()").extract()[0]
                heroAttributeItem['physical_reduce_rate'] = response.xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[6]/span/text()").extract()[0].replace("%", "")
                heroAttributeItem['magic_defence'] = response.xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[7]/span/text()").extract()[0]
                heroAttributeItem['magic_reduce_rate'] = response.xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[8]/span/text()").extract()[0].replace("%", "")
                heroAttributeItem['mobility'] = response.xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[9]/span/text()").extract()[0]
                heroAttributeItem['physical_guard_break'] = response.xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[10]/span/text()").extract()[0]
                heroAttributeItem['magic_guard_break'] = response.xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[11]/span/text()").extract()[0]
                heroAttributeItem['attack_velocity_increase'] = response.xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[12]/span/text()").extract()[0]
                heroAttributeItem['heavy_attack_rate'] = response.xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[13]/span/text()").extract()[0].replace("%", "")
                heroAttributeItem['heavy_attack_affect'] = response.xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[14]/span/text()").extract()[0].replace("%", "")
                heroAttributeItem['physical_blood_sucking'] = response.xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[15]/span/text()").extract()[0]
                heroAttributeItem['magic_blook_sucking'] = response.xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[16]/span/text()").extract()[0]
                heroAttributeItem['cool_down_reduce'] = response.xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[17]/span/text()").extract()[0].replace("%", "")
                heroAttributeItem['attack_scope'] = response.xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[18]/span/text()").extract()[0]
                heroAttributeItem['toughness'] = response.xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[19]/span/text()").extract()[0]
                heroAttributeItem['lift_refresh'] = response.xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[20]/span/text()").extract()[0].replace("%", "")
                heroAttributeItem['magic_refresh'] = response.xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[21]/span/text()").extract()[0]

        except:
            print "Error when parsing " + filename

        yield heroAttributeItem