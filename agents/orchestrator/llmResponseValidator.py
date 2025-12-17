import json
from chain.baseHandler import BaseHandler
from messages.llm_message import LLMMessage
# import os
# from dotenv import load_dotenv

class LLMResponseValidator(BaseHandler):
    def handle(self, context):
        message,orchestrator_self = context
        if isinstance(message,LLMMessage):
            msg = message.message
            # load_dotenv()
            # manual_override = os.getenv('MANUAL_OVERRIDE')
            print("Action from CheckLLm response")
            res = json.loads(msg.text)
            print(res["response"])
            return res["response"]
        return super().handle(context)
        
    