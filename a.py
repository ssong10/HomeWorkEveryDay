from typing import List, Text


class NoAgentFoundException(Exception):
    def __init__(self, m):
        self.m = m

    def __str__(self):
        return self.m


class Agent(object):
    def __str__(self):
        return "<Agent: {}>".format(self._name)


class Ticket(object):
    def __init__(self):

    pass


class FinderPolicy(object):
    def _filter_loaded_agents(self, agents: List[Agent]) -> List[Agent]:
        raise NotImplemented

    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        raise NotImplemented


class LeastLoadedAgent(FinderPolicy):
    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        raise NotImplemented


class LeastFlexibleAgent(FinderPolicy):
    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        raise NotImplemented
