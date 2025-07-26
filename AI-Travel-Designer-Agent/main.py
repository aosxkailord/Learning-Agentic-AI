import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, function_tool
from agents.run import RunConfig
from travel_tools import get_flight_info, get_hotel_info
import asyncio

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
# 🌍✨ Welcome to the AI Travel Designer Agent! ✨🌍
# -------------------------------------------------
# Crafted with ❤️ by Kashan Malik
#
# This module defines three specialized travel agents:
#   - Destination Agent: Finds flights & hotels 🛫🏨
#   - Booking Agent: Assists with bookings 📅📝
#   - Explorer Agent: Helps plan your adventures 🧭🌏
#
# Each agent uses advanced AI models to provide you with
# the best travel recommendations and arrangements.
# -------------------------------------------------

# 🧑‍💼 Define the Destination Agent: Your travel info expert!
destination_agent = Agent(
    name="Destination Agent",
    instructions="You are a travel agent specializing in providing flight and hotel information.",
    tools=[get_flight_info, get_hotel_info],
    model=model,
)

# 📝 Define the Booking Agent: Your booking assistant!
booking_agent = Agent(
    name="Booking Agent",
    instructions="You are a booking agent that can assist with travel arrangements and booking.",
    tools=[get_flight_info, get_hotel_info],
    model=model,
)

# 🧭 Define the Explorer Agent: Your adventure planner!
explorer_agent = Agent(
    name="Explorer Agent",
    instructions="You are an explorer agent that can help with travel planning and exploration.",
    tools=[get_flight_info, get_hotel_info],
    model=model,
)

async def main():
    """
    🚀 Main entry point for the AI Travel Designer Agent.
    Interacts with the user to gather travel preferences,
    then queries three specialized agents for recommendations.
    """
    print("🌟 Welcome to the AI Travel Designer Agent! 🌟")
    print("Created with ❤️ by Kashan Malik\n")
    print("Let's design your perfect trip together! ✈️🏝️\n")

    # 🎭 Gather user preferences
    mood = input("🤔 What is your mood for travel? (e.g., adventurous, relaxing, cultural): ")
    destination = input("📍 Where would you like to travel? (e.g., Paris, Tokyo): ")
    dates = input("📅 What are your travel dates? (e.g., 2023-12-01 to 2023-12-15): ")
    return_date_needed = input("🔄 Do you need a return date? (yes/no): ")

    if return_date_needed.strip().lower() == 'yes':
        return_date = input("📆 Please provide your return date (YYYY-MM-DD): ")
    else:
        return_date = None

    print("\n🔎 Processing your travel request... Please wait! 🚦\n")

    # 🌈✨ Prepare user input for the agents with all your travel vibes!
    user_input = {
        "mood": mood,                # 😃 User's travel mood (adventurous, relaxing, etc.)
        "destination": destination,  # 📍 Desired travel destination
        "dates": dates,              # 📅 Travel dates
        "return_date": return_date   # 🔄 Return date (if needed)
    }
    """
    🧳 user_input structure:
    [
        "mood": str,          # e.g., "adventurous"
        "destination": str,   # e.g., "Paris"
        "dates": str,         # e.g., "2023-12-01 to 2023-12-15"
        "return_date": str    # e.g., "2023-12-15" or None
    ]
    This dictionary is sent to each agent for personalized recommendations! 🌟
    """

    # 🛫 Get recommendations from the Destination Agent
    result1 = await Runner.run(
        destination_agent,
        [user_input],
        run_config=config
    )
    print("🗺️ Destination Agent Result:\n", result1.final_output, "\n")

    # 📝 Get booking assistance from the Booking Agent
    result2 = await Runner.run(
        booking_agent,
        [user_input],
        run_config=config
    )
    print("📑 Booking Agent Result:\n", result2.final_output, "\n")

    # 🧭 Get exploration ideas from the Explorer Agent
    result3 = await Runner.run(
        explorer_agent,
        [user_input],
        run_config=config
    )
    print("🌄 Explorer Agent Result:\n", result3.final_output, "\n")

    print("🎉 Thank you for using the AI Travel Designer Agent! Safe travels! 🌏✨")

if __name__ == "__main__":
    asyncio.run(main())
