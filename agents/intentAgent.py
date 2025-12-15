from pyexpat import model
from messages.llmResponse import LLMResponse
from thespian.actors import Actor
from model.llama_model import LlamaModel
from model.model_adapter import ModelAdapter
from agents import GreetAgent,AgentRegistry
class IntentAgent(Actor):
    def __init__(self):
        super().__init__()
        self.model = ModelAdapter(LlamaModel())
        self.agent_name = "IntentAgent"
        self.agent_description = """Act as an agent that identifies the intent of the user's prompt in one word and match with agent registry give the json response."""
    def receiveMessage(self, msg, sender):
        if isinstance(msg, tuple):
            message,reply_to= msg
            agent_registry=AgentRegistry()
            agents = agent_registry.get_agents()
            agent_string = ",".join([str(obj) for obj in agents])
            message = self.agent_description + " " + message+" "+agent_string
            response = LLMResponse(self.model.generate(message))
            print(reply_to)
            self.send(reply_to, response)
        else:
            self.send(sender, "Unknown command. Please send 'greet' to receive a greeting.")