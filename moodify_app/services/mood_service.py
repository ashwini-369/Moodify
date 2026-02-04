import pickle
import os

BASE_DIR = os.path.dirname(__file__)
MODEL_PATH = os.path.join(BASE_DIR, "../ml/mood_model.pkl")
VEC_PATH = os.path.join(BASE_DIR, "../ml/vectorizer.pkl")

model = pickle.load(open(MODEL_PATH, "rb"))
vectorizer = pickle.load(open(VEC_PATH, "rb"))

from textblob import TextBlob
from random import choice
from .playlist_data import mood_playlists
from .recent_service import add_to_recent

def predict_mood_ml(text):
    vec = vectorizer.transform([text])
    return model.predict(vec)[0]

def detect_mood_from_text(text):
    negative_words = [
        "sad", "exhausted", "tired", "lonely",
        "upset", "stressed", "angry", "down",
        "depressed", "crying"
    ]

    text_lower = text.lower()

    # 1️⃣ Safety-first rule-based check
    if any(word in text_lower for word in negative_words):
        mood = "chill"
        message = "Let's calm things down 🌙"

    # 2️⃣ ML-based prediction for meaningful input
    elif len(text.split()) >= 3:
        mood = predict_mood_ml(text)
        message = "Mood detected using ML 🎯"

    # 3️⃣ Safe fallback
    else:
        mood = "chill"
        message = "Using default chill vibes 🎶"

    playlist = choice(mood_playlists[mood])
    add_to_recent(mood, playlist[0])

    return mood, [playlist], message
