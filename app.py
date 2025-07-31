import os
from flask import Flask, render_template, request, url_for
from werkzeug.utils import secure_filename
from utils.granite_api import get_meal_plan

# App configuration
UPLOAD_FOLDER = 'static/uploads'
app = Flask(__name__, static_url_path='/static')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/form')
def form():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    user_data = {
        "age": request.form['age'],
        "gender": request.form['gender'],
        "goal": request.form['goal'],
        "diet": request.form['diet']
    }

    # Handle uploaded image
    image = request.files.get('food_image')
    image_filename = None
    if image and image.filename != '':
        image_filename = secure_filename(image.filename)
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], image_filename))

    # Handle feedback from previous response (if present)
    feedback_text = request.form.get("feedback", "").strip()

    # Get meal plan using Granite with optional feedback
    meal_plan = get_meal_plan(user_data, feedback=feedback_text)

    return render_template(
        'result.html',
        meal_plan=meal_plan,
        image_filename=image_filename
    )

# Optional route to handle feedback POST separately (if using JS/AJAX)
@app.route('/feedback', methods=['POST'])
def feedback():
    return render_template('index.html')  # Or redirect with pre-filled values

if __name__ == '__main__':
    app.run(debug=True)
