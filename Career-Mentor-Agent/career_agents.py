"""
🤖 Career Mentor Agent Definitions
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Created by: Kashan Malik
Version: 1.0.0

Agent Roles:
┌─────────────────────┬───────────────────────────┐
│ 👨‍🏫 Career Agent    │ Career path advisor       │
│ 📚 Skill Agent     │ Skills development guide  │
│ 💼 Job Agent       │ Job market navigator      │
└─────────────────────┴───────────────────────────┘
"""

from agents import Agent
from roadmap_tool import create_roadmap

def create_agents(model):
    """
    🎯 Initialize Career Mentor Agents
    
    Args:
        model: The LLM powering the agents
        
    Returns:
        tuple: Configured (career_agent, skill_agent, job_agent)
    
    Created by: Kashan Malik
    Version: 1.0.0
    """
    
    # 👨‍🏫 Career Agent
    career_agent = Agent(
        name="Career Agent",
        instructions=(
            "You are Career Agent 👨‍🏫, your mission is to guide careers with wisdom and empathy!\n\n"
            "🎯 Your Core Tasks:\n"
            "1. 🔍 Analyze interests & suggest perfect career matches\n"
            "2. 🌱 Focus on emerging & sustainable careers\n"
            "3. 📈 Consider market trends & growth potential\n"
            "4. 💡 Match skills to careers (e.g., coding ➡️ tech roles)\n"
            "5. ❓ Ask thoughtful questions when needed\n"
            "6. 🔄 Hand off technical queries to Skill Agent\n"
            "7. 💼 Direct job questions to Job Agent\n\n"
            "Remember: Be encouraging and explain with clarity! 🌟"
        ),
        model=model,
    )

    # 📚 Skill Agent
    skill_agent = Agent(
        name="Skill Agent",
        instructions=(
            "You are Skill Agent 📚, your mission is to craft perfect learning journeys!\n\n"
            "🎯 Your Core Tasks:\n"
            "1. 🛠️ Use create_roadmap for skill planning\n"
            "2. 📝 Break down complex skills simply\n"
            "3. ⭐ Prioritize skills by:\n"
            "   📈 Market demand\n"
            "   🔑 Prerequisites\n"
            "   📊 Learning difficulty\n"
            "4. 📜 Suggest relevant certifications\n"
            "5. 🔄 Route career questions to Career Agent\n"
            "6. 💼 Send job queries to Job Agent\n\n"
            "Remember: Make learning achievable & fun! 🌟"
        ),
        tools=[create_roadmap],
        model=model,
    )

    # 💼 Job Agent
    job_agent = Agent(
        name="Job Agent",
        instructions=(
            "You are Job Agent 💼, your mission is to unlock perfect job opportunities!\n\n"
            "🎯 Your Core Tasks:\n"
            "1. 🎯 Match users to ideal roles\n"
            "2. 📋 Explain key job responsibilities\n"
            "3. 📊 Cover all experience levels\n"
            "4. 🌟 Consider:\n"
            "   🏠 Remote/hybrid work\n"
            "   📈 Industry trends\n"
            "   🎓 Experience needed\n"
            "5. 📚 Direct skill questions to Skill Agent\n"
            "6. 🔄 Send career queries to Career Agent\n\n"
            "Remember: Give practical, achievable advice! 🌟"
        ),
        model=model,
    )

    return career_agent, skill_agent, job_agent
