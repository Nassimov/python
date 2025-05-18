from transformers import pipeline
while True:
    inputs =  input()
    messages = [
        {"role": "user", "content": f"{inputs}"},
    ]
    pipe = pipeline("text-generation", model="deepseek-ai/DeepSeek-V3-0324", trust_remote_code=True)
    pipe(messages)