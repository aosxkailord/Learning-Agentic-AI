"""
🌟 AI Travel Designer 🌟
-----------------------
Created with ❤️ by Kashan Malik

Your personal AI-powered travel planning assistant that brings
together a team of specialized agents to craft the perfect
travel experience! 

Features:
🤖 Advanced AI-powered conversations
🌍 Personalized travel recommendations
✈️ Flight and hotel assistance
🎨 Custom activity planning

Let's make your travel dreams come true! ✨
"""

import os
from dotenv import load_dotenv
from agents import Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig
from travel_tools import get_flight_info, get_hotel_info
from travel_agents import travel_orchestrator
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

async def main():
    """
    🚀 Launch the AI Travel Designer experience!
    
    This is where the magic happens! Our AI travel team comes together
    to help plan your perfect trip. Just chat naturally, and let our
    agents guide you through the journey of planning your dream vacation!
    
    Created by: Kashan Malik 
    With: ❤️ and advanced AI
    """
    print("""
    🌟 Welcome to Kashan Malik's AI Travel Designer! 🌟
    ------------------------------------------------
    Your personal team of AI travel experts is ready
    to help plan your perfect trip! 
    
    Type 'quit' whenever you want to end our chat.
    ------------------------------------------------
    """)

    while True:
        try:
            # Get user input
            user_message = input("\nYou: ").strip()
            
            if user_message.lower() == 'quit':
                print("\n✨ Thank you for using AI Travel Designer! Safe travels! ✨")
                break

            print("\n🤔 AI is thinking...")
            
            # Process the message through the orchestrator
            response = await Runner.run(
                starting_agent=travel_orchestrator,
                input=user_message,
                run_config=config
            )

            # Print the agent's response
            print("\nAI Travel Assistant:", response.final_output)

        except Exception as e:
            print(f"\n⚠️ Oops! Something went wrong: {str(e)}")
            print("Let's try that again differently!")

if __name__ == "__main__":
    asyncio.run(main())
