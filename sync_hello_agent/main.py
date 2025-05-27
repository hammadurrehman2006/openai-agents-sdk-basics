import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig
import asyncio

# Load environment variables
load_dotenv()
# Get API keys from environment variables
gemini_api_key = os.getenv("GEMINI_API_KEY")
#check if the api key is set
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set")

# create client for external api
external_client = AsyncOpenAI(api_key=gemini_api_key,
                            base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
                            )

# model for external api
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
    )

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
    )

# create a topic based joke generator agent
agent : Agent = Agent(
    name="Joke Generator",
    instructions="You are a joke generator. You will generate a best joke based on the topic provided by the user.",
    model=model,
)

topic = input("Enter a topic: ")
result = Runner.run_sync(agent, topic, run_config=config)
print("\n\n")
print(result.final_output)