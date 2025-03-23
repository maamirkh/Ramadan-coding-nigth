import google.generativeai as genai # for google api
from dotenv import load_dotenv # for loading environment variables
import os # for environment variables

load_dotenv() # load environment variables from .env file

genai.configure(api_key=os.environ["GEMINI_API_KEY"]) # configure google api with api key

model = genai.GenerativeModel(model_name="gemini-2.0-flash")# create a generative model instance

while True: # infinite loop

    user_input = input("\nEnter your question (or 'quit' to exit): ")  # get user input
    
    if user_input.lower() == "quit": # check if user wants to exit
        print("Thanks for chatting! Goodbye!") # print goodbye message
        break 


    response = model.generate_content(user_input) # generate response using the model

    print("\nResponse:", response.text) # print the response


