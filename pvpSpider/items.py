# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PvpspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class HeroItem(scrapy.Item):
    ename = scrapy.Field()
    cname = scrapy.Field()
    title = scrapy.Field()
    hero_type = scrapy.Field()
    survive_capability = scrapy.Field()
    attack_effect = scrapy.Field()
    skill_effect = scrapy.Field()
    pickup_easy = scrapy.Field()
    hero_skill = scrapy.Field()
    summoner_skill = scrapy.Field()
    best_partner = scrapy.Field()
    suppress_hero = scrapy.Field()
    defeated_hero = scrapy.Field()
    hero_recommend_items = scrapy.Field()
    hero_ming = scrapy.Field()
    hero_ming_tips = scrapy.Field()
    hero_story = scrapy.Field()
    hero_history = scrapy.Field()

class HeroSkill(scrapy.Item):
    hero_ename = scrapy.Field()
    hero_cname = scrapy.Field()
    skill_name = scrapy.Field()
    skill_cool_down = scrapy.Field()
    skill_consume = scrapy.Field()
    skill_desc = scrapy.Field()
    skill_tip = scrapy.Field()
    is_primary_upgrade = scrapy.Field()
    is_secondary_upgrade = scrapy.Field()

class ItemItem(scrapy.Item):
    item_id = scrapy.Field()
    item_name = scrapy.Field()
    item_type = scrapy.Field()
    price = scrapy.Field()
    total_price = scrapy.Field()
    item_desc1 = scrapy.Field()
    item_desc2 = scrapy.Field()

class SummonerItem(scrapy.Item):
    summoner_id = scrapy.Field()
    summoner_name = scrapy.Field()
    summoner_rank = scrapy.Field()
    summoner_description = scrapy.Field()

class MingItem(scrapy.Item):
    ming_id = scrapy.Field()
    ming_type = scrapy.Field()
    ming_grade = scrapy.Field()
    ming_name = scrapy.Field()
    ming_des = scrapy.Field()

class HeroAttributeItem(scrapy.Item):
    hero_name = scrapy.Field()
    max_lift = scrapy.Field() #最大生命
    max_magic = scrapy.Field() #最大法力
    physical_attack = scrapy.Field() #物理攻击
    magic_attack = scrapy.Field() #法术攻击
    physical_defence = scrapy.Field() #物理防御
    physical_reduce_rate = scrapy.Field() #物理减伤率
    magic_defence = scrapy.Field() #法术防御
    magic_reduce_rate = scrapy.Field() #法术减伤率
    mobility = scrapy.Field() #移速
    physical_guard_break = scrapy.Field() #物理护甲穿透
    magic_guard_break = scrapy.Field() #法术护甲穿透
    attack_velocity_increase = scrapy.Field() #攻速加成
    heavy_attack_rate = scrapy.Field() #暴击几率
    heavy_attack_affect = scrapy.Field() #暴击效果
    physical_blood_sucking = scrapy.Field() #物理吸血
    magic_blook_sucking = scrapy.Field() #法术吸血
    cool_down_reduce = scrapy.Field() #冷却缩减
    attack_scope = scrapy.Field() #攻击范围
    toughness = scrapy.Field() #韧性
    lift_refresh = scrapy.Field() #生命回复
    magic_refresh = scrapy.Field() #法力回复
