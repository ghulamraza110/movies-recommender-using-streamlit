import os
import streamlit as st
import pickle
import pandas as pd
import requests


# 🔐 Load TMDB API key from Hugging Face secrets
api_key = st.secrets["TMDB_API_KEY"]

# 📥 Download required files from Hugging Face Hub
def download_file(remote_url, destination_path):
    if not os.path.exists(destination_path):
        with st.spinner(f"Downloading {destination_path}..."):
            response = requests.get(remote_url)
            if response.status_code == 200:
                with open(destination_path, "wb") as f:
                    f.write(response.content)
            else:
                st.error(f"Failed to download {destination_path}. Status code: {response.status_code}")

file_map = {
    "similarity.pkl": "https://huggingface.co/datasets/graza/movie-recommender-files/resolve/main/similarity.pkl",
    "movie_dict.pkl": "https://huggingface.co/datasets/graza/movie-recommender-files/resolve/main/movie_dict.pkl",
    "movies.pkl": "https://huggingface.co/datasets/graza/movie-recommender-files/resolve/main/movies.pkl"
}

for target_file, source_url in file_map.items():
    download_file(remote_url=source_url, destination_path=target_file)


# 🎞️ Fetch poster from TMDB
def fetch_poster(movie_id):
    response = requests.get(
        f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    )
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data["poster_path"]



def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters

movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
'Choose a movie to get recommendations:',
movies['title'].values)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])
