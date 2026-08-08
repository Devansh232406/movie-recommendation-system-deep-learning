from fastapi import FastAPI, HTTPException
from ml.recommend import recommend_movies
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title  = "Movie Recommendation API",
    description = "Neural Collaborative Filtering Movie Recommendation API",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:5174",
        "http://127.0.0.1:5174",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def root():

    return {"message": "Welcome to the Cine API!"}

@app.get("/recommendations/{user_id}")
def get_recommendations(user_id: int):

    try:
        recommendations = recommend_movies(
            user_id = user_id,
            n = 10
        )
        return {
            "user_id" : user_id,
            "recommendations": recommendations
        }
    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )