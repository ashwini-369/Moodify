from flask import Blueprint, render_template, request, session
import random, requests

from .services.playlist_data import mood_playlists
from .services.recent_service import add_to_recent
from .services.mood_service import detect_mood_from_text
from .utils.time_vibe import get_time_vibe
from .config import YOUTUBE_API_KEY

main = Blueprint("main", __name__)

@main.route("/")
def index():
    vibe = get_time_vibe()
    recent = session.get("recent", [])
    suggestion = mood_playlists[vibe][0]
    return render_template("index.html", recent=recent, suggestion=suggestion, vibe=vibe)

@main.route("/recommend", methods=["POST"])
def recommend():
    mood = request.form.get("mood")
    playlists = mood_playlists.get(mood, [])
    if playlists:
        add_to_recent(mood, playlists[0][0])
    return render_template("result.html", mood=mood, playlists=playlists)

@main.route("/surprise", methods=["POST"])
def surprise():
    mood = random.choice(list(mood_playlists.keys()))
    playlists = mood_playlists[mood]
    add_to_recent(mood, playlists[0][0])
    return render_template("result.html", mood=mood, playlists=playlists)

@main.route("/detect_mood", methods=["POST"])
def detect_mood():
    text = request.form.get("feeling", "")
    mood, playlists, message = detect_mood_from_text(text)
    return render_template("result.html", mood=mood, playlists=playlists, message=message)

@main.route("/search")
def search():
    query = request.args.get("q", "").strip()
    if not query:
        return render_template("search_results.html", query=query, results=[])

    url = (
        "https://www.googleapis.com/youtube/v3/search"
        f"?part=snippet&maxResults=8&q={query}&key={YOUTUBE_API_KEY}&type=video"
    )

    data = requests.get(url).json()
    results = []

    for item in data.get("items", []):
        vid = item["id"]["videoId"]
        results.append({
            "title": item["snippet"]["title"],
            "thumbnail": item["snippet"]["thumbnails"]["high"]["url"],
            "embed_url": f"https://www.youtube.com/embed/{vid}"
        })

    return render_template("search_results.html", query=query, results=results)
