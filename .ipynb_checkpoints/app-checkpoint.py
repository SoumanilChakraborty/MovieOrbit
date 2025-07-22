import streamlit as st
import pandas as pd
import pickle

similarity=pickle.load(open('similarity.pkl','rb'))
movie_list=pickle.load(open('movies.pkl','rb'))
movie_list_searchbar=movie_list['title'].values
movies=pd.DataFrame(movie_list)
st.title("MovieOrbit")
selection= st.selectbox(
    "Enter your favourite Movie:",
    movie_list_searchbar,
)

def movie_poster_fetch(movie_id):
    


def recommend(movie):
    rec_list=[]
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]
    for i in movie_list:
        movie_id=i[0]

        rec_list.append(movies.iloc[i[0]].title)
    return rec_list

if st.button("Recommend",type="secondary"):
    st.write("You selected:", selection)
    recommendations=recommend(selection)
    for i in recommendations:
        st.write(i)

