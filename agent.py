 # Ollama AI Agent
# SLE-1 - Introduction to Artificial Intelligence

import ollama


def ai_agent(user_input):
    response = ollama.chat(
        model="llama3.2:latest",
        messages=[
            {
                "role": "user",
                "content": user_input
            }
        ]
    )

    return response["message"]["content"]


print("================================")
print("       OLLAMA AI AGENT")
print("================================")
print("Type 'bye' to exit.")

while True:
    user_input = input("You: ")

    if user_input.lower() == "bye":
        print("Agent: Goodbye! Keep learning AI.")
        break

    response = ai_agent(user_input)
    print("Agent:", response)