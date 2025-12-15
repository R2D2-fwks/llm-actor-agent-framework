from chain.baseHandler import BaseHandler
from messages.llmResponse import LLMResponse


class CheckLLmResponse(BaseHandler):
    def handle(self, message):
        if isinstance(message,LLMResponse):
            # do action
            return message
        
    