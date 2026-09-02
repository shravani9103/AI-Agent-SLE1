# Basic Rule-Based AI Agent
# SLE-1 - Introduction to Artificial Intelligence

def ai_agent(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! I am your basic AI Agent."

    elif "study" in user_input:
        return "You should create a study plan and practice regularly."

    elif "python" in user_input:
        return "Python is widely used in Artificial Intelligence and Machine Learning."

    elif "bye" in user_input:
        return "Goodbye! Keep learning AI."

    else:
        return "I am still learning. Please ask me about Python, study, or AI."


print("================================")
print("       BASIC AI AGENT")
print("================================")
print("Type 'bye' to exit.")

while True:
    user_input = input("You: ")

    response = ai_agent(user_input)

    print("Agent:", response)

    if "bye" in user_input.lower():
        break