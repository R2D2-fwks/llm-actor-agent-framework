
from agents.orchestrator.LLmResponseValidator import LLMResponseValidator


def checkMessage(context):
    llmResponse = LLMResponseValidator()
    
    llmResponse.set_next()
    return llmResponse.handle(context)