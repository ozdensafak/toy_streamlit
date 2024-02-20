import streamlit as st
import pandas as pd

poets = st.sidebar.radio("Who is your favourite poet?",
                 ["***Bukowski***", ":rainbow[Prevert]", "Data Scientist"],
                 captions=["They think I am macho, I am not!", 
                           "They think I am a covard, I am not!",
                           "Boooooring!"])

if poets == "***Bukowski***":
    st.subheader("A poem by Charles Bukowski")
    video_path = "https://www.youtube.com/watch?v=mw8DlHFCKC8"
    st.video(video_path)

elif poets == ":rainbow[Prevert]":
    st.subheader("I am a proud anarchist")
    photo_path = "prevert.png"
    st.image(photo_path, caption = "This is what I think!", width=380)

else:
    my_file = st.file_uploader("Upload a CSV")
    if my_file:
        data = pd.read_csv(my_file)
        st.dataframe(data)
    # st.table(my_dataframe.iloc[0:10])

