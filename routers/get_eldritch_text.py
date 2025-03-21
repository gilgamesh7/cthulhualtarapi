from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

from config import CHATGPT_API_KEY

def get_eldritch_text(message: str) -> str:

    # Set up prompts
    horror_prompt = [
            SystemMessage(content="You are H.P. Lovecraft, crafting a chilling cosmic horror narrative."),
            HumanMessage(content=f"Describe this astronomy data as if it were an ominous revelation in 50 words. Instead of Auckland, use the name R'lyeh : {message}")
        ]
    
    # Create a ChatOpenAI object
    llm = ChatOpenAI(openai_api_key=CHATGPT_API_KEY, model_name="gpt-4")


    # Generate a response
    eldritch_text = llm.invoke(horror_prompt)
    print(eldritch_text)

    # Return the response
    return eldritch_text