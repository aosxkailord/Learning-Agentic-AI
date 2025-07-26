import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, function_tool
from agents.run import RunConfig
from game_tools import generate_event, roll_dice


# 🌱 Load environment variables for secure API access
load_dotenv()

# 🤖 Initialize the OpenAI-compatible Gemini model client
external_client = AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url=os.getenv("Gemini_API_BASE_URL", "https://generativelanguage.googleapis.com/v1beta/openai/")
)

# 🧠 Set up the chat model for our agents
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

# ⚙️ Configure how the agents will run (tracing is off for privacy)
config = RunConfig(
    model=model,
    tracing_disabled=True,
)

# 🌟 Agents for the Game Master Experience
# Author: Kashan Malik

# 🎤 Narrator Agent: Sets the scene and tells the story
narrator_agent = Agent(
    name="Narrator Agent",
    instructions="🎙️ You are the narrator of a tabletop RPG. Describe the world, events, and characters vividly, immersing players in the adventure.",
    model=model,
)

# 👹 Monster Agent: Creates challenges and encounters
monster_agent = Agent(
    name="Monster Agent",
    instructions="👾 You are the monster in a tabletop RPG. Devise thrilling challenges and encounters for the players.",
    model=model,
    tools=[generate_event, roll_dice],
)

# 🪄 Item Agent: Generates magical items and artifacts
item_agent = Agent(
    name="Item Agent",
    instructions="🧰 You are the item agent in a tabletop RPG. Invent fascinating items and artifacts for the players to discover.",
    model=model,   
)

def main():
    """
    🚀 Main entry point for the Game Master Agent.
    Guides the player through a simple RPG scenario using AI-powered agents.
    Created with ❤️ by Kashan Malik.
    """
    print("🌟 Welcome to the Game Master Agent! 🌟")
    print("Created by Kashan Malik\n")
    choice = input("🗝️ Only the bravest dare enter the dungeon. Are you bold enough to proceed, or will you admit defeat and turn back? (yes/no): ").strip().lower()

    # 🎲 Narrator sets the scene
    result1 = Runner.run_sync(narrator_agent, choice, run_config=config)
    print(f"\n📖 Story: {result1.final_output}")

    # 👹 Monster encounter
    result2 = Runner.run_sync(monster_agent, choice, run_config=config)
    print(f"\n⚔️ Monster Encounter: {result2.final_output}")

    # 🪄 Item discovery
    result3 = Runner.run_sync(item_agent, choice, run_config=config)
    print(f"\n🎁 Item Found: {result3.final_output}")

if __name__ == "__main__":
    main()