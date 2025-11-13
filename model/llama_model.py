from model.model_interface import ModelInterface
import requests

class LlamaModel(ModelInterface):
    def __init__(self):
        super().__init__()
        self.model_name = "llama3"
        self.model_url = "http://127.0.0.1:11434"
        self.headers = {'Content-Type': 'application/json'}
    def generate(self, prompt: str) -> str:
        # Generate a response using the LLaMA model
        payload = {
            "model": self.model_name,
            "prompt": prompt,
            "stream": False
        }
        url = f"{self.model_url}/api/generate"
        response = requests.post(url, 
        headers=self.headers, 
        json=payload,
        timeout=60)
        return response

    # def curate_response(self, response: str) -> str:
    #     # Curate the response to ensure quality and relevance
    #     curated_response = response.strip()
    #     return curated_response