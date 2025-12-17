from pyexpat import model
from messages.llm_message import LLMMessage
from messages.query import QueryMessage
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
        if isinstance(msg, QueryMessage):
            message = msg.message
            agent_registry=AgentRegistry()
            agents = agent_registry.get_agents()
            agent_string = ",".join([str(obj) for obj in agents])
            print("agent_string----->>", agent_string)
            message = self.agent_description + " " + message+" "+agent_string
            response = LLMMessage(self.model.generate(message))
            self.send(sender, response)
        else:
            self.send(sender, "Unknown command. Please send 'greet' to receive a greeting.")