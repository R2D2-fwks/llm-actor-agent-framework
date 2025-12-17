from agents.agentRegistry import AgentRegistry
from chain.baseHandler import BaseHandler
from messages.intent_agent_message import IntentAgentMessage


class IntentAgentMessageValidator(BaseHandler):
    def handle(self, context):
        message, orchestrator_self = context
        if(isinstance(message, IntentAgentMessage)):
            agent_name = message.message.get("response", None)
            if agent_name is not None:
                agent = AgentRegistry().get_agent(agent_name)
                print("Creating Action Agent:", agent_name)
                action_agent_addr = orchestrator_self.createActor(agent)
                orchestrator_self.send(action_agent_addr, message)
            print("IntentAgentMessage Validator", agent_name)
            return context
        return super().handle(context)
    