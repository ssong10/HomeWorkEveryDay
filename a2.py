from typing import List, Text


class NoAgentFoundException(Exception):
    def __init__(self, m):
        self.m = m

    def __str__(self):
        return self.m

class Agent(object):
    def __init__(self,name,skills,load):
        self.name = name
        self.skills = set()
        for skill in skills:
            self.skills.add(skill)
        self.load = load

    @property
    def _name(self):
        return self.name

    def __str__(self):
        return "<Agent: {}>".format(self._name)


class Ticket(object):
    def __init__(self,id,restrictions):
        self.id = id
        self.restrictions = set()
        for restriction in restrictions:
            self.restrictions.add(restriction)



class FinderPolicy(object):
    def _filter_loaded_agents(self, agents: List[Agent]) -> List[Agent]:
        raise NotImplemented

    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        raise NotImplemented


class LeastLoadedAgent(FinderPolicy):
    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        leastloaded = None
        for agent in agents:
            if leastloaded:
                if agent.load < leastloaded.load:
                    leastloaded = agent
            else:
                leastloaded = agent
        return leastloaded


class LeastFlexibleAgent(FinderPolicy):
    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        Flexible = None
        for agent in agents:
            try:
                if Flexible:
                    if ticket.restrictions in agent.skills:
                        if agent.load < 3:
                            for restriction in ticket.restrictions:
                                if restriction not in agent.skills:
                                    break
                            else:
                                Flexible = agent
                        else:
                            raise NoAgentFoundException
                else:
                    for restriction in ticket.restrictions:
                        if restriction not in agent.skills:
                            break
                    else:
                        Flexible = agent
            except Exception as e:
                return NoAgentFoundException
        return Flexible

ticket = Ticket(id="1", restrictions=["English"])

agent1 = Agent(name="A", skills=["English"], load=2)
agent2 = Agent(name="B", skills=["English", "Japanese"], load=0)
least_loaded_policy = LeastLoadedAgent()
least_loaded_policy.find(ticket, [agent1, agent2])

least_flexible_policy = LeastFlexibleAgent()
least_flexible_policy.find(ticket, [agent1, agent2])