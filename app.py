import streamlit as st
import pickle

with open('movies_list.pkl', 'rb') as fp:
    movies_list = pickle.load(fp)

with open('similarity_matrix.pkl', 'rb') as fp:
    similarity = pickle.load(fp)

movies_list2 = movies_list['title'].values


def recommend(movie):
    rec = []
    movie_index = movies_list[movies_list['title'] == movie].index[0]
    movie_list_recom = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x : x[1])[1:6]

    for i in movie_list_recom:
        movie_id = i
        # Fetch poster from API
        
        rec.append(movies_list.iloc[i[0]].title)
    return rec



st.title('Movie Recommender System')
selected_movie_name = st.selectbox(
    'How would you like to be contacted?',
    movies_list2)

if st.button('Recommend'):
    recommended_movies = recommend(movie=selected_movie_name)
    for i in recommended_movies:
        st.write(i)
