from ollama import Client

# Initialize the client
client = Client()

# Simple test function
def hazard_query(query: str):
    response = client.chat(
        model="llama3",
        messages=[
            {"role": "system", "content": "You are a hazard analysis assistant. You analyze risks and hazards in detail."},
            {"role": "user", "content": query}
        ]
    )
    return response['message']['content']

if __name__ == "__main__":
    user_input = input("Enter a hazard or risk to analyze: ")
    print("\n--- Hazard Analysis ---")
    print(hazard_query(user_input))
