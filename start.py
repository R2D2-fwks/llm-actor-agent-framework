from agents.agentRegistry import AgentRegistry
from agents.greetAgent import GreetAgent
from messages.query import QueryMessage
from thespian.actors import ActorSystem
from agents import OrchestratorAgent
import json

if __name__ == "__main__":
    with open('capabilities.json', 'r') as f:
        capabilities = json.load(f)
        query = QueryMessage("hello how are you ?")
        system = ActorSystem(capabilities=capabilities)
        orchestrator_agent_address = system.createActor(OrchestratorAgent)
        agent_registry=AgentRegistry()
        agent_registry.register_agents([GreetAgent])
        response = system.ask(orchestrator_agent_address, query)
        # print(type(response.text))
        res = json.loads(response.text)
        print(res["response"])