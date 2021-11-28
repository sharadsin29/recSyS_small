# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 01:14:57 2021

@author: SHARAD
"""

import json
import numpy as np
from numpy import load
import pandas as pd
import pickle
import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie
from annotated_text import annotated_text as at
import random
import colorsys
import os
import base64

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

lottie_loading = load_lottiefile("movie2.json")
img = Image.open('nn.png')
st.set_page_config(page_title="New Netflix", page_icon=img,layout="wide",initial_sidebar_state="expanded")


hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        h1 {color: #E50914;}
        img {width: auto;margin: auto;display: block;}
        </style>
        <a><img src="https://fontmeme.com/permalink/211116/9f7bb909884a58264f63170a745337d2.png" alt="bebas-neue-font" border="0"></a>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
col1,col2=st.columns(2)

col1.write(""" 
         # Why New Netflix?  
         - #### Let's be honest, Netflix is a streaming service. Their priorities aren't to recommend the best movie, instead they are biased towards promoting their own Netflix Originals and hence aren't the best recommendation engine out there.
         - #### Don't worry we are here to help!!!
         - #### Pick a movie from the sidebar and we will give you an unbiased recommendation
         """)


with col2:
    st_lottie(
    lottie_loading,
    speed=1,
    reverse=False,
    loop=True,
    quality="low", # medium ; high
    renderer="svg", # canvas
    height=None,
    width=None,
    key=None,
)



with open("movies_list_small.txt", "rb") as fp:
    movies_list = pickle.load(fp)


movie_name=st.sidebar.selectbox("Select Movie",movies_list,index=1)
nor = st.sidebar.slider("No. of Recommendations",1,20)

mv_list= pd.read_csv('mv_list_small.csv',header=None)
dict_corr_mat=load('corr_mat_small.npz')
corr_mat = dict_corr_mat['arr_0']

movie =movies_list.index(movie_name)


corr_movie=corr_mat[movie]

st.write("If you like "+movie_name+ " then you'd also like the following:")

movie_rec=[]
rr = np.arange(0.2, 1.0, 0.01)
rr[::-1].sort()

for i in rr:
    rec=list(mv_list[(corr_movie<1.0)&(corr_movie>i)][0])
    for j in rec:
        if((j!=movie_name) and (j not in movie_rec) and (len(movie_rec)<nor)):
            movie_rec.append(j)


mv_csv=pd.read_csv('movies.csv')
links_csv=pd.read_csv('links.csv')
imdb_link="https://www.imdb.com/title/tt"
tmdb_link="https://www.themoviedb.org/movie/"

@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

@st.cache(allow_output_mutation=True)
def get_img_with_href(local_img_path, target_url):
    img_format = os.path.splitext(local_img_path)[-1].replace('.', '')
    bin_str = get_base64_of_bin_file(local_img_path)
    html_code = f'''
        <a href="{target_url}" target="_blank">
            <img src="data:image/{img_format};base64,{bin_str}" />
        </a>'''
    return html_code




for k in movie_rec:
    movie_id=mv_csv[mv_csv['title']==k]['movieId'].astype(int).iloc[0]
    genres=mv_csv[mv_csv['title']==k]['genres']
    imdb_id=int(links_csv[links_csv['movieId']==movie_id]['imdbId'])
    paddingZ=str(imdb_id).rjust(7, '0')
    tmdb_id=int(links_csv[links_csv['movieId']==movie_id]['tmdbId'])
    f_imdb=imdb_link+paddingZ
    f_tmdb=tmdb_link+str(tmdb_id)
    h,s,l = random.random(), 0.5 + random.random()/2.0, 0.4 + random.random()/5.0
    r,g,b = [int(256*i) for i in colorsys.hls_to_rgb(h,l,s)]
    qq="rgb("+str(r)+","+str(g)+","+str(b)+")"
    c1,c2=st.columns(2)
    with c1:
        if(k=='Untitled Spider-Man Reboot (2017)'):
            k='Spider-Man: Homecoming (2017)'
        at((k,genres ,qq, ))

    imdb_html = get_img_with_href('imdb (1).png', f_imdb)
    c2.markdown(imdb_html, unsafe_allow_html=True)
    st.write("")
    
    
    
    

