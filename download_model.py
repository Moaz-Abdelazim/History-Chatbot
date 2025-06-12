from transformers import AutoTokenizer, AutoModelForCausalLM

#Qwen 0.6
output_path = './Qwen-0.6B'
# Load model only once (shared across calls)
tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen3-0.6B", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen3-0.6B", trust_remote_code=True)

model.save_pretrained(output_path)
tokenizer.save_pretrained(output_path)

print(f"Saved at : {output_path}")


#Qwen 1.8
output_path = './Qwen-1_8B-Chat'
# Load model only once (shared across calls)
tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen-1_8B-Chat", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen-1_8B-Chat", trust_remote_code=True)

model.save_pretrained(output_path)
tokenizer.save_pretrained(output_path)

print(f"Saved at : {output_path}")