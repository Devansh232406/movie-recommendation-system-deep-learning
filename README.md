# Deep Learning Movie Recommendation System

## Overview

This project implements a Movie Recommendation System using Neural Collaborative Filtering (NCF) on the MovieLens 100K dataset. The model learns latent user preferences and movie characteristics through embedding layers and predicts user ratings for unseen movies. Based on these predictions, the system generates personalized movie recommendations.

The project demonstrates the application of Deep Learning techniques in recommendation systems, a technology widely used by platforms such as Netflix, Amazon, YouTube, and Spotify.

---

## Problem Statement

Traditional recommendation systems struggle to capture complex relationships between users and items. This project uses Neural Collaborative Filtering to learn non-linear interactions between users and movies, resulting in more personalized recommendations.

---

## Dataset

### MovieLens 100K Dataset

* 100,000 ratings
* 943 users
* 1,682 movies
* Ratings ranging from 1 to 5

Dataset Source: GroupLens Research

---

## Model Architecture

The recommendation model uses Neural Collaborative Filtering with trainable embeddings.

User ID → Embedding Layer (32)

Movie ID → Embedding Layer (32)

Concatenation Layer

Dense Layer (128 neurons, ReLU)

Dense Layer (64 neurons, ReLU)

Output Layer (Predicted Rating)

This architecture enables the model to learn meaningful latent representations of users and movies while capturing complex interaction patterns.

---

## Features

* User Embedding Learning
* Movie Embedding Learning
* Neural Collaborative Filtering (NCF)
* Personalized Rating Prediction
* Top-N Movie Recommendations
* Deep Learning-based Recommendation Engine
* TensorFlow/Keras Implementation

---

## Results

* Validation MAE: ~0.75
* Successfully learned user-movie interaction patterns
* Generated personalized movie recommendations based on predicted ratings

---

## Technologies Used

* Python
* TensorFlow / Keras
* Pandas
* NumPy
* Scikit-Learn
* Google Colab
* Matplotlib

---

## Project Structure

```text
movie-recommendation-system/
│
├── data/
├── notebooks/
├── models/
├── outputs/
├── requirements.txt
├── README.md
└── movie_recommendation.ipynb
```

---

## How to Run

### Clone Repository

```bash
git clone <repository-link>
cd movie-recommendation-system
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Notebook

```bash
jupyter notebook
```

Open the notebook and execute all cells to train the model and generate recommendations.

---

## Sample Recommendation Output

Example:

User ID: 25

Recommended Movies:

1. Star Wars (1977)
2. Raiders of the Lost Ark (1981)
3. Empire Strikes Back (1980)
4. Terminator 2 (1991)
5. Back to the Future (1985)

---

## Future Improvements

* Hybrid Recommendation System
* Content-Based Filtering Integration
* Implicit Feedback Learning
* Deployment using Streamlit
* Real-Time User Recommendation Interface

---

## Author

Devansh Joshi

Machine Learning & Deep Learning Enthusiast

