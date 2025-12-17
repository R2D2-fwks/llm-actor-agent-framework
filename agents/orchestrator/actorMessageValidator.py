from chain.baseHandler import BaseHandler
from thespian.actors import ActorExitRequest,ChildActorExited, PoisonMessage,WakeupMessage,DeadEnvelope,ActorSystemConventionUpdate

class ActorMessageValidator(BaseHandler):
    def handle(self, context):
        message, orchestrator_self = context
        if(isinstance(message,(ActorExitRequest, ChildActorExited, PoisonMessage, WakeupMessage, DeadEnvelope, ActorSystemConventionUpdate))):
            # do action when the message is recived from the actor
            print("ActorMessage Validator")
            return context
        return super().handle(context)