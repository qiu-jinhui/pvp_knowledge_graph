#coding=utf-8
import scrapy
import json

from pvpSpider.items import ItemItem


class ItemSpider(scrapy.Spider):
    def __init__(self):
        pass

    name = "itemSpider"
    allowed_domains = ["qq.com"]
    start_urls = [
        "http://pvp.qq.com/web201605/js/item.json"
    ]

    item_type_disc = {1: "攻击", 2: "法术", 3: "防御", 4: "移动", 5: "打野", 7: "辅助"}

    def parse(self, response):
        filename = 'data/' + response.url.split('/')[-1]
        with open(filename, 'wb') as f:
            f.write(response.body)

        itemlist = json.loads(response.body)

        for item in itemlist:
            itemItem = ItemItem()
            itemItem['item_id'] = item['item_id']
            itemItem['item_name'] = item['item_name']
            itemItem['item_type'] = self.item_type_disc[item['item_type']]
            itemItem['price'] = item['price']
            itemItem['total_price'] = item['total_price']
            itemItem['item_desc1'] = item['des1'].replace("<p>", "").replace("</p>", "").replace("<br>", " ")
            itemItem['item_desc2'] = item.get('des2', "").replace("<p>", "").replace("</p>", "").replace("<br>", " ")

            yield itemItem
