from agents.orchestrator import messageTypeResolver
from thespian.actors import Actor
from model.llama_model import LlamaModel
from model.model_adapter import ModelAdapter
from thespian.troupe import troupe
@troupe(max_count=10, idle_count=3)
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
        orchestrator= self
        context=(message,orchestrator)
        response= messageTypeResolver.checkMessage(context)
        print("Response from archestrator=--->",response)
        # self.send(sender,response)

        