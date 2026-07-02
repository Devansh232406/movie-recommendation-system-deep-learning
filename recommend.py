import pickle
import numpy as np
import pandas as pd
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
import tensorflow as tf
from keras.models import load_model

# Load model
model = load_model(
    "models/ncf_model.h5",
    compile=False
)

# Load encoders
with open("encoders/user_encoder.pkl", "rb") as f:
    user_encoder = pickle.load(f)

with open("encoders/movie_encoder.pkl", "rb") as f:
    movie_encoder = pickle.load(f)

# Load data
movies = pd.read_csv("data/movies.csv")
ratings = pd.read_csv("data/ratings.csv")

# User input
user_id = int(input("Enter User ID: "))

# Check user exists
if user_id not in user_encoder.classes_:
    print("User not found.")
    exit()

# Encode user
encoded_user = user_encoder.transform([user_id])[0]

# Movies already watched
watched_movies = ratings[
    ratings["user_id"] == user_id
]["movie_id"].values

# Candidate movies
all_movies = movies["movie_id"].unique()

candidate_movies = [
    movie
    for movie in all_movies
    if movie not in watched_movies
]

# Encode movies
encoded_movies = movie_encoder.transform(candidate_movies)

# Create prediction arrays
user_array = np.full(
    len(encoded_movies),
    encoded_user
)

# Predict ratings
predictions = model.predict(
    [user_array, encoded_movies],
    verbose=0
).flatten()

# Top recommendations
top_indices = predictions.argsort()[-10:][::-1]

top_movie_ids = np.array(candidate_movies)[top_indices]

print("\nTop 10 Recommendations:\n")

for i, movie_id in enumerate(top_movie_ids, start=1):

    title = movies.loc[
        movies["movie_id"] == movie_id,
        "title"
    ].values[0]

    print(f"{i}. {title}")
