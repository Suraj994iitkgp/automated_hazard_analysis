from ollama import Client

client = Client()

response = client.chat(model="llama3", messages=[
    {"role": "user", "content": "Hello Llama 3, can you confirm you are working?"}
])

print(response['message']['content'])
