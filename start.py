from agents.agentRegistry import AgentRegistry
from agents.greetAgent import GreetAgent
from thespian.actors import ActorSystem
from agents import OrchestratorAgent
import json

if __name__ == "__main__":
    with open('capabilities.json', 'r') as f:
        capabilities = json.load(f)
        query = "hello how are you ?"
        system = ActorSystem(capabilities=capabilities)
        orchestrator_agent = system.createActor(OrchestratorAgent)
        agent_registry=AgentRegistry()
        agent_registry.register_agents([GreetAgent])
        response = system.ask(orchestrator_agent, query)
        # print(type(response.text))
        res = json.loads(response.text)
        print(res["response"])