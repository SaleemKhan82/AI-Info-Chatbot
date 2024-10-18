import streamlit as st

# A dictionary of predefined AI-related questions and answers
ai_info = {
    "What is AI?": "AI stands for Artificial Intelligence, which refers to the simulation of human intelligence in machines that are programmed to think and act like humans.",
    "What is machine learning?": "Machine learning is a subset of AI that allows systems to learn from data and improve performance over time without being explicitly programmed.",
    "What is deep learning?": "Deep learning is a type of machine learning that uses neural networks with many layers to model complex patterns in data.",
    "What is natural language processing (NLP)?": "NLP is a field of AI that focuses on the interaction between computers and humans through natural language. Examples include language translation, sentiment analysis, and chatbots.",
    "What are neural networks?": "Neural networks are a series of algorithms that attempt to recognize relationships in a set of data by mimicking the way a human brain operates.",
    "What is reinforcement learning?": "Reinforcement learning is an area of machine learning where an agent learns to make decisions by taking actions in an environment to maximize cumulative rewards."
}

# Function to generate AI response
def get_ai_info(user_input):
    # Return a predefined answer if the question is known, otherwise give a default response
    return ai_info.get(user_input, "Sorry, I don't have information on that. Please ask something else about AI.")

# Streamlit app structure
st.title("AI Information Chatbot")
st.write("Ask anything related to AI, and I will provide information.")

# User input field
user_input = st.text_input("Enter your question about AI:")

# Check if user input is provided and display the chatbot response
if user_input:
    response = get_ai_info(user_input)
    st.write(f"Chatbot: {response}")
