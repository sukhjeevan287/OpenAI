import requests


api_key = ""

url = ""

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

data = {
    "model": "gpt-4o-mini",
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What's the capital of France?"}
    ],
    "temperature": 0.7
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    reply = response.json()['choices'][0]['message']['content']
    print("AI:", reply)
else:
    print("Error:", response.status_code, response.text)
