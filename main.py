from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app = FastAPI()

movies = [
    {
        "id": 1,
        "title": "3 Idiots",
        "director": "Rajkumar Hirani",
        "genre": "Comedy Drama",
        "language": "Hindi",
        "release_year": 2009
    },
    {
        "id": 2,
        "title": "Baahubali",
        "director": "S S Rajamouli",
        "genre": "Action Drama",
        "language": "Telugu",
        "release_year": 2015
    }
]

# Pydantic Model
class MovieUpdate(BaseModel):
    title : str
    director : str
    genre : str
    language : str
    release_year : int

@app.get('/')
def movie():
    return movies

@app.get('/movies')
def get_movies():
    return movies

@app.get('/movies/{movies_id}')
def get_movies_by_id(movies_id : int | None = None):
    if movies_id is not None:
        filter_movie = []
        for movie in movies:
            if movie["id"] == movies_id:
                filter_movie.append(movie)
        return filter_movie
    return movies

@app.put("/movies/{movie_id}")
def update_movie(movie_id: int, movie: MovieUpdate):
    for existing_movie in movies:
        if existing_movie["id"] == movie_id:
            existing_movie["title"] = movie.title
            existing_movie["director"] = movie.director
            existing_movie["genre"] = movie.genre
            existing_movie["language"] = movie.language
            existing_movie["release_year"] = movie.release_year

            return {
                "message": "Movie Updated Successfully",
                "movie": existing_movie
            }
    raise HTTPException(status_code = 404, detail = "Movie Not found")