import streamlit as st

st.set_page_config(page_title="YouTube Tool", layout="wide")

st.title("Welcome to YouTube Analysis Tool")

st.write("Navigate using the sidebar.")

st.page_link("pages/01_search_category_youtube_channels.py", label="🔍 Search Channels")
st.page_link("pages/02_capture_about.py", label="⬇️ Capture About ")
