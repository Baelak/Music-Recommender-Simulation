from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Read a CSV file of songs and return a list of dicts with typed numeric fields."""
    import csv
    float_fields = {'energy', 'tempo_bpm', 'valence', 'danceability', 'acousticness'}
    songs = []
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            for field in float_fields:
                row[field] = float(row[field])
            songs.append(dict(row))
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score a song against user preferences and return a (score, reasons) tuple."""
    score = 0.0
    reasons = []

    # 1. Categorical matching
    if song.get('genre') == user_prefs.get('genre'):
        score += 2.0
        reasons.append(f"genre match (+2.0)")

    if song.get('mood') == user_prefs.get('mood'):
        score += 1.0
        reasons.append(f"mood match (+1.0)")

    # 2. Numeric feature similarity: 1 - abs(song_value - target) / max_range
    numeric_features = {
        'energy':       1.0,
        'tempo_bpm':    200.0,
        'valence':      1.0,
        'danceability': 1.0,
        'acousticness': 1.0,
    }

    for feature, max_range in numeric_features.items():
        if feature not in user_prefs:
            continue
        similarity = 1.0 - abs(song[feature] - user_prefs[feature]) / max_range
        score += similarity
        reasons.append(f"{feature} similarity ({similarity:.2f})")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Score all songs, rank them, and return the top k as (song, score, explanation) tuples."""
    scored = [
        (song, *score_song(user_prefs, song))
        for song in songs
    ]

    ranked = sorted(scored, key=lambda x: x[1], reverse=True)

    return [
        (song, score, ", ".join(reasons))
        for song, score, reasons in ranked[:k]
    ]
