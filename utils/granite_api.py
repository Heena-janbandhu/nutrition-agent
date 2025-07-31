import os
from dotenv import load_dotenv
from genai import Client, Credentials

load_dotenv()
API_KEY = os.getenv("GRANITE_API_KEY")

# Initialize IBM Granite client with credentials
creds = Credentials(api_key=API_KEY)
client = Client(credentials=creds)

def get_meal_plan(user_data, feedback=""):
    # Build the dynamic prompt
    prompt = f"""
    Generate a personalized one-day meal plan for a {user_data['age']}-year-old {user_data['gender']} 
    who wants to achieve the goal of {user_data['goal']} and follows a {user_data['diet']} diet. 
    Include Breakfast, Lunch, Dinner, and a short explanation for your choices.
    """

    if feedback:
        prompt += f"\n\nUser Feedback on Previous Plan: \"{feedback}\". Please adjust and improve based on this."

    try:
        # Call IBM Granite model
        response = client.text.generation.create(
            model_id="granite-13b-chat",
            inputs=[prompt],
            parameters={
                "decoding_method": "greedy",
                "max_new_tokens": 300
            }
        )

        # Collect all output chunks
        result_text = ""
        for result in response:
            result_text += result.generated_text

        return {
            "breakfast": extract_section(result_text, "breakfast"),
            "lunch": extract_section(result_text, "lunch"),
            "dinner": extract_section(result_text, "dinner"),
            "explanation": extract_section(result_text, "explanation")
        }

    except Exception as e:
        return {
            "breakfast": "Error: Could not fetch meal plan.",
            "lunch": "",
            "dinner": "",
            "explanation": str(e)
        }

def extract_section(text, keyword):
    # Find line matching keyword (case-insensitive)
    for line in text.split('\n'):
        if keyword.lower() in line.lower():
            return line.strip()
    return f"{keyword.capitalize()} not found."
