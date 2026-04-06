# This is a simple example of how to call an Ollama LLM (Language Model) using Python.
# It sends a prompt to the model and prints the response. Make sure you have Ollama running locally and the specified model available.
# Note: This example assumes you have the Ollama API running on localhost at port 11434 and that you have a model named "gemma2:2b" available.

import requests
import json

def chat_with_llm(prompt, model="gemma2:2b"):
    url = "http://localhost:11434/api/generate"
    
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False  # get the full response at once
    }
    
    response = requests.post(url, json=payload)
    result = response.json()
    
    return result["response"]

# Test it
answer = chat_with_llm("How is AI agent is different from Agentic AI?")
print(answer)