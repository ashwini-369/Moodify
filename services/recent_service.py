from flask import session

def add_to_recent(mood, playlist):
    if "recent" not in session:
        session["recent"] = []

    recent = session["recent"]
    entry = {"mood": mood, "playlist": playlist}

    if entry in recent:
        recent.remove(entry)

    recent.insert(0, entry)
    session["recent"] = recent[:3]
