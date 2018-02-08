#coding=utf-8
import scrapy
import json

from pvpSpider.items import HeroItem, HeroSkill


class HeroSpider(scrapy.Spider):
    def __init__(self):
        pass

    name = "heroSpider"
    allowed_domains = ["qq.com"]
    start_urls = [
        "http://pvp.qq.com/web201605/herolist.shtml"
    ]

    def parse(self, response):
        filename = 'data' + response.url.split('/')[-1]
        with open(filename, 'wb') as f:
            f.write(response.body)

class HeroJsonSpider(scrapy.Spider):
    def __init__(self):
        pass

    name = "heroJsonSpider"
    allowed_domains = ["qq.com"]
    start_urls = [
        "http://pvp.qq.com/web201605/js/herolist.json"
    ]

    def parse(self, response):
        filename = 'data/' + response.url.split('/')[-1]
        with open(filename, 'wb') as f:
            f.write(response.body)

class HeroJsonParser(scrapy.Spider):
    def __init__(self):
        pass

    name = "heroJsonParser"
    allowed_domains = ["qq.com"]
    start_urls = [
        "http://pvp.qq.com/web201605/js/herolist.json"
    ]

    hero_sort = {"herodetail-sort-1": "战士", "herodetail-sort-2":"法师", "herodetail-sort-3":"坦克", "herodetail-sort-4":"刺客", "herodetail-sort-5":"射手", "herodetail-sort-6":"辅助"}

    def parse(self, response):

        filename = 'data/' + response.url.split('/')[-1]
        with open(filename, 'wb') as f:
            f.write(response.body)

        herolist = json.loads(response.body)

        for hero in herolist:
            ename = hero['ename']
            cname = hero['cname']
            title = hero['skin_name'].split('|')
            heroItem = HeroItem(ename=ename, cname=cname, title=title)

            detailurl = "http://pvp.qq.com/web201605/herodetail/" + str(ename) + ".shtml"
            #detailurl = "file:/Users/sonicqiu/Documents/workspace/IdeaProjects/pvpSpider/data/" + str(ename) + ".shtml"
            #yield heroItem
            yield scrapy.Request(url=detailurl, meta={'heroItem': heroItem}, callback=self.parseHeroDetail)

    def parseHeroDetail(self, response):

        filename = "data/" + response.url.split("/")[-1]
        with open(filename, 'wb') as f:
            f.write(response.body)

        cname = response.xpath('/html/body/div[1]/div[1]/div/div/div[1]/h2/text()').extract()[0]

        hero_type = self.hero_sort[response.xpath("/html/body/div[1]/div[1]/div/div/div[1]/span/i/@class").extract()[0]]

        survive_capability = int(response.xpath("/html/body/div[1]/div[1]/div/div/div[1]/ul/li[1]/span/i/@style").extract()[0].split(":")[1][0:-1])

        attack_effect = int(response.xpath("/html/body/div[1]/div[1]/div/div/div[1]/ul/li[2]/span/i/@style").extract()[0].split(":")[1][0:-1])

        skill_effect = int(response.xpath("/html/body/div[1]/div[1]/div/div/div[1]/ul/li[3]/span/i/@style").extract()[0].split(":")[1][0:-1])

        pickup_easy = int(response.xpath("/html/body/div[1]/div[1]/div/div/div[1]/ul/li[4]/span/i/@style").extract()[0].split(":")[1][0:-1])

        #召唤技能
        summoner_skill = response.xpath("//*[@id='skill3']/@data-skill").extract()[0].split("|")

        #最佳拍档
        best_partner = [str.split(".")[0] for str in response.xpath("/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/div[1]/div[2]/ul/li/a/@href").extract()]
        best_partner_desc = response.xpath("/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/div[1]/div[3]/p/text()").extract()
        best_partner_list = zip(best_partner, best_partner_desc)

        #压制英雄
        suppress_hero = [str.split(".")[0] for str in response.xpath("/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/div[2]/div[2]/ul/li/a/@href").extract()]
        suppress_hero_desc = response.xpath("/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/div[2]/div[3]/p/text()").extract()
        suppress_hero_list = zip(suppress_hero, suppress_hero_desc)

        #被压制英雄
        defeated_hero = [str.split(".")[0] for str in response.xpath("/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/div[3]/div[2]/ul/li/a/@href").extract()]
        defeated_hero_desc = response.xpath("/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/div[3]/div[3]/p/text()").extract()
        defeated_hero_list = zip(defeated_hero, defeated_hero_desc)

        skill_pic_list = response.xpath("/html/body/div[1]/div[2]/div/div[1]/div[2]/div/ul/li/img/@src").extract()
        skill_name_list = response.xpath("/html/body/div[1]/div[2]/div/div[1]/div[2]/div/div/div/p[1]/b/text()").extract()
        skill_cool_down_list = response.xpath("/html/body/div[1]/div[2]/div/div[1]/div[2]/div/div/div/p[1]/span[1]/text()").extract()
        skill_consume_list = response.xpath("/html/body/div[1]/div[2]/div/div[1]/div[2]/div/div/div/p[1]/span[2]/text()").extract()
        skill_desc_list = response.xpath("/html/body/div[1]/div[2]/div/div[1]/div[2]/div/div/div/p[2]/text()").extract()
        skill_tip_list = response.xpath("/html/body/div[1]/div[2]/div/div[1]/div[2]/div/div/div/div/text()").extract()

        hero_skill_list = []

        primary_upgrade_skill = response.xpath("/html/body/div[1]/div[2]/div/div[2]/div[1]/div[2]/p[2]/img/@src").extract()[0]
        secondary_upgrade_skill = response.xpath("/html/body/div[1]/div[2]/div/div[2]/div[1]/div[2]/p[4]/img/@src").extract()[0]

        for i in range(len(skill_name_list)):
            heroSkill = HeroSkill(hero_ename=response.url.split('/')[-1].split('.')[0], hero_cname=cname, skill_name=skill_name_list[i], skill_cool_down=skill_cool_down_list[i], skill_consume=skill_consume_list[i], skill_desc=skill_desc_list[i], skill_tip=skill_tip_list[i], is_primary_upgrade=cmp(primary_upgrade_skill, skill_pic_list[i]) == 0, is_secondary_upgrade=cmp(secondary_upgrade_skill, skill_pic_list[i]) == 0)
            hero_skill_list.append(heroSkill)

        # 出装建议
        hero_recommend_items = [str.split("|") for str in response.xpath("/html/body/div[1]/div[2]/div/div[2]/div[2]/div[2]/div/ul/@data-item").extract()]
        hero_recommend_items_desc = response.xpath("/html/body/div[1]/div[2]/div/div[2]/div[2]/div[2]/div/p/text()").extract()
        hero_recommend_items_list = zip(hero_recommend_items, hero_recommend_items_desc)

        # 铭文
        hero_ming = response.xpath("/html/body/div[1]/div[2]/div/div[1]/div[3]/div[2]/ul/@data-ming").extract()[0].split("|")
        hero_ming_tips = response.xpath("/html/body/div[1]/div[2]/div/div[1]/div[3]/div[2]/p/text()").extract()[0]

        # 英雄故事
        hero_story = response.xpath("string(//*[@id='hero-story']/div[2]/p)").extract()[0]

        # 历史上的ta
        hero_history = response.xpath("string(//*[@id='history']/div[2]/p)").extract()[0]

        heroItem = response.meta['heroItem']
        heroItem['hero_skill'] = hero_skill_list
        heroItem['hero_type'] = hero_type
        heroItem['survive_capability'] = survive_capability
        heroItem['attack_effect'] = attack_effect
        heroItem['skill_effect'] = skill_effect
        heroItem['pickup_easy'] = pickup_easy
        heroItem['summoner_skill'] = summoner_skill
        heroItem['best_partner'] = best_partner_list
        heroItem['suppress_hero'] = suppress_hero_list
        heroItem['defeated_hero'] = defeated_hero_list
        heroItem['hero_recommend_items'] = hero_recommend_items_list
        heroItem['hero_ming'] = hero_ming
        heroItem['hero_ming_tips'] = hero_ming_tips
        heroItem['hero_story'] = hero_story
        heroItem['hero_history'] = hero_history

        yield heroItem



class HeroDetailSpider(scrapy.Spider):
    def __init__(self):
        pass

    name = "heroDetailSpider"
    allowed_domains = ["qq.com"]
    start_urls = [
        "http://pvp.qq.com/web201605/herodetail/501.shtml"
    ]

    def parse(self, response):
        filename = "data/" + response.url.split("/")[-1]
        with open(filename, 'wb') as f:
            f.write(response.body)

class HeroDetailParseSpider(scrapy.Spider):
    def __init__(self):
        pass

    name = "heroDetailParseSpider"
    allowed_domains = ["qq.com"]
    start_urls = [
        "http://pvp.qq.com/web201605/herodetail/501.shtml"
    ]

    hero_sort = {"herodetail-sort-1": "战士", "herodetail-sort-2":"法师", "herodetail-sort-3":"坦克", "herodetail-sort-4":"刺客", "herodetail-sort-5":"射手", "herodetail-sort-6":"辅助"}

    def parse(self, response):

        cname = response.xpath('/html/body/div[1]/div[1]/div/div/div[1]/h2/text()').extract()[0]

        hero_type = self.hero_sort[response.xpath("/html/body/div[1]/div[1]/div/div/div[1]/span/i/@class").extract()[0]]

        survive_capability = int(response.xpath("/html/body/div[1]/div[1]/div/div/div[1]/ul/li[1]/span/i/@style").extract()[0].split(":")[1][0:-1])

        attack_effect = int(response.xpath("/html/body/div[1]/div[1]/div/div/div[1]/ul/li[2]/span/i/@style").extract()[0].split(":")[1][0:-1])

        skill_effect = int(response.xpath("/html/body/div[1]/div[1]/div/div/div[1]/ul/li[3]/span/i/@style").extract()[0].split(":")[1][0:-1])

        pickup_easy = int(response.xpath("/html/body/div[1]/div[1]/div/div/div[1]/ul/li[4]/span/i/@style").extract()[0].split(":")[1][0:-1])

        #召唤技能
        summoner_skill = response.xpath("//*[@id='skill3']/@data-skill").extract()[0].split("|")

        #最佳拍档
        best_partner = [str.split(".")[0] for str in response.xpath("/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/div[1]/div[2]/ul/li/a/@href").extract()]
        best_partner_desc = response.xpath("/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/div[1]/div[3]/p/text()").extract()
        best_partner_list = zip(best_partner, best_partner_desc)

        #压制英雄
        suppress_hero = [str.split(".")[0] for str in response.xpath("/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/div[2]/div[2]/ul/li/a/@href").extract()]
        suppress_hero_desc = response.xpath("/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/div[2]/div[3]/p/text()").extract()
        suppress_hero_list = zip(suppress_hero, suppress_hero_desc)

        #被压制英雄
        defeated_hero = [str.split(".")[0] for str in response.xpath("/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/div[3]/div[2]/ul/li/a/@href").extract()]
        defeated_hero_desc = response.xpath("/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/div[3]/div[3]/p/text()").extract()
        defeated_hero_list = zip(defeated_hero, defeated_hero_desc)

        skill_pic_list = response.xpath("/html/body/div[1]/div[2]/div/div[1]/div[2]/div/ul/li/img/@src").extract()
        skill_name_list = response.xpath("/html/body/div[1]/div[2]/div/div[1]/div[2]/div/div/div/p[1]/b/text()").extract()
        skill_cool_down_list = response.xpath("/html/body/div[1]/div[2]/div/div[1]/div[2]/div/div/div/p[1]/span[1]/text()").extract()
        skill_consume_list = response.xpath("/html/body/div[1]/div[2]/div/div[1]/div[2]/div/div/div/p[1]/span[2]/text()").extract()
        skill_desc_list = response.xpath("/html/body/div[1]/div[2]/div/div[1]/div[2]/div/div/div/p[2]/text()").extract()
        skill_tip_list = response.xpath("/html/body/div[1]/div[2]/div/div[1]/div[2]/div/div/div/div/text()").extract()

        hero_skill_list = []

        primary_upgrade_skill = response.xpath("/html/body/div[1]/div[2]/div/div[2]/div[1]/div[2]/p[2]/img/@src").extract()[0]
        secondary_upgrade_skill = response.xpath("/html/body/div[1]/div[2]/div/div[2]/div[1]/div[2]/p[4]/img/@src").extract()[0]

        for i in range(len(skill_name_list)):
            heroSkill = HeroSkill(hero_ename=response.url.split('/')[-1].split('.')[0], hero_cname=cname, skill_name=skill_name_list[i], skill_cool_down=skill_cool_down_list[i], skill_consume=skill_consume_list[i], skill_desc=skill_desc_list[i], skill_tip=skill_tip_list[i], is_primary_upgrade=cmp(primary_upgrade_skill, skill_pic_list[i]) == 0, is_secondary_upgrade=cmp(secondary_upgrade_skill, skill_pic_list[i]) == 0)
            hero_skill_list.append(heroSkill)

        # 出装建议
        hero_recommend_items = [str.split("|") for str in response.xpath("/html/body/div[1]/div[2]/div/div[2]/div[2]/div[2]/div/ul/@data-item").extract()]
        hero_recommend_items_desc = response.xpath("/html/body/div[1]/div[2]/div/div[2]/div[2]/div[2]/div/p/text()").extract()
        hero_recommend_items_list = zip(hero_recommend_items, hero_recommend_items_desc)

        # 铭文
        hero_ming = response.xpath("/html/body/div[1]/div[2]/div/div[1]/div[3]/div[2]/ul/@data-ming").extract()[0].split("|")
        hero_ming_tips = response.xpath("/html/body/div[1]/div[2]/div/div[1]/div[3]/div[2]/p/text()").extract()[0]

        # 英雄故事
        hero_story = response.xpath("string(//*[@id='hero-story']/div[2]/p)").extract()[0]

        # 历史上的ta
        hero_history = response.xpath("string(//*[@id='history']/div[2]/p)").extract()[0]

        heroItem = HeroItem(ename=response.url.split('/')[-1].split('.')[0], cname=cname, hero_skill=hero_skill_list)
        heroItem['hero_type'] = hero_type
        heroItem['survive_capability'] = survive_capability
        heroItem['attack_effect'] = attack_effect
        heroItem['skill_effect'] = skill_effect
        heroItem['pickup_easy'] = pickup_easy
        heroItem['summoner_skill'] = summoner_skill
        heroItem['best_partner'] = best_partner_list
        heroItem['suppress_hero'] = suppress_hero_list
        heroItem['defeated_hero'] = defeated_hero_list
        heroItem['hero_recommend_items'] = hero_recommend_items_list
        heroItem['hero_ming'] = hero_ming
        heroItem['hero_ming_tips'] = hero_ming_tips
        heroItem['hero_story'] = hero_story
        heroItem['hero_history'] = hero_history

        yield heroItem
