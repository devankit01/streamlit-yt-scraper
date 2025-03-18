
import streamlit as st
import yt_dlp
import csv
import pandas as pd
import os


def search_youtube_channels(query, max_results=10):
    """Search for YouTube channels and extract their URLs and view count."""
    ydl_opts = {
        'quiet': True,
        'extract_flat': True,
        'default_search': 'ytsearch',
        'force_generic_extractor': True
    }

    channels = []
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            search_results = ydl.extract_info(f"ytsearch{max_results}: {query}", download=False)
            if 'entries' in search_results:
                for entry in search_results['entries']:
                    if entry.get('channel_url') and entry.get('channel'):
                        channels.append({
                            'channel_name': entry.get('channel'),
                            'channel_url': entry.get('channel_url'),
                            'views': entry.get('view_count', 0)  # Defaults to 0 if missing
                        })
    except Exception as e:
        st.error(f"Error fetching channel data: {e}")
    return channels

def save_to_csv(channels, filename="youtube_channels.csv"):
    """Save the channel data to a CSV file."""
    if not channels:
        return None
    df = pd.DataFrame(channels)
    df.to_csv(filename, index=False, encoding='utf-8')
    return filename
