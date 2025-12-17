from agents.intentAgent import IntentAgent
from chain.baseHandler import BaseHandler
from messages.query import QueryMessage


class QueryMessageValidator(BaseHandler):
    def handle(self, context):
        message,orchestrator_self = context
        if(isinstance(message,QueryMessage)):
            print("QueryMessage Validator")
            intent_agent_addr = orchestrator_self.createActor(IntentAgent,globalName="IntentAgent")
            orchestrator_self.send(intent_agent_addr, message)
            return context
        return super().handle(context)
