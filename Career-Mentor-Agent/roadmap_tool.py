"""
🛠️ Career Roadmap Generation Tool
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Created by: Kashan Malik
Version: 1.0.0

Provides structured career development paths with:
┌────────────────────┐
│ 📝 Step-by-step    │
│ 🎯 Clear goals     │
│ 📈 Progress paths  │
└────────────────────┘
"""

from agents import function_tool

@function_tool
def create_roadmap(fields: str) -> str:
    """
    📍 Generate Career Development Roadmap
    
    Args:
        fields (str): Career field to generate roadmap for
        
    Returns:
        str: Structured JSON roadmap with steps
        
    Example Output:
    ┌────────────────┐
    │ • Step 1      │
    │ • Step 2      │
    │ • Step 3      │
    └────────────────┘
    """
    maps = {     
            "Software Developer": {
                "steps": [ 
                    "💻 Master core programming languages",
                    "🏗️ Build portfolio projects",
                    "🌟 Contribute to open source",
                    "🎯 Ace technical interviews"
                ],
                "description": "Your journey to becoming a software developer! 🚀"
            },
            "Data Scientist": {
                "steps": [
                    "📊 Master statistics and data analysis.",
                    "🐍 Learn Python or R for data science.",
                    "📈 Work on machine learning projects.",
                    "📚 Build a portfolio with real-world datasets."
                ],
                "description": "A roadmap for becoming a data scientist, emphasizing statistical knowledge and practical experience."
            },
            "Graphic Designer": {
                "steps": [
                    "🎨 Learn design principles and software like Adobe Creative Suite.",
                    "🖼️ Create a portfolio showcasing your design work.",
                    "📅 Stay updated with design trends and techniques.",
                    "🤝 Network with other designers and potential clients."
                ],
                "description": "A roadmap for becoming a graphic designer, focusing on design skills and portfolio development."
            },
            "Teacher": {
                "steps": [
                    "📚 Obtain a degree in education or a specific subject area.",
                    "👩‍🏫 Gain teaching experience through internships or volunteer work.",
                    "📝 Develop classroom management and lesson planning skills.",
                    "🔍 Stay informed about educational best practices."
                ],
                "description": "A roadmap for becoming a teacher, highlighting educational qualifications and teaching skills."
            }
    }
    return maps.get(goal, {}).get(steps, "✨ Let's explore a different path! No suggestions for this combination yet.")

