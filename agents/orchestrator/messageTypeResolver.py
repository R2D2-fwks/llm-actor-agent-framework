from agents.orchestrator.actorMessageValidator import ActorMessageValidator
from agents.orchestrator.intentAgentMessageValidator import IntentAgentMessageValidator
from agents.orchestrator.llmResponseValidator import LLMResponseValidator
from agents.orchestrator.queryMessageValidator import QueryMessageValidator

def checkMessage(context):
    llm_response_validator = LLMResponseValidator()
    query_message_validator = QueryMessageValidator()
    actor_message_validator = ActorMessageValidator()
    intent_agent_message_validator = IntentAgentMessageValidator()
    llm_response_validator.set_next(query_message_validator).set_next(actor_message_validator).set_next(intent_agent_message_validator)
    return llm_response_validator.handle(context)