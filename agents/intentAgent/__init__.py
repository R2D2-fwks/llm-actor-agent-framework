import json
from pyexpat import model
from tracemalloc import start
from urllib import response
from messages.intent_agent_message import IntentAgentMessage
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
        self.agent_description = """Act as an agent that identifies the intent of the user's prompt 
        in one word and match with agent registry give the json response. 
        The response structure should be like {"response":"agent_name"} 
        where intent_word is the identified intent in one word."""
    def receiveMessage(self, msg, sender):
        if isinstance(msg, QueryMessage):
            message = msg.message
            agent_registry=AgentRegistry()
            agents = agent_registry.get_agents()
            agent_string = ",".join([str(obj) for obj in agents])
            complete_message = self.agent_description + " " + message+" "+agent_string
            llm_response = self.model.generate(complete_message)

            message = IntentAgentMessage(self.parse_response(llm_response),message)
            self.send(sender, message)
        else:
            self.send(sender, "Unknown command. Please send 'greet' to receive a greeting.")

    def parse_response(self, response: str) -> str:
        raw_message = response.text
        message = json.loads(raw_message)
        text_response = message.get("response", None)
        if text_response is not None:
            start = text_response.find('{')
            end = text_response.rfind('}') + 1
            json_str = text_response[start:end]
            next_agent_name = json.loads(json_str)
            return next_agent_name
        return None
        # Implement parsing logic specific to IntentAgent