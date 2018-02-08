import os
import json

from pvpSpider.items import HeroAttributeItem

os.chdir('/Users/sonicqiu/Documents/workspace/IdeaProjects/pvpSpider')

from py2neo import Node, Graph, Relationship
import pandas as pd

g = Graph("http://localhost:7474", username="neo4j", password="password")

# delete all node
g.delete_all()

# create summoner nodes
summoner_data_list = pd.read_csv('./result/summoner.csv', header=0)
for i in range(0, len(summoner_data_list)):
    tempNode = Node('summoner',
                    summoner_rank=str(summoner_data_list['summoner_rank'][i]),
                    summoner_name=str(summoner_data_list['summoner_name'][i]),
                    summoner_id=summoner_data_list['summoner_id'][i],
                    summoner_description=str(summoner_data_list['summoner_description'][i])
                    )
    g.create(tempNode)

# create item nodes
item_data_list = pd.read_csv('./result/item.csv', header=0)
for i in range(0, len(item_data_list)):
    tempNode = Node('item',
                    total_price=item_data_list['total_price'][i],
                    item_name=str(item_data_list['item_name'][i]),
                    item_desc2=str(item_data_list['item_desc2'][i]),
                    item_desc1=str(item_data_list['item_desc1'][i]),
                    item_type=str(item_data_list['item_type'][i]),
                    item_id=item_data_list['item_id'][i],
                    price=item_data_list['price'][i]
                    )
    g.create(tempNode)

# create ming nodes
ming_data_list = pd.read_csv('./result/ming.csv', header=0)
for i in range(0, len(ming_data_list)):
    tempNode = Node('ming',
                    ming_id=ming_data_list['ming_id'][i],
                    ming_type=str(ming_data_list['ming_type'][i]),
                    ming_grade=ming_data_list['ming_grade'][i],
                    ming_name=str(ming_data_list['ming_name'][i]),
                    ming_des=str(ming_data_list['ming_des'][i])
                    )
    g.create(tempNode)

# create hero nodes
hero_data_list = pd.read_csv('./result/heromain.csv', header=0)
for i in range(0, len(hero_data_list)):
    tempNode = Node('hero',
                    ename=hero_data_list['ename'][i],
                    pickup_easy=hero_data_list['pickup_easy'][i],
                    hero_history=str(hero_data_list['hero_history'][i]),
                    title=str(hero_data_list['title'][i]),
                    hero_type=str(hero_data_list['hero_type'][i]),
                    survive_capability=hero_data_list['survive_capability'][i],
                    cname=str(hero_data_list['cname'][i]),
                    hero_story=str(hero_data_list['hero_story'][i]),
                    skill_effect=hero_data_list['skill_effect'][i],
                    attack_effect=hero_data_list['attack_effect'][i]
                    )
    g.create(tempNode)

# create hero - summoner relation
for i in range(0, len(hero_data_list)):
    hero_ename = hero_data_list['ename'][i]
    hero_summoner_list = hero_data_list['summoner_skill'][i].split(",")
    for summoner_key in hero_summoner_list:
        relation = Relationship(g.find_one(label='hero', property_key='ename', property_value=hero_ename),
                                "has_summoner",
                                g.find_one(label='summoner', property_key='summoner_id', property_value=int(summoner_key)))
        g.create(relation)

# create hero - skill relation
for i in range(0, len(hero_data_list)):
    hero_ename = hero_data_list['ename'][i]
    #print "before " + hero_data_list['cname'][i]
    #hero_skill_text = hero_data_list['hero_skill'][i].decode('raw_unicode-escape').encode('utf-8').replace("u'", "\"").replace("'", "\"").replace("\n", "").replace('False', 'false').replace('True', 'true').replace("\\xb7", "").replace("\\xd7", "*")
    #print hero_skill_text
    #hero_skill_list = json.loads(hero_skill_text)
    hero_skill_list = eval(hero_data_list['hero_skill'][i])
    for hero_skill in hero_skill_list:
        tempNode = Node('skill',
                        skill_name=hero_skill['skill_name'],
                        is_primary_upgrade=hero_skill['is_primary_upgrade'],
                        is_secondary_upgrade=hero_skill['is_secondary_upgrade'],
                        skill_consume=hero_skill['skill_consume'],
                        skill_cool_down=hero_skill['skill_cool_down'],
                        skill_desc=hero_skill['skill_desc'],
                        skill_tip=hero_skill['skill_tip']
                        )
        relation = Relationship(g.find_one(label='hero', property_key='ename', property_value=hero_ename),
                                "has_skill",
                                tempNode)
        g.create(relation)

# create hero - recommend item
for i in range(0, len(hero_data_list)):
    hero_ename = hero_data_list['ename'][i]
    #print "current hero ename: " + str(hero_ename)

    hero_recommend_items_list = eval(hero_data_list['hero_recommend_items'][i])
    for hero_recommend_items in hero_recommend_items_list:
        item_tip = hero_recommend_items[1]
        item_set_node = Node('item_set',
                             tips=item_tip)
        hero_item_set_rel = Relationship(
            g.find_one(label='hero', property_key='ename', property_value=hero_ename),
            'recommend_item_set',
            item_set_node
        )
        g.create(hero_item_set_rel)

        for hero_recommend_item in hero_recommend_items[0]:
            print hero_recommend_item + " " + str(hero_ename) + " " + item_tip
            iset_node = g.find_one(label='item_set', property_key='tips', property_value=item_tip)
            print iset_node
            i_node = g.find_one(label='item', property_key='item_id', property_value=int(hero_recommend_item))
            print i_node
            item_set_item_rel = Relationship(
                iset_node,
                'recommend_item',
                i_node
            )
            g.create(item_set_item_rel)

# create hero - ming relation
for i in range(0, len(hero_data_list)):
    hero_ename = hero_data_list['ename'][i]
    hero_ming_tips = hero_data_list['hero_ming_tips'][i]
    hero_ming_list = hero_data_list['hero_ming'][i].split(",")
    for hero_ming in hero_ming_list:
        ming_rel = Relationship(
            g.find_one(label='hero', property_key='ename', property_value=hero_ename),
            'has_ming',
            g.find_one(label='ming', property_key='ming_id', property_value=int(hero_ming))
        )
        ming_rel['ming_tips'] = hero_ming_tips
        g.create(ming_rel)

# create best partner relation
for i in range(0, len(hero_data_list)):
    hero_ename = hero_data_list['ename'][i]
    best_partner_list = eval(hero_data_list['best_partner'][i])
    for best_partner in best_partner_list:
        best_partnet_rel = Relationship(
            g.find_one(label='hero', property_key='ename', property_value=hero_ename),
            'best_partner',
            g.find_one(label='hero', property_key='ename', property_value=int(best_partner[0]))
        )
        best_partnet_rel['best_partner_tips'] = best_partner[1]
        g.create(best_partnet_rel)

# create suppress hero relation
for i in range(0, len(hero_data_list)):
    hero_ename = hero_data_list['ename'][i]
    suppress_hero_list = eval(hero_data_list['suppress_hero'][i])
    for suppress_hero in suppress_hero_list:
        suppress_hero_rel = Relationship(
            g.find_one(label='hero', property_key='ename', property_value=hero_ename),
            'suppress_hero',
            g.find_one(label='hero', property_key='ename', property_value=int(suppress_hero[0]))
        )
        suppress_hero_rel['suppress_hero_tips'] = suppress_hero[1]
        g.create(suppress_hero_rel)

# create defeated hero relateion
for i in range(0, len(hero_data_list)):
    hero_ename = hero_data_list['ename'][i]
    defeated_hero_list = eval(hero_data_list['defeated_hero'][i])
    for defeated_hero in defeated_hero_list:
        defeated_hero_rel = Relationship(
            g.find_one(label='hero', property_key='ename', property_value=hero_ename),
            'defeated_hero',
            g.find_one(label='hero', property_key='ename', property_value=int(defeated_hero[0]))
        )
        defeated_hero_rel['defeated_hero_tips'] = defeated_hero[1]
        g.create(defeated_hero_rel)

# set the hero attribute which from 17173
# 1. load the 17173 hero attribute and store into a disc
heroattribute_data_list = pd.read_csv('./result/heroattribute.csv', header=0)
heroattribute_disc = {}
for i in range(0, len(heroattribute_data_list)):
    hero_key = heroattribute_data_list['hero_name'][i]

    heroAttribute = HeroAttributeItem(
        hero_name=heroattribute_data_list['hero_name'][i],
        max_lift=heroattribute_data_list['max_lift'][i],
        max_magic=heroattribute_data_list['max_magic'][i],
        physical_attack=heroattribute_data_list['physical_attack'][i],
        magic_attack=heroattribute_data_list['magic_attack'][i],
        physical_defence=heroattribute_data_list['physical_defence'][i],
        physical_reduce_rate=heroattribute_data_list['physical_reduce_rate'][i],
        magic_defence=heroattribute_data_list['magic_defence'][i],
        magic_reduce_rate=heroattribute_data_list['magic_reduce_rate'][i],
        mobility=heroattribute_data_list['mobility'][i],
        physical_guard_break=heroattribute_data_list['physical_guard_break'][i],
        magic_guard_break=heroattribute_data_list['magic_guard_break'][i],
        attack_velocity_increase=heroattribute_data_list['attack_velocity_increase'][i],
        heavy_attack_rate=heroattribute_data_list['heavy_attack_rate'][i],
        heavy_attack_affect=heroattribute_data_list['heavy_attack_affect'][i],
        physical_blood_sucking=heroattribute_data_list['physical_blood_sucking'][i],
        magic_blook_sucking=heroattribute_data_list['magic_blook_sucking'][i],
        cool_down_reduce=heroattribute_data_list['cool_down_reduce'][i],
        attack_scope=heroattribute_data_list['attack_scope'][i],
        toughness=heroattribute_data_list['toughness'][i],
        lift_refresh=heroattribute_data_list['lift_refresh'][i],
        magic_refresh=heroattribute_data_list['magic_refresh'][i],
    )

    heroattribute_disc[hero_key] = heroAttribute

# 2. set the attribute to hero node
for i in range(0, len(hero_data_list)):
    hero_ename = hero_data_list['ename'][i]
    hero_cname = hero_data_list['cname'][i]

    heroattribute = heroattribute_disc[hero_cname]

    hero_node = g.find_one(label='hero', property_key='ename', property_value=hero_ename)
    hero_node['max_lift'] = heroattribute['max_lift']
    hero_node['max_magic'] = heroattribute['max_magic']
    hero_node['physical_attack'] = heroattribute['physical_attack']
    hero_node['magic_attack'] = heroattribute['magic_attack']
    hero_node['physical_defence'] = heroattribute['physical_defence']
    hero_node['physical_reduce_rate'] = heroattribute['physical_reduce_rate']
    hero_node['magic_defence'] = heroattribute['magic_defence']
    hero_node['magic_reduce_rate'] = heroattribute['magic_reduce_rate']
    hero_node['mobility'] = heroattribute['mobility']
    hero_node['physical_guard_break'] = heroattribute['physical_guard_break']
    hero_node['magic_guard_break'] = heroattribute['magic_guard_break']
    hero_node['attack_velocity_increase'] = heroattribute['attack_velocity_increase']
    hero_node['heavy_attack_rate'] = heroattribute['heavy_attack_rate']
    hero_node['heavy_attack_affect'] = heroattribute['heavy_attack_affect']
    hero_node['physical_blood_sucking'] = heroattribute['physical_blood_sucking']
    hero_node['magic_blook_sucking'] = heroattribute['magic_blook_sucking']
    hero_node['cool_down_reduce'] = heroattribute['cool_down_reduce']
    hero_node['attack_scope'] = heroattribute['attack_scope']
    hero_node['toughness'] = heroattribute['toughness']
    hero_node['lift_refresh'] = heroattribute['lift_refresh']
    hero_node['magic_refresh'] = heroattribute['magic_refresh']

    #print hero_node
    g.push(hero_node)
