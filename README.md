# Deep Learning Movie Recommendation System

## Overview

Built a Movie Recommendation System using Neural Collaborative Filtering (NCF) on the MovieLens 100K dataset.

## Features

* User and Movie Embeddings
* Neural Collaborative Filtering
* Rating Prediction
* Top-N Movie Recommendations
* TensorFlow/Keras Implementation

## Dataset

MovieLens 100K

* 100,000 ratings
* 943 users
* 1,682 movies

## Architecture

User ID → Embedding(32)

Movie ID → Embedding(32)

Concatenate

Dense(128)

Dense(64)

Output Rating

## Results

* Validation MAE: ~0.75
* Successfully generated personalized movie recommendations.

## Technologies

* Python
* TensorFlow/Keras
* Pandas
* NumPy
* Scikit-Learn
* Google Colab
