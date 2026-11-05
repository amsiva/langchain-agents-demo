# from langchain.agents import create_agent
# from langchain_openrouter import ChatOpenRouter
# from langgraph.checkpoint.memory import InMemorySaver
# from dotenv import load_dotenv
# load_dotenv()
# import os 


# llm = ChatOpenRouter(
#      model = "openai/gpt-4o-mini",
#      temperature=0.7
# )

# response = llm.invoke("What is the distance between Earth and the Moon?")
# print(response.content)


# # agent = create_agent(
# #     model = llm,
# #     system_prompt= """
# #     You are an AI assistant who answers queries with a bit of humor. Use EMojis to decorate your response. Be polite

# #     """,
# #     checkpointer=InMemorySaver()
# # )



# # while True:

# #     user_input = input("You : ")
# #     if user_input.lower()=='exit':
# #         break

# #     response = agent.invoke(
# #         {
# #             "messages":[{"role":"user","content":user_input}]
# #         },
# #         config={"configurable":{"thread_id":1}}

# #     )

# #     print(response["messages"][-1].content)

import os
from dotenv import load_dotenv
from langchain_openrouter import ChatOpenRouter

# Load environment variables from .env
load_dotenv()

# The class automatically looks for the OPENROUTER_API_KEY env variable
llm = ChatOpenRouter(
    model="meta-llama/llama-3-8b-instruct:free",
    temperature=0.7
)

response = llm.invoke("What is the distance between Earth and the Moon?")
print(response.content)