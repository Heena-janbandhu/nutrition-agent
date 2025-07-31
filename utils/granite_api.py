import os
from dotenv import load_dotenv
from genai import Client, Credentials

load_dotenv()
API_KEY = os.getenv("GRANITE_API_KEY")

# Initialize IBM Granite client with credentials
creds = Credentials(api_key=API_KEY)
client = Client(credentials=creds)

def get_meal_plan(user_data, feedback=""):
    # Build the dynamic prompt (just for reference)
    prompt = f"""
    Generate a personalized one-day meal plan for a {user_data['age']}-year-old {user_data['gender']} 
    who wants to achieve the goal of {user_data['goal']} and follows a {user_data['diet']} diet. 
    Include Breakfast, Lunch, Dinner, and a short explanation for your choices.
    """
    if feedback:
        prompt += f"\n\nUser Feedback on Previous Plan: \"{feedback}\". Please adjust and improve based on this."

    # 🧪 MOCKED RESPONSE (to simulate working API)
    result_text = """
Breakfast: Oats with almond milk and berries
Lunch: Grilled tofu salad with quinoa
Dinner: Vegetable stir-fry with brown rice
Explanation: These meals provide a high-fiber, low-fat diet ideal for your weight loss goals while ensuring adequate protein.
"""

    return {
        "breakfast": extract_section(result_text, "breakfast"),
        "lunch": extract_section(result_text, "lunch"),
        "dinner": extract_section(result_text, "dinner"),
        "explanation": extract_section(result_text, "explanation")
    }

def extract_section(text, keyword):
    for line in text.strip().split('\n'):
        if keyword.lower() in line.lower():
            return line.strip()
    return f"{keyword.capitalize()} not found."
