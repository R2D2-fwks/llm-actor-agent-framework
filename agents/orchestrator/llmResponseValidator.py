from agents.intentAgent import IntentAgent
from chain.baseHandler import BaseHandler
from messages.llm_message import LLMMessage


class LLMResponseValidator(BaseHandler):
    def handle(self, context):
        message,orchestrator_address = context
        if isinstance(message,LLMMessage):
            # do action
            print("Action from CheckLLm response")
            intent_agent_addr = self.createActor(IntentAgent,globalName=self.child_actor)
            self.send(intent_agent_addr, (message,orchestrator_address))
            return message
        return super().handle(message)
        
    