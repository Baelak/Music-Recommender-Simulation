"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


USERS = {
    "Late-Night Coder": {
        "genre": "lofi", "mood": "chill",
        "energy": 0.4, "tempo_bpm": 75, "acousticness": 0.8,
    },
    "Workout Warrior": {
        "genre": "rock", "mood": "intense",
        "energy": 0.95, "tempo_bpm": 150, "danceability": 0.7,
    },
    "Sunday Morning": {
        "genre": "pop", "mood": "happy",
        "energy": 0.6, "valence": 0.85, "acousticness": 0.5,
    },
}


def main() -> None:
    songs = load_songs("data/songs.csv")

    for username, user_prefs in USERS.items():
        recommendations = recommend_songs(user_prefs, songs, k=5)

        print("\n" + "=" * 40)
        print(f"  {username}")
        print("=" * 40)
        for i, (song, score, explanation) in enumerate(recommendations, start=1):
            print(f"\n#{i}  {song['title']} by {song['artist']}")
            print(f"    Score : {score:.2f} / 8.00")
            print(f"    Why   : {explanation}")
        print("\n" + "=" * 40)


if __name__ == "__main__":
    main()
