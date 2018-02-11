# coding=utf-8
from py2neo.ogm import GraphObject, Property, RelatedFrom, RelatedTo


class hero(GraphObject):
    ename = Property()  #
    cname = Property()  #
    title = Property()  #
    hero_type = Property()  #
    survive_capability = Property()  #
    attack_effect = Property()  #
    skill_effect = Property()  #
    pickup_easy = Property()  #

    has_skill = RelatedTo("skill", "has_skill")
    has_summoner = RelatedTo("summoner", "has_summoner")
    best_partner = RelatedTo("hero", "best_partner")
    suppress_hero = RelatedTo("hero", "suppress_hero")
    defeated_hero = RelatedTo("hero", "defeated_hero")
    recommend_item_set = RelatedTo("item_set", "recommend_item_set")
    has_ming = RelatedTo("ming", "has_ming")

    hero_story = Property()  #
    hero_history = Property()  #
    max_lift = Property()  # 最大生命
    max_magic = Property()  # 最大法力
    physical_attack = Property()  # 物理攻击
    magic_attack = Property()  # 法术攻击
    physical_defence = Property()  # 物理防御
    physical_reduce_rate = Property()  # 物理减伤率
    magic_defence = Property()  # 法术防御
    magic_reduce_rate = Property()  # 法术减伤率
    mobility = Property()  # 移速
    physical_guard_break = Property()  # 物理护甲穿透
    magic_guard_break = Property()  # 法术护甲穿透
    attack_velocity_increase = Property()  # 攻速加成
    heavy_attack_rate = Property()  # 暴击几率
    heavy_attack_affect = Property()  # 暴击效果
    physical_blood_sucking = Property()  # 物理吸血
    magic_blook_sucking = Property()  # 法术吸血
    cool_down_reduce = Property()  # 冷却缩减
    attack_scope = Property()  # 攻击范围
    toughness = Property()  # 韧性
    lift_refresh = Property()  # 生命回复
    magic_refresh = Property()  # 法力回复


class skill(GraphObject):
    skill_name = Property()
    is_primary_upgrade = Property()
    is_secondary_upgrade = Property()
    skill_consume = Property()
    skill_cool_down = Property()
    skill_desc = Property()
    skill_tip = Property()


class summoner(GraphObject):
    summoner_rank = Property()
    summoner_name = Property()
    summoner_id = Property()
    summoner_description = Property()


class item(GraphObject):
    total_price = Property()
    item_name = Property()
    item_desc2 = Property()
    item_desc1 = Property()
    item_type = Property()
    item_id = Property()
    price = Property()
    recommended_item_set = RelatedFrom('item_set', 'recommend_item')


class ming(GraphObject):
    ming_id = Property()
    ming_type = Property()
    ming_grade = Property()
    ming_name = Property()
    ming_des = Property()
    owned_hero = RelatedFrom("hero", "has_ming")


class item_set(GraphObject):
    tips = Property()
    recommend_item = RelatedTo("item", "recommend_item")
    recommended_hero = RelatedFrom("hero", "recommend_item_set")
