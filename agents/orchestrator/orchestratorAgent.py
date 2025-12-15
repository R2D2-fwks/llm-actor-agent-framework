from pyexpat import model
from thespian.actors import Actor
from model.llama_model import LlamaModel
from model.model_adapter import ModelAdapter
from agents import AgentRegistry, GreetAgent,IntentAgent
from messages import LLMResponse

class OrchestratorAgent(Actor):
    def __init__(self):
        super().__init__()
        self.model = ModelAdapter(LlamaModel())
        self.agent_name = "OrchestratorAgent"
        self.child_actor="IntentAgent"
        self.agent_description = """Act as an agent that orchestrates tasks. We will be having three layers 
        of Agents interaction.First Layer will be intent layer What is the intent of the prompt given by the user.
        Second layer will be to find out the agent from the registry which we have registered to find the appropriate agent.
        Third layer will be to pass the prompt and the intent to business layer agent to get the action done based on the intent which
        in turn will connect with data layer agents to get the data and perform the action. And all of these communication will be done via
        this Orchestrator agent."""
    def receiveMessage(self, message, sender):
        if isinstance(message, str):
            my_addr = self.myAddress
            intent_agent_addr = self.createActor(IntentAgent,globalName=self.child_actor)
            self.send(intent_agent_addr, (message,my_addr))
        elif
        else:
            self.send(sender, "Unknown command. Please send 'greet' to receive a greeting.")