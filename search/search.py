# coding=utf-8
from HeroSearch import HeroSearch
from ItemSearch import ItemSearch
from MingSearch import MingSearch

heroSearch = HeroSearch()
heroresult = heroSearch.search_hero_by_cname(u'达摩')

print '=======Hero attribute========='
print heroresult.ename
print heroresult.cname
print heroresult.title
print heroresult.hero_type
print heroresult.survive_capability
print heroresult.attack_effect
print heroresult.skill_effect
print heroresult.pickup_easy
print heroresult.hero_story
print heroresult.hero_history
print heroresult.max_lift
print heroresult.max_magic
print heroresult.physical_attack
print heroresult.magic_attack
print heroresult.physical_defence
print heroresult.physical_reduce_rate
print heroresult.magic_defence
print heroresult.magic_reduce_rate
print heroresult.mobility
print heroresult.physical_guard_break
print heroresult.magic_guard_break
print heroresult.attack_velocity_increase
print heroresult.heavy_attack_rate
print heroresult.heavy_attack_affect
print heroresult.physical_blood_sucking
print heroresult.magic_blook_sucking
print heroresult.cool_down_reduce
print heroresult.attack_scope
print heroresult.toughness
print heroresult.lift_refresh
print heroresult.magic_refresh

print '=======Hero skill========='
for heroskill in heroresult.has_skill:
    print heroskill.skill_name
    print heroskill.is_primary_upgrade
    print heroskill.is_secondary_upgrade
    print heroskill.skill_consume
    print heroskill.skill_cool_down
    print heroskill.skill_desc
    print heroskill.skill_tip

print '=========Summoner========='
for summoner in heroresult.has_summoner:
    print summoner.summoner_rank
    print summoner.summoner_name
    print summoner.summoner_id
    print summoner.summoner_description

print '==========Ming============'
for ming in heroresult.has_ming:
    print ming.ming_id
    print ming.ming_type
    print ming.ming_grade
    print ming.ming_name
    print ming.ming_des

print '=======Item set==========='
for item_set in heroresult.recommend_item_set:
    print '**********************'
    print item_set.tips
    for item in item_set.recommend_item:
        print item.total_price
        print item.item_name
        print item.item_desc2
        print item.item_desc1
        print item.item_type
        print item.item_id
        print item.price

print '========best partner======='
for best_partner in heroresult.best_partner:
    print best_partner.cname

print '========suppress hero======='
for suppress_hero in heroresult.suppress_hero:
    print suppress_hero.cname

print '========defeated hero======='
for defeated_hero in heroresult.defeated_hero:
    print defeated_hero.cname

print '=========Ming==============='
mingSearch = MingSearch()
mingresult = mingSearch.search_ming_by_name(u'心眼')
for hero in mingresult.owned_hero:
    print hero.cname

print '==========Item============='
itemSearch = ItemSearch()
itemresult = itemSearch.search_item_by_name(u'无尽战刃')
print itemresult.item_name
for item_set in itemresult.recommended_item_set:
    for recommended_hero in item_set.recommended_hero:
        print recommended_hero.cname

print '=========hero relation====='
returntype = heroSearch.search_hero_relation('韩信', '王昭君')
print returntype
