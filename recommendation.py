import pandas as pd

# Load movie dataset
movies = pd.read_csv("movies.csv")

def recommend_movies(movie_name):
    # Check if movie exists
    if movie_name not in movies["title"].values:
        return ["Movie not found"]

    # Get selected movie genre
    genre = movies[movies["title"] == movie_name]["genre"].values[0]

    # Recommend movies with the same genre
    recommended = movies[movies["genre"] == genre]["title"].tolist()

    # Remove selected movie
    recommended.remove(movie_name)

    # Return top 5 recommendations
    return recommended[:5]