import requests
import streamlit as st
import pandas as pd
import pickle


def fatch_poster(movie_id):
    responce = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=da686772bcf6ab2c918a2cc56756388b&language=en-US'.format(movie_id))
    data = responce.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarty[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_poster = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        # fatch poster from API
        recommended_movies_poster.append(fatch_poster(movie_id))
    return recommended_movies, recommended_movies_poster


movie_dict = pickle.load(open('movies_dictonary.pkl','rb'))
movies = pd.DataFrame(movie_dict)

similarty = pickle.load(open('similarty.pkl','rb'))

st.title("Movie Recommender System")
select_movie_name = st.selectbox(
    'Select a movie:',
    movies['title'])

if st.button('Recommender'):
    recommended_movie_names, recommended_movie_posters = recommend(select_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])

