import os
from dotenv import load_dotenv
from agents import Agent, InputGuardrail, AsyncOpenAI, GuardrailFunctionOutput, Runner, OpenAIChatCompletionsModel, RunConfig
from pydantic import BaseModel
import asyncio

# Load environment variables from .env file
load_dotenv()
# Set up the LLM
gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY environment variable not set.")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)


class HomeworkOutput(BaseModel):
    is_homework: bool
    reasoning: str

guardrail_agent = Agent(
    name="Guardrail check",
    instructions="Check if the user is asking about homework. Respond with 'is_homework: true' if it's related to academic homework, and 'is_homework: false' otherwise. Provide a brief reasoning.",
    output_type=HomeworkOutput,
    model=model,
)

math_tutor_agent = Agent(
    name="Math Tutor",
    handoff_description="Specialist agent for math questions",
    instructions="You provide help with math problems. Explain your reasoning at each step and include examples",
    model=model,
)

history_tutor_agent = Agent(
    name="History Tutor",
    handoff_description="Specialist agent for historical questions",
    instructions="You provide assistance with historical queries. Explain important events and context clearly.",
    model=model,
)

science_tutor_agent = Agent(
    name="Science Tutor",
    handoff_description="Specialist agent for science questions",
    instructions="You provide help with science problems and concepts. Explain scientific principles, theories, and experimental details clearly, using examples where appropriate.",
    model=model,
)

literature_tutor_agent = Agent(
    name="Literature Tutor",
    handoff_description="Specialist agent for literature and language arts questions",
    instructions="You provide assistance with literature, including analyzing texts, understanding literary devices, exploring themes in books or poetry, and grammar. Explain concepts clearly with textual examples when relevant.",
    model=model,
)

geography_tutor_agent = Agent(
    name="Geography Tutor",
    handoff_description="Specialist agent for geography questions",
    instructions="You provide help with geography questions. Explain geographical features, concepts like climate and cartography, and information about different regions and cultures. Use maps or spatial reasoning in your explanations where helpful.",
    model=model,
)

computer_science_tutor_agent = Agent(
    name="Computer Science Tutor",
    handoff_description="Specialist agent for computer science questions",
    instructions="You provide help with computer science concepts, algorithms, data structures, and programming problems. Explain logic clearly and provide code examples or pseudocode when useful.",
    model=model,
)

general_tutor_agent = Agent(
    name="General Agents",
    handoff_description="Fallback agent for non-homework questions",
    instructions="""
You are a fallback agent that responds when the user's question does not clearly match a specific homework subject.
If the question is not related to homework, simply respond with:
“I'm only trained to help with homework! Ask me math, history, science, literature, geography, or computer science questions.”
Do not attempt to assist with unrelated questions. Do not provide general help or additional information
""",
    handoffs=[
        math_tutor_agent,
        history_tutor_agent,
        science_tutor_agent,
        literature_tutor_agent,
        geography_tutor_agent,
        computer_science_tutor_agent
    ],
    model=model,
)

async def homework_guardrail(ctx, agent, input_data):
    result = await Runner.run(guardrail_agent, input_data, context=ctx.context, run_config=config)
    final_output = result.final_output_as(HomeworkOutput)

    # Don't trip the wire anymore
    return GuardrailFunctionOutput(
        output_info=final_output,
        tripwire_triggered=False,  # <-- Always allow through
    )



triage_agent = Agent(
    name="Triage Agent",
    instructions="You determine which agent to use based on the user's homework question",
    handoffs=[history_tutor_agent,
              math_tutor_agent,
              science_tutor_agent,
              literature_tutor_agent,
              geography_tutor_agent,
              computer_science_tutor_agent,
              general_tutor_agent],
    input_guardrails=[
        InputGuardrail(guardrail_function=homework_guardrail),
    ],
    model=model
)

async def main():
    print("\n\t\tWelcome to the Homework Help Agent!")
    print("\n\t\tType your homework question, or 'exit' to quit.\n")

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["bye", "goodbye", "exit"]:
            print("\n\t\tGoodbye! Have a great day!")
            break

        try:
            result = await Runner.run(triage_agent, user_input, run_config=config)
            print(f"\nAgent: {result.final_output}")

        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")
    
    
  

if __name__ == "__main__":
    asyncio.run(main())