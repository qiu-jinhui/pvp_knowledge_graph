# coding=utf-8
from py2neo.ogm import GraphObject, Property


class Hero(GraphObject):
    ename = Property()  #
    cname = Property()  #
    title = Property()  #
    hero_type = Property()  #
    survive_capability = Property()  #
    attack_effect = Property()  #
    skill_effect = Property()  #
    pickup_easy = Property()  #
    hero_skill = Property()
    summoner_skill = Property()
    best_partner = Property()
    suppress_hero = Property()
    defeated_hero = Property()
    hero_recommend_items = Property()
    hero_ming = Property()
    hero_ming_tips = Property()
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

class HeroSkill(GraphObject):
    skill_name = Property()
    is_primary_upgrade = Property()
    is_secondary_upgrade = Property()
    skill_consume = Property()
    skill_cool_down = Property()
    skill_desc = Property()
    skill_tip = Property()