import torch
from create_llm_model import Create_model

class generator:
    def __init__(self, model_name='Qwen 0.6B'):
        # Initialize model and tokenizer
        self.model, self.tokenizer = Create_model(model_name)
        self.name = model_name
        # Store the device the model is on
        self.device = next(self.model.parameters()).device

    def generate_answer(self, prompt):
        # Tokenize input and move to the same device as the model
        inputs = self.tokenizer(prompt, return_tensors="pt")
        inputs = {k: v.to(self.device) for k, v in inputs.items()}
        
        with torch.no_grad():
            output = self.model.generate(**inputs, max_new_tokens=256)
        
        out = self.tokenizer.decode(output[0], skip_special_tokens=True)
        out = out[len(prompt):]#.split('\n\n')[0]
        if 'Answer: ' in out:
            out = out.split('Answer: ')[-2]
        
        if '.' in out:
            out = out.split('.')[0]
        return out  
        
        
    
    def __call__(self, prompt):
        return self.generate_answer(prompt)