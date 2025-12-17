from pyexpat import model
from messages.intent_agent_message import IntentAgentMessage
from messages.llm_message import LLMMessage
from thespian.actors import Actor
from model.llama_model import LlamaModel
from model.model_adapter import ModelAdapter

class GreetAgent(Actor):
    def __init__(self):
        super().__init__()
        self.model = ModelAdapter(LlamaModel())
        self.agent_name = "GreetAgent"
        self.agent_description = "Act as an agent that greets users."
    def receiveMessage(self, message, sender):
        if (isinstance(message, IntentAgentMessage)):
            query = message.query
            print("GreetAgent received query:", query)
            complete_message = self.agent_description + " " + query
            response = LLMMessage(self.model.generate(complete_message))
            self.send(sender, response)
        else:
            self.send(sender, "Unknown command. Please send 'greet' to receive a greeting.")