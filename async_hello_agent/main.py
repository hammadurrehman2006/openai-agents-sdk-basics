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

async def main():
    agent = Agent(
        name="A Creative Storyteller.",
        instructions="You are a creative storyteller. You are given a prompt and you need to generate a short story.",
        model=model
    )
    title = input("Enter a title for your story: ")
    result = await Runner.run(agent, f"Tell me a story about {title}.", run_config=config)
    print(result.final_output)
   
if __name__ == "__main__":
    asyncio.run(main())
