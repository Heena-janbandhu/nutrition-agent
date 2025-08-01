# 🧠 AI-Powered Nutrition Agent 🍽️

**Personalized Meal Planning Using IBM Granite AI**

---

## 📌 Problem Statement

> In today’s health-conscious world, individuals seek **personalized nutrition advice**, but most apps offer **generic diet plans**, ignoring lifestyle, cultural preferences, and medical history. This app aims to bridge that gap using **Generative AI**.

---

## 🎯 Objective

Create “The Smartest AI Nutrition Assistant” using **IBM Granite**, enabling:
- Personalized, one-day meal plans
- Natural language interaction (text + voice)
- Image-based input (e.g., food photos)
- Explanations for food recommendations
- Real-time feedback-driven improvement

---

## 🚀 Features

- 📝 **Text Input**: Users provide age, gender, diet, and goals
- 🎤 **Voice Input**: Speak instead of typing (Web Speech API)
- 🖼️ **Image Upload**: Upload food images (placeholder functionality)
- 🤖 **IBM Granite Integration**: Generates smart meal plans
- 💡 **Explainable AI**: Shows "Why these foods?"
- 🔁 **Feedback Loop**: Improves suggestions with real-time feedback
- 🌐 **Deployed with Render**: Live web application

---

## 🧪 Tech Stack

| Layer            | Technology Used             |
|------------------|-----------------------------|
| Frontend         | HTML, CSS, JavaScript (Voice API) |
| Backend          | Python (Flask)              |
| AI Integration   | IBM Generative AI SDK (Granite) |
| Deployment       | Render (via GitHub)         |
| Environment      | IBM Cloud Lite              |

---

## 🛠️ Setup Instructions

### 1. Clone the Repo

git clone https://github.com/Heena-janbandhu/nutrition-agent.git
cd nutrition-agent


### 2. Install Dependencies
pip install -r requirements.txt

### 3. Add API Key
Create a .env file:
GRANITE_API_KEY=your_ibm_granite_api_key_here

### 4. Run Locally
python app.py

🌍 Deployment
The app is deployed using Render and is publicly accessible.
link - https://nutrition-agent-c7ol.onrender.com/ 

IBM Granite API is used via genai SDK (v3.0.0) fulfilling the cloud requirement.

📩 Feedback Mechanism
Users can provide suggestions like:
“Add more vegetarian options” or “Include iron-rich foods”
This is fed back to the AI model for improved recommendations on next load.

🙌 Author
Heena Janbandhu
GitHub: @Heena-janbandhu

