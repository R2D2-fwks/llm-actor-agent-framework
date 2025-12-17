from chain.baseHandler import BaseHandler
from messages.query import QueryMessage


class QueryMessageValidator(BaseHandler):
    def handle(self, context):
        message,orchestrator_address = context
        if(isinstance(message,QueryMessage)):
            print("QueryMessage Validator")
            return message
        return super().handle(context)
