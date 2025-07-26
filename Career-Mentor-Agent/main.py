import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, function_tool
from agents.run import RunConfig
from roadmap_tool import create_roadmap
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

# 👨‍🏫 Career Agent: Your friendly mentor for career exploration!
career_agent = Agent(
    name="Career Agent",
    instructions=(
        "You are Career Agent, an expert career mentor. "
        "Guide users as they explore career paths, discover skill gaps, and build actionable roadmaps. "
        "Offer personalized, practical, and encouraging advice. "
        "Stay up-to-date with industry trends and best practices. "
        "When needed, use the 'create_roadmap' tool to craft step-by-step plans for users' career goals."
    ),
    model=model,
)

# 🛠️ Skill Agent: Specialist in crafting and explaining career roadmaps!
skill_agent = Agent(
    name="Skill Agent",
    instructions=(
        "You are Skill Agent, a specialist in sharing and explaining career roadmaps. "
        "When a user requests a career roadmap, use the 'create_roadmap' tool to generate and present a clear, actionable plan. "
        "Make sure the roadmap fits the user's goals and skill level, and provide concise explanations for each step."
    ),
    tools=[create_roadmap],
    model=model,
)

# 💼 Job Agent: Your expert for job suggestions and opportunities!
job_agent = Agent(
    name="Job Agent",
    instructions=(
        "You are Job Agent, an expert in suggesting job opportunities. "
        "Help users by recommending relevant jobs based on their skills, interests, and career goals. "
        "Share practical advice on job searching, application strategies, and industry trends. "
        "Make your suggestions personalized and actionable."
    ),
    model=model,
)

def main():
    print("🌟 Welcome to the Career Mentor Agent! 🌟")
    print("👋 Hi there! I'm your AI-powered career companion, coded with care by Kashan Malik.")
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