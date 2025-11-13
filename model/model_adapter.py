from model.model_interface import ModelInterface


class ModelAdapter(ModelInterface):
    def __init__(self, model: ModelInterface):
        super().__init__()
        self.model = model

    def generate(self, prompt: str) :
        return self.model.generate(prompt)

    def getModel(self) -> ModelInterface:
        return self.model