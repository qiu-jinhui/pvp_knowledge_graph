from py2neo import Graph

from Objects import item

class ItemSearch():

    __graph = None

    def __init__(self):
        self.__graph = Graph("http://localhost:7474", username="neo4j", password="password")

    def search_item_by_name(self, name):
        return item.select(self.__graph).where(item_name=name).first()

