import requests
import json

# API key obtained from Hugging face.
API_KEY = "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"


MODEL_NAME = 'gpt2'

# Constructing the URL for the model endpoint
url = f'https://api-inference.huggingface.co/models/{MODEL_NAME}'

headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json'
}

# Define the prompt and parameters
prompt = "Imagine You are an expert in Analyzing the NFL data. You have all the required historical data and you should be using data that you know to answer question specific to NFL.If you do not know about the data, strictly say that you are not aware about the data. If user ask about two players, try to user thier respective performances, and records to make a comparision between them."
params = {
    'inputs': prompt,
    'parameters': {
        'max_new_tokens': 250,  # Adjust as per your requirement
        'num_return_sequences': 1  # Adjust if you want more sequences
    }
}

# Make a POST request to the model endpoint
response = requests.post(url, headers=headers, data=json.dumps(params))

# Check if the request was successful
if response.status_code == 200:
    # Parse the response JSON
    response_data = response.json()
   
    # The response might be a list of items if num_return_sequences > 1
    # Handling response data appropriately based on its structure
    if isinstance(response_data, list):
        # If response_data is a list, iterate and print generated text for each
        for item in response_data:
            print(item.get('generated_text', 'Generated text not found'))
    else:
        # If it's not a list, attempt to directly access 'generated_text'
        print(response_data.get('generated_text', 'Generated text not found'))
else:
    print(f"Error: {response.status_code}, {response.reason}")
