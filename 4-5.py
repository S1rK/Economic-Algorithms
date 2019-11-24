"""
Economic Algorithms
Exercise 4 , Question 5
AUTHOR: Tal Nakar
SINCE:  24-11-2019
"""

from typing import List


class Agent:
    @staticmethod
    def item(item_index: int) -> float:
        """
        :param item_index: the index of the item.
        :return: The value the agent give to a certain item.
        """
        raise NotImplemented("")

    @staticmethod
    def name() -> str:
        raise NotImplemented("")


def is_EF1(agents: List[Agent], bundles: List[List[int]]) -> bool:
    """
    :param agents: the agents involved in the distribution.
    :param bundles: a list that represent teh distribution: bundles[i] is a list of item indexes that agent i gets.
    :return: If it's a free envy distribution except 1.
    """
    # before we start, check if both lists with the length
    if len(agents) != len(bundles):
        raise Exception("Agents and bundles lists aren't with the same length.")
    # we will check if every agent envy any other
    for i in range(len(agents)):
        # the current agent
        current_agent = agents[i]
        # calc it's own item's value
        current_value = sum([current_agent.item(item) for item in bundles[i]])

        # for each agent which isn't the current agent
        for j in range(len(agents)):
            # if it's the same agent, skip him
            if i == j:
                continue

            # save the other agent
            other = agents[j]
            # the other's item's value in the eye of the current agent
            other_value = sum([current_agent.item(item) for item in bundles[j]])

            # if current agent doesn't envy the other, skip him
            if current_value >= other_value:
                continue

            # the current agent envy the other
            # if we drop one item from the other
            for item in bundles[j]:
                # if the current won't envy the other after dropping one of the other's item, it's EF1
                # so continue to the next agent
                if current_value >= other_value - current_agent.item(item):
                    break

            # if finished the inner loop adn didn't break from it, then
            else:
                # if we got to here, it means that there is no item that we can take from the other agent
                # that will stop the current agent from envying the other, so it's not EF1
                # return False
                return False

    # if we got to here it means that it's EF1, so return True
    return True


# def is_EF1(agents: List[Agent], bundles: List[int]) -> bool:
#     """
#     :param agents: the agents involved in the distribution.
#     :param bundles: a list that represent teh distribution: bundles[i] is a list of item indexes that agent i gets.
#     :return: If it's a free envy distribution except 1.
#     """
#     return is_EF1(agents, [[item] for item in bundles])


def test():
    """
    Testing the is_EF1 function
    :return: Nothing, void.
    """
    # define few agents
    class Alice(Agent):
        @staticmethod
        def item(item_index: int) -> float:
            """
            :param item_index: the index of the item.
            :return: The value the agent give to a certain item.
            """
            return (item_index+1) % 2

        @staticmethod
        def name() -> str:
            return "Alice"

    print("Alice's item(item_index) = (item_index+1) % 2")

    class Bob(Agent):
        @staticmethod
        def item(item_index: int) -> float:
            """
            :param item_index: the index of the item.
            :return: The value the agent give to a certain item.
            """
            return item_index % 2

        @staticmethod
        def name() -> str:
            return "Bob"

    print("Bob's item(item_index) = item_index % 2")

    class Charlie(Agent):
        @staticmethod
        def item(item_index: int) -> float:
            """
            :param item_index: the index of the item.
            :return: The value the agent give to a certain item.
            """
            return 3 * (item_index % 2)

        @staticmethod
        def name() -> str:
            return "Charlie"

    print("Charlie's item(item_index) = 3 * (item_index % 2)")

    alice = Alice()
    bob = Bob()
    charlie = Charlie()

    # first test
    print("------------First Test------------")
    print("distribution: Alice: [0,2], Bob: [1,3]")
    print("EF1 = " + is_EF1([alice, bob], [[0, 2], [1, 3]]).__str__())

    # second test
    print("------------Second Test------------")
    print("distribution: Alice: [1,3], Bob: [0,2]")
    print("EF1 = " + is_EF1([alice, bob], [[1, 3], [0, 2]]).__str__())

    # third test
    print("------------Third Test------------")
    print("distribution: Alice: [1,3], Bob: [0,2]")
    print("EF1 = " + is_EF1([alice, bob], [[0, 1, 3], [2]]).__str__())

    # fourth test
    print("------------Fourth Test------------")
    print("distribution: Alice: [0,2], Bob: [1], Charlie: [3]")
    print("EF1 = " + is_EF1([alice, bob, charlie], [[0, 2], [1], [3]]).__str__())

    # fifth test
    print("------------Fifth Test------------")
    print("distribution: Alice: [0,2], Bob: [1,3], Charlie: [5]")
    print("EF1 = " + is_EF1([alice, bob, charlie], [[0, 2], [1, 3], [5]]).__str__())

    # sixth test
    print("------------Sixth Test------------")
    print("distribution: Alice: [0,2], Bob: [1,3], Charlie: [4, 5]")
    print("EF1 = " + is_EF1([alice, bob, charlie], [[0, 2], [1, 3], [4, 5]]).__str__())


def main():
    test()


if __name__ == "__main__":
    main()
