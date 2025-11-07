from lyricsgenius import Genius
import streamlit as st
import requests

st.title("🎵 Lyrics Finder App")
song = st.text_input("Enter Song Name:")
artist = st.text_input("Artist (optional):")

if st.button("Find Lyrics"):
    genius = Genius(st.secrets["GENIUS_TOKEN"])
    song_data = genius.search_song(song)
    if song_data:
        st.text_area("Lyrics", song_data.lyrics, height=400)
    else:
        st.write("Not found, trying backup...")
        res = requests.get(f"https://api.lyrics.ovh/v1/{artist}/{song}")
        data = res.json()
        st.text_area("Lyrics", data.get("lyrics", "Lyrics not found"), height=400)
