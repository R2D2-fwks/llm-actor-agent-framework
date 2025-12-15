class AgentSingleton(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
class AgentRegistry(metaclass=AgentSingleton):
    def __init__(self):
        self.agents=[]
    def register_agent(self,agent):
        self.agents.append(agent)
    def register_agents(self,agents):
      self.agents = self.agents+agents
    def get_agents(self):
        return self.agents
    

        