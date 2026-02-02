# Moodify

Moodify is a simple Flask-based web application that recommends music playlists based on the user’s mood.

This project was built as a learning project to understand Flask, basic machine learning integration.

---

##  What this project does

- Allows users to select a mood (Happy, Sad, Chill, Energetic)
- Allows users to type how they feel and get music suggestions
- Uses simple rules and a lightweight ML model to guess mood from text
- Provides music links and search using YouTube
- Stores recently played items during the session

---

## How mood detection works 

Moodify uses a **hybrid approach**:
- **Rule-based logic** to handle common or sensitive inputs safely
- **A simple machine learning model** (Logistic Regression) for longer text inputs

The ML model is trained on a small sample dataset and is meant as a **prototype**, not a production-level system.

---

##  Technologies Used

- Python
- Flask
- HTML, CSS
- TextBlob (sentiment support)
- Scikit-learn (basic ML)
- YouTube Data API
- Git & GitHub

---

## How to Run the Project

1. Clone the repository:
   ```bash
    git clone https://github.com/ashwini-369/Moodify.git
    cd Moodify

2. Create and activate a virtual environment:
    python -m venv venv
    venv\Scripts\activate

3. Install dependencies:
    pip install -r requirements.txt

4. Run the application:
    python run.py

5. Open your browser and visit:
    http://127.0.0.1:5000/

## Future Improvements
 - Improve the ML model using a larger dataset
 - Enhance UI and mobile responsiveness
 - Add user login and personalized history
 - Deploy the application to a cloud platform
 
## Author
  Ashwini
  Computer Science Engineering Student