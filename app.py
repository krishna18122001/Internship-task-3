import  pickle
import streamlit as st
import pandas as pd
import requests

def fetch_poster(movie_id):
    Url = "https://api.themoviedb.org/3/movie/{}?api_key=6e22529a13568d157199d01a27be2023&language=en-US".format(movie_id)
    data = requests.get(Url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "http://image.tmdb.org/t/p/w500/"+poster_path
    return full_path

def recommend(movie):
    movie_index = movies[movies['title']==movie].index[0]
    distance = similarity[movie_index]
    movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_poster = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_poster


movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))
st.title("Movie Recommendation System")

search_query = st.text_input('Search for a movie:', '')

# Update the movie selection based on the search query
filtered_movies = movies[movies['title'].str.lower().str.contains(search_query.lower())]


select_movie_name = st.selectbox(
    "Select a movie name from dropdown",
    filtered_movies["title"].values)

if st.button("Recommend"):
    names, posters = recommend(select_movie_name)
    FO1, FO2, FO3, FO4, FO5 = st.columns(5)
    with FO1:
        st.text(names[0])
        st.image(posters[0])
    with FO2:
        st.text(names[1])
        st.image(posters[1])
    with FO3:
        st.text(names[2])
        st.image(posters[2])
    with FO4:
        st.text(names[3])
        st.image(posters[3])
    with FO5:
        st.text(names[4])
        st.image(posters[4])