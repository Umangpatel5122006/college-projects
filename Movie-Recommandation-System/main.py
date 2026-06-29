# alternate way using streamlit
import streamlit as st
import pickle
import pandas as pd
import requests

movie_list = pickle.load(open('config/all_movie.pkl','rb'))
movie = pd.DataFrame(movie_list)
similarity = pickle.load(open('config/all_countries_metrics.pkl','rb'))

def fetch_poster(movie_id):
    
    
    match = movie[movie['id'] == movie_id]
    if match.empty or pd.isna(match['poster_path'].iloc[0]):
        return "https://via.placeholder.com/500x750?text=No+Image"
    return "https://image.tmdb.org/t/p/w500" + match['poster_path'].iloc[0]

def recommend(movie_name):
    movie_idx = str(movie[movie['title']==movie_name]['id'].iloc[0])

    if movie_idx not in similarity:
        st.error(f"No recommendations found for movie id {movie_idx}")
        return []
    distances = similarity[movie_idx]

    rec_movie = []
    rec_movie_posters = []
    for movie_id, score in distances:
        movie_id = int(movie_id)

        match = movie[movie['id'] == movie_id]

        if not match.empty:
            rec_movie.append(match['title'].iloc[0])
            # fetch poster from api
            rec_movie_posters.append(fetch_poster(movie_id))

    return rec_movie,rec_movie_posters
    
st.title("Movie Recommander System")

selected_movie_name = st.selectbox(
    "Which movie is you loved most",
    options=movie['title'].values,
    key="movie_select"
)

if st.button('Recommand'):
    name, posters = recommend(selected_movie_name)
    
    
    
    row1 = st.columns(5)
    row2 = st.columns(5)
    
    for i in range(min(5, len(name))):
        with row1[i]:
            st.image(posters[i])
            st.markdown(
                f"<p style='text-align:center; font-size:14px; font-weight:600; "
                f"white-space:nowrap; overflow:hidden; text-overflow:ellipsis;' "
                f"title='{name[i]}'>{name[i]}</p>",
                unsafe_allow_html=True
            )
    
    for i in range(5, min(10, len(name))):
        with row2[i - 5]:
            st.image(posters[i])
            st.markdown(
                f"<p style='text-align:center; font-size:14px; font-weight:600; "
                f"white-space:nowrap; overflow:hidden; text-overflow:ellipsis;' "
                f"title='{name[i]}'>{name[i]}</p>",
                unsafe_allow_html=True
            )

