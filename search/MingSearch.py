from py2neo import Graph

from Objects import ming

class MingSearch():

    __graph = None

    def __init__(self):
        self.__graph = Graph("http://localhost:7474", username="neo4j", password="password")

    def search_ming_by_name(self, name):
        return ming.select(self.__graph).where(ming_name=name).first()

