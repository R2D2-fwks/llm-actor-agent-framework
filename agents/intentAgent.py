from pyexpat import model
from thespian.actors import Actor
from model.llama_model import LlamaModel
from model.model_adapter import ModelAdapter

class IntentAgent(Actor):
    def __init__(self):
        super().__init__()
        self.model = ModelAdapter(LlamaModel())
        self.agent_name = "IntentAgent"
        self.agent_description = """Act as an agent that identifies the intent of the user's prompt in one word and match with"""
    def receiveMessage(self, message, sender):
        if isinstance(message, str):
            message = self.agent_description + " " + message
            response = self.model.generate(message)
            self.send(sender, response)
        else:
            self.send(sender, "Unknown command. Please send 'greet' to receive a greeting.")