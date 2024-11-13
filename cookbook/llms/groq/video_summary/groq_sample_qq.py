from phi.llm.groq import Groq
from phi.assistant import Assistant

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()  # This loads all environment variables from the .env file


def ask_groq_question(question: str):
    model = "llama3-70b-8192"  # You can change this to another model if needed
    groq_model = Groq(model=model)

    assistant = Assistant(
        name="groq_question_answering",
        llm=groq_model,
        description="You are an assistant answering user questions based on Groq's capabilities.",
        instructions=["You will be provided with a question. Your task is to provide a clear and concise answer based on the knowledge of Groq."],
        add_datetime_to_instructions=True,
        debug_mode=True
    )
    
    # Run the Assistant with the provided question
    response = assistant.run(question)
    
    # Since it's a generator, we need to iterate through it
    return "".join([part for part in response])

# Example usage
question = "What is the capital of France?"
response = ask_groq_question(question)

print(response)  # Output will be the answer from Groq


# from phi.llm.groq import Groq
# from phi.assistant import Assistant

# # Define the Assistant with Groq
# def ask_groq_question(question: str):
#     # Initialize the Groq model
#     model = "llama3-70b-8192"  # You can change this to another model if needed
#     groq_model = Groq(model=model)

#     # Define the assistant with a simple task
#     assistant = Assistant(
#         name="groq_question_answering",
#         llm=groq_model,
#         description="You are an assistant answering user questions based on Groq's capabilities.",
#         instructions=[
#             "You will be provided with a question. Your task is to provide a clear and concise answer based on the knowledge of Groq.",
#         ],
#         add_datetime_to_instructions=True,
#         debug_mode=True
#     )
    
#     # Run the Assistant with the provided question
#     response = assistant.run(question)
    
#     # Return the answer
#     return response

# # Example usage
# question = "What is the capital of France?"
# response = ask_groq_question(question)

# print(response)  # Output will be the answer from Groq
