from agents.orchestrator.actorMessageValidator import ActorMessageValidator
from agents.orchestrator.llmResponseValidator import LLMResponseValidator
from agents.orchestrator.queryMessageValidator import QueryMessageValidator

def checkMessage(context):
    llm_response_action = LLMResponseValidator()
    query_message_action = QueryMessageValidator()
    actor_message_action = ActorMessageValidator()
    llm_response_action.set_next(query_message_action).set_next(actor_message_action)
    return llm_response_action.handle(context)