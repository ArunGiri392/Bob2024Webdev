import requests
import json

# this is the image feature that i am currently working.
# API key obtained from Hugging face.
API_KEY = "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"
data = "anolamy"
MODEL_NAME = 'gpt2'

# Constructing the URL for the model endpoint
url = f'https://api-inference.huggingface.co/models/{MODEL_NAME}'

headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json'
}

# 