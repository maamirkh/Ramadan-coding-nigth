import os # for environment variable
import chainlit as cl # for chainlit interface
import google.generativeai as genai # for google api
from dotenv import load_dotenv # for loading environment variable

load_dotenv # load environment variable from .env file

gemini_api_key = os.getenv('GEMINI_API_KEY') # get gemini api key from environment variable

genai.configure(api_key=gemini_api_key) # configure google api with gemini api key

model = genai.GenerativeModel(
    model_name="gemini-2.0-flash"
) # create a generative Gemini model instance

@cl.on_chat_start # chainlit decorator for chat start event
async def handle_chat_start():
    await cl.Message(content="Hello how can I help you today?").send()

@cl.on_message # chainlit decorator for message is recieved
async def handle_message(message: cl.Message): # handle message event
    prompt = message.content

    response = model.generate_content(prompt) # generate response using Gemini model

    response_text = response.text if hasattr(response, "text") else "" # get response text

    await cl.Message(content=response_text).send() # send response to user