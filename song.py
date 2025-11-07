import streamlit as st
from lyricsgenius import Genius
import requests

st.title("🎵 Lyrics Finder App")
song = st.text_input("Enter Song Name:")
artist = st.text_input("Artist (optional):")

if st.button("Find Lyrics"):
    genius = Genius("k6fdieOY12aWgCDC6SWYqfXOZrxpguNe5hY14icmh831D45Q1_L0hX8pVuf4FZsh")
    song_data = genius.search_song(song)
    if song_data:
        st.text_area("Lyrics", song_data.lyrics, height=400)
    else:
        st.write("Not found, trying backup...")
        res = requests.get(f"https://api.lyrics.ovh/v1/{artist}/{song}")
        data = res.json()
        st.text_area("Lyrics", data.get("lyrics", "Lyrics not found"), height=400)
