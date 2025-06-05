import streamlit as st
import pandas as pd
import pickle
#import numpy as np
import os
import time

#from recommendationSystem.pipeline.predict import return_data
from recommendationSystem.utils.common import recommend,find_anime
from predict_trial import return_data
 
@st.cache_resource
def Recommendation_System():
    with st.spinner("Started training the model...",show_time=True):
        time.sleep(5)
        data_path, matrix_path = return_data().predict()
        #os.system("python main.py")             #remove the comment if docker file is not used
        return data_path,matrix_path
    st.success("Deployment complete, Successfully created the system!")


st.title("Anime Recommender System")



data_path, matrix_path = Recommendation_System()

anime_data = pd.read_csv(data_path)
similarity_matrix = pickle.load(open(file=matrix_path,mode='rb'))

select_anime_name = st.selectbox(
    "Choose Anime Name : ",
    anime_data['title'].values,
    index=None,
    placeholder="Select the anime for recommendation..."
)

if select_anime_name is not None:
    if st.button("Recommend",use_container_width=True):
        st.write('')
        st.write('')
        st.write('')

        name, posters, link, score = recommend(data=anime_data,matrix=similarity_matrix,anime=select_anime_name)


        _, col, _ = st.columns(3)

        with col:
            st.image(posters[0])
        #st.write(name[0])
        st.text(f"{find_anime(select_anime_name)}")
        st.write(f'Similarity Score : {score[0]}')
        st.write('')
        st.link_button("Know More", link[0],use_container_width=True)

        col1, col2, col3 = st.columns(3)

        with col1:
            st.image(posters[1])
            st.write(name[1])
            st.write(f'Similarity Score : {score[1]}')
            st.write('')
            st.link_button("Know More", link[1],use_container_width=True)

        with col2:
            st.image(posters[2])
            st.write(name[2])
            st.write(f'Similarity Score : {score[2]}')
            st.write('')
            st.link_button("Know More", link[2],use_container_width=True)

        with col3:
            st.image(posters[3])
            st.write(name[3])
            st.write(f'Similarity Score : {score[3]}')
            st.write('')
            st.link_button("Know More", link[3],use_container_width=True)

        st.write('')
        st.write('')
        st.write('')

        col4, col5, col6 = st.columns(3)

        with col4:
            st.image(posters[4])
            st.write(name[4])
            st.write(f'Similarity Score : {score[4]}')
            st.write('')
            st.link_button("Know More", link[4],use_container_width=True)

        with col5:
            st.image(posters[5])
            st.write(name[5])
            st.write(f'Similarity Score : {score[5]}')
            st.write('')
            st.link_button("Know More", link[5],use_container_width=True)

        with col6:
            st.image(posters[6])
            st.write(name[6])
            st.write(f'Similarity Score : {score[6]}')
            st.write('')
            st.link_button("Know More", link[6],use_container_width=True)

        st.write('')
        st.write('')
        st.write('')

        col7, col8, col9 = st.columns(3)

        with col7:
            st.image(posters[7])
            st.write(name[7])
            st.write(f'Similarity Score : {score[7]}')
            st.write('')
            st.link_button("Know More", link[7],use_container_width=True)

        with col8:
            st.image(posters[8])
            st.write(name[8])
            st.write(f'Similarity Score : {score[8]}')
            st.write('')
            st.link_button("Know More", link[8],use_container_width=True)

        with col9:
            st.image(posters[9])
            st.write(name[9])
            st.write(f'Similarity Score : {score[9]}')
            st.write('')
            st.link_button("Know More", link[9],use_container_width=True)