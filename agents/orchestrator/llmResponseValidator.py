from chain.baseHandler import BaseHandler
from messages.llm_message import LLMMessage


class LLMResponseValidator(BaseHandler):
    def handle(self, context):
        message,orchestrator_self = context
        if isinstance(message,LLMMessage):
            # do action
            print("Action from CheckLLm response")
            return context
        return super().handle(context)
        
    