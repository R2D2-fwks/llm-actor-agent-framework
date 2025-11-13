from thespian.actors import ActorSystem
from agents.greetAgent import GreetAgent
import json

if __name__ == "__main__":
    with open('capabilities.json', 'r') as f:
        capabilities = json.load(f)
        system = ActorSystem(capabilities=capabilities)
        greet_actor = system.createActor(GreetAgent)
        response = system.ask(greet_actor, "greet")
        print(f"Response from GreetAgent: {response.text}")