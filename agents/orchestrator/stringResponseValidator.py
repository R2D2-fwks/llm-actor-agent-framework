from chain.baseHandler import BaseHandler


class StringResponseValidator(BaseHandler):
    def handle(self, context):
        message,orchestrator_address= context
        if isinstance(message,string):
            # do action
            return message
        return super().handle(context)