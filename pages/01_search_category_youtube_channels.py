import streamlit as st
import pandas as pd
from utils.yt import search_youtube_channels, save_to_csv
import os

st.title("YouTube Channel Search")

query = st.text_input("Enter search query:", "indian comedian")
max_results = st.number_input("Max results:", min_value=1, max_value=10000, value=10)

if st.button("Search"):
    with st.spinner("Fetching data..."):
        channels = search_youtube_channels(query, max_results)
        if channels:
            st.success(f"Found {len(channels)} channels!")
            df = pd.DataFrame(channels)
            st.dataframe(df)
            csv_file = save_to_csv(channels)
            if csv_file:
                with open(csv_file, "rb") as file:
                    st.download_button(
                        label="Download CSV",
                        data=file,
                        file_name="youtube_channels.csv",
                        mime="text/csv"
                    )
                os.remove(csv_file)
        else:
            st.warning("No channels found.")
