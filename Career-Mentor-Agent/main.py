"""
🌟 Career Mentor Agent System
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Created by: Kashan Malik
Version: 1.0.0

An AI-powered career guidance system that helps users:
┌─────────────────────────────┐
│ 🎯 Discover career paths    │
│ 📚 Learn required skills    │
│ 💼 Find job opportunities   │
└─────────────────────────────┘
"""

import os
from dotenv import load_dotenv
from agents import Runner, OpenAIChatCompletionsModel, AsyncOpenAI
from agents.run import RunConfig
from career_agents import create_agents

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔧 Configuration
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━
load_dotenv()

external_client = AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url=os.getenv("Gemini_API_BASE_URL", "https://generativelanguage.googleapis.com/v1beta/openai/")
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    tracing_disabled=True,
)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🤖 Initialize Agents
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━
career_agent, skill_agent, job_agent = create_agents(model)

def main():
    """
    🚀 Career Mentor Interactive Session
    Run the main career guidance workflow
    """
    print("┌────────────────────────────────┐")
    print("│    Career Mentor Agent v1.0    │")
    print("└────────────────────────────────┘")
    print("👋 Welcome! I'm your AI career companion")
    print("💫 Crafted with ❤️  by Kashan Malik\n")

    interest = input("🔎 What is your career interest? ")

    print("\n🤔 Thinking about the best career field for you...")
    result1 = Runner.run_sync(career_agent, interest, run_config=config)
    field = result1.final_output.strip()
    print(f"✅ Suggested Career Field: {field}")

    print("\n🔍 Finding the most important skill for your chosen field...")
    result2 = Runner.run_sync(skill_agent, field, run_config=config)
    print(f"🎯 Recommended Skill: {result2.final_output.strip()}")

    print("\n🚀 Looking for job opportunities that match your interests...")
    result3 = Runner.run_sync(job_agent, field, run_config=config)
    print(f"💼 Suggested Job Opportunity: {result3.final_output.strip()}")

if __name__ == "__main__":
    main()