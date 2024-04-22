import transformers
import torch


class InferlessPythonModel:
    def initialize(self):
        self.model_id = "Undi95/Meta-Llama-3-8B-hf"
        self.pipeline = transformers.pipeline(
            "text-generation",
            model=self.model_id,
            model_kwargs={"torch_dtype": torch.bfloat16},
            device_map="auto"
        )

    def infer(self, inputs):
        prompt = inputs["prompt"]
        return self.pipeline(prompt)

    def finalize(self):
        self.pipeline = None
