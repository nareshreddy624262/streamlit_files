import streamlit as st
import numpy as np
import pandas as pd


st.title("working with files in streamlit ...")
st.file_uploader("upload your file here :",type = ["csv","xlsx"])

st.subheader("loading csv files in streamlit ...")
file = st.file_uploader("upload your file here ...",type = ["csv"])
f = pd.read_csv(file)
if f is not None:
    st.table(f.head())

st.subheader("working wit images in streamlit .....")
img = st.file_uploader("upload your image here .....",type = ["png","JPEG"])
if img is not None:
    st.image(img)

st.subheader("working with videos files")
video = st.file_uploader("upload your file here ....",type = ["mp4"])
if video is not None:
    st.video(video)

st.subheader("audio files ....")
audio = st.file_uploader("upload your file here..",type = ["mp3"])
if audio is not None:
    st.audio(audio)
