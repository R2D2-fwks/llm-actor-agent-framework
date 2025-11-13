from abc import abstractmethod


class ModelInterface:
    @abstractmethod
    def generate(self, prompt: str) -> str:
        pass