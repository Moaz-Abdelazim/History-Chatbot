import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

def Create_model(model_name='Qwen 0.6B'):
    # Determine device (GPU if available, else CPU)
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    
    if model_name == 'Qwen 0.6B':
        model_path = './Qwen-0.6B'
    elif model_name == 'Qwen 1.8B':
        model_path = './Qwen-1_8B-Chat'
    else:
        raise ValueError(f"Unsupported model: {model_name}")

    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(model_path, trust_remote_code=True)
    
    # Move model to the appropriate device
    model.to(device)
    
    return model, tokenizer

