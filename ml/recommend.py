import os
import pickle
import numpy as np
import pandas as pd
import tensorflow as tf
from keras.models import load_model

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"


# =========================
# Load Model
# =========================

model = load_model(
    "ml/models/movie_recommender.keras",
    compile=False
)


# =========================
# Load Encoders
# =========================

with open("ml/encoders/user_encoder.pkl", "rb") as f:
    user_encoder = pickle.load(f)

with open("ml/encoders/movie_encoder.pkl", "rb") as f:
    movie_encoder = pickle.load(f)


# =========================
# Load Data
# =========================

movies = pd.read_csv("ml/data/movies.csv")
ratings = pd.read_csv("ml/data/ratings.csv")


# =========================
# Recommendation Function
# =========================

def recommend_movies(user_id, n=10):

    # Check user
    if user_id not in user_encoder.classes_:
        raise ValueError(f"User {user_id} not found.")

    # Encode user
    encoded_user = user_encoder.transform([user_id])[0]

    # Movies already watched
    watched_movies = ratings[
        ratings["user_id"] == user_id
    ]["movie_id"].values

    # All movies
    all_movies = movies["movie_id"].unique()

    # Remove watched movies
    candidate_movies = [
        movie_id
        for movie_id in all_movies
        if movie_id not in watched_movies
    ]

    # Encode candidate movies
    encoded_movies = movie_encoder.transform(candidate_movies)

    # Repeat user ID for every movie
    user_array = np.full(
        len(encoded_movies),
        encoded_user
    )

    # Predict ratings
    predictions = model.predict(
        [user_array, encoded_movies],
        verbose=0
    ).flatten()

    # Get top N
    top_indices = predictions.argsort()[-n:][::-1]

    recommendations = []

    for index in top_indices:

        movie_id = candidate_movies[index]

        movie_row = movies[
            movies["movie_id"] == movie_id
        ].iloc[0]

        recommendations.append({
            "movie_id": int(movie_id),
            "title": movie_row["title"],
            "predicted_rating": round(
                float(predictions[index]),
                2
            )
        })

    return recommendations