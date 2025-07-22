import streamlit as st
import pandas as pd
import pickle
import requests

st.markdown("""
    <style>
        body {
            background: linear-gradient(to right, #00BFFF #007FFF);
            color: white;
        }
        .stApp {
            background: linear-gradient(to right, #00BFFF, #007FFF);
        }
    </style>
""", unsafe_allow_html=True)



similarity=pickle.load(open('similarity.pkl','rb'))
movie_list=pickle.load(open('movies.pkl','rb'))
movie_list_searchbar=movie_list['title'].values
movies=pd.DataFrame(movie_list)
st.title("MovieOrbit")
selection= st.selectbox(
    "Enter your favourite Movie:",
    movie_list_searchbar,
)


def movie_poster_fetch(id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=eabdde02d473a1de0ef654ec4a610d37'
                          .format(id))
    data = response.json()
    return  'https://image.tmdb.org/t/p/w500/' + data['poster_path']

def recommend(movie):
    rec_list=[]
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:13]
    rec_movie_poster=[]
    for i in movie_list:
        movie_id=movies.iloc[i[0]].id

        rec_list.append(movies.iloc[i[0]].title)
        rec_movie_poster.append(movie_poster_fetch(movie_id))
    return rec_list,rec_movie_poster

if st.button("Recommend",type="secondary"):
    st.write("You selected:", selection)
    names,posters=recommend(selection)
    for i in range(0, len(names), 4):
     cols = st.columns(4)
     for j in range(4):
        if i + j < len(names):
            with cols[j]:
                st.image(posters[i + j])
                st.text(names[i + j])