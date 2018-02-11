from py2neo import Graph

from Objects import hero

class HeroSearch():

    __graph = None

    def __init__(self):
        self.__graph = Graph("http://localhost:7474", username="neo4j", password="password")

    def search_hero_by_cname(self, hero_cname):
        return hero.select(self.__graph).where(cname=hero_cname).first()

    def search_hero_by_ename(self, hero_ename):
        return hero.select(self.__graph).where(ename=hero_ename).first()

    def search_hero_relation(self, hero_cname_1, hero_cname_2):
        #hero1 = hero.select(self.__graph).where(cname=hero_cname_1).first()
        #hero2 = hero.select(self.__graph).where(cname=hero_cname_2).first()
        cql1 = 'match (a:hero) <-[r]- (b:hero) where a.cname=\'' + hero_cname_1 + '\' and b.cname=\'' + hero_cname_2 + '\' return type(r)'
        cql2 = 'match (a:hero) -[r]-> (b:hero) where a.cname=\'' + hero_cname_1 + '\' and b.cname=\'' + hero_cname_2 + '\' return type(r)'

        returntype = self.__graph.data(cql1)

        if len(returntype) > 0:
            return str(hero_cname_1) + " -[" + str(returntype[0].get(u'type(r)')) + "]-> " + str(hero_cname_2)
        elif len(returntype) == 0:
            returntype = self.__graph.data(cql2)
            if len(returntype) > 0:
                return str(hero_cname_2) + " -[" + str(returntype[0].get(u'type(r)')) + "]-> " + str(hero_cname_1)

        return None

