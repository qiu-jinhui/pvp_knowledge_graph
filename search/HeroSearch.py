from py2neo import Graph


class HeroSearch():

    __graph = None

    def __init__(self):
        self.__graph = Graph("http://localhost:7474", username="neo4j", password="password")


    def search_hero(self, hero_name):
        self.__graph