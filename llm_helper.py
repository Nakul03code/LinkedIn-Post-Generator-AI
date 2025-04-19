import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Manually set the API key for testing
os.environ["GROQ_API_KEY"] = "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"

# Now try to load it
api_key = os.getenv("GROQ_API_KEY")

# Create the ChatGroq client with the manually set API key
llm = ChatGroq(groq_api_key=api_key, model_name="llama-3.1-8b-instant")

if __name__ == "__main__":
# Test invocation (replace with a valid query)
    response = llm.invoke("Two most important ingredients in samosa are")
    print(response.content)
