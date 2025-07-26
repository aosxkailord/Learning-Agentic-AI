# --- RoadMap Tool ---
# This tool is designed to help users create and manage a roadmap for their career development.
from agents import function_tool

@function_tool
def create_roadmap(fields: str) -> str:
    maps = {     
            "Software Developer": {
                "steps": [ 
                    "Learn programming languages like Python, Java, or JavaScript.",
                    "Build projects to showcase your skills.",
                    "Contribute to open source projects.",
                    "Prepare for technical interviews."
                ],
                "description": "A roadmap for becoming a software developer, focusing on essential skills and project experience."
            },
            "Data Scientist": {
                "steps": [
                    "Master statistics and data analysis.",
                    "Learn programming languages like Python or R.",
                    "Work on data visualization and machine learning projects.",
                    "Build a portfolio with real-world datasets."
                ],
                "description": "A roadmap for becoming a data scientist, emphasizing statistical knowledge and practical experience."
            },
            "Graphic Designer": {
                "steps": [
                    "Learn design principles and software like Adobe Creative Suite.",
                    "Create a portfolio showcasing your design work.",
                    "Stay updated with design trends and techniques.",
                    "Network with other designers and potential clients."
                ],
                "description": "A roadmap for becoming a graphic designer, focusing on design skills and portfolio development."
            },
            "Teacher": {
                "steps": [
                    "Obtain a degree in education or a specific subject area.",
                    "Gain teaching experience through internships or volunteer work.",
                    "Develop classroom management and lesson planning skills.",
                    "Stay informed about educational best practices."
                ],
                "description": "A roadmap for becoming a teacher, highlighting educational qualifications and teaching skills."
            }
    }
    return maps.get(goal, {}).get(steps, "No suggestions available for this goal and steps.")

