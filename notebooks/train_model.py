import os
import pickle
import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from keras.layers import Concatenate, Dense, Embedding, Flatten, Input
from keras.models import Model

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

ratings = pd.read_csv("ml/data/ratings.csv")


with open("ml/encoders/user_encoder.pkl", "rb") as f:
    user_encoder = pickle.load(f)

with open("ml/encoders/movie_encoder.pkl", "rb") as f:
    movie_encoder = pickle.load(f)

X_user = user_encoder.transform(ratings["user_id"].values)
X_movie = movie_encoder.transform(ratings["movie_id"].values)
y = ratings["rating"].values

X_user_train, X_user_test, X_movie_train, X_movie_test, y_train, y_test = train_test_split(
    X_user,
    X_movie,
    y,
    test_size=0.2,
    random_state=42,
)

user_input = Input(shape=(1,))
movie_input = Input(shape=(1,))

user_embedding = Embedding(
    input_dim=len(user_encoder.classes_) + 1,
    output_dim=32,
)(user_input)

movie_embedding = Embedding(
    input_dim=len(movie_encoder.classes_) + 1,
    output_dim=32,
)(movie_input)

user_vec = Flatten()(user_embedding)
movie_vec = Flatten()(movie_embedding)

x = Concatenate()([user_vec, movie_vec])
x = Dense(128, activation="relu")(x)
x = Dense(64, activation="relu")(x)
output = Dense(1)(x)

model = Model(inputs=[user_input, movie_input], outputs=output)
model.compile(optimizer="adam", loss="mse", metrics=["mae"])

history = model.fit(
    [X_user_train, X_movie_train],
    y_train,
    validation_split=0.1,
    epochs=10,
    batch_size=256,
    verbose=0,
)

test_loss, test_mae = model.evaluate(
    [X_user_test, X_movie_test],
    y_test,
    verbose=0
)

print(f"Test MAE: {test_mae:.4f}")

os.makedirs("ml/models", exist_ok=True)
model.save("ml/models/movie_recommender.keras")
print("trained")
