import os

from dotenv import load_dotenv
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate

# Load environment variables from .env file
load_dotenv()

# Get the OpenAI API key from the environment variable
api_key = os.getenv("OPENAI_API_KEY")


# Initialize OpenAI language model
llm = OpenAI(api_key=api_key)

# Define the prompt template
prompt_template = PromptTemplate(
    input_variables=["question"],
    template="You are a knowledgeable assistant. Answer the following question: {question}"
)

# Create the chain
chain = prompt_template | llm

first_iteration = True
# Get the question from user input
while True:
    if first_iteration:
        # First iteration message
        print("You can type 'exit' to quit at any time.")
        print("Hello! I am your knowledge assistant. How can I help you today?")
        first_iteration = False
    else:
        # Subsequent iteration message
        print("Please enter your next question:")

    question = input()

    # Check if the user wants to exit
    if question.lower() == "exit":
        print("Ok, bye!")
        print("Exiting the application.")
        break

    # Use the chain to answer the question
    answer = chain.invoke({ "question": question })
    print(answer.strip())
    print("")