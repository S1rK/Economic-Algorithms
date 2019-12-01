from typing import List
import networkx


class OrdinalAgent(object):
    def best_room(self, prices: List[int]) -> int:
        """
        INPUT:  the prices of the n rooms.
        OUTPUT: the index of room that the agent most prefers in therese prices. index is between 0 and n-1.
        """
        raise NotImplemented()


class Alice(OrdinalAgent):
    def best_room(self, prices: List[int]) -> int:
        return 0


class Bob(OrdinalAgent):
    def best_room(self, prices: List[int]) -> int:
        return 1


class Charlie(OrdinalAgent):
    def best_room(self, prices: List[int]) -> int:
        return 2


def find_almost_envy_free(agens:List[OrdinalAgent], totalRent:int):

    shiz = []
    for agent, room, price in shiz:
        print("Agent %d recives room %d for %d shekels" % (agent, room, price))


alice = Alice()
bob = Bob()
charlie = Charlie()

find_almost_envy_free([alice, bob, charlie], 5000)
