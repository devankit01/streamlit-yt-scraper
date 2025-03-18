import streamlit as st
import os
import asyncio
from playwright.async_api import async_playwright

# Temp folder to store screenshots
TMP_FOLDER = "tmp"
os.makedirs(TMP_FOLDER, exist_ok=True)

async def capture_screenshot(url, filename):
    """Captures a fixed height (500px) of the YouTube About page."""
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        try:
            await page.goto(url, timeout=15000)
            await asyncio.sleep(2)  # Wait for 2 seconds to load content

            # Set viewport to capture only 500px height
            await page.set_viewport_size({"width": 1280, "height": 800})

            # Capture screenshot
            await page.screenshot(path=os.path.join(TMP_FOLDER, filename), full_page=False)
            return filename

        except Exception as e:
            st.error(f"Failed to capture {url}: {e}")
            return None
        finally:
            await browser.close()

# Streamlit UI
st.title("YouTube Channel About Page Screenshot")

channel_url = st.text_input("Enter YouTube Channel URL:", "")

if channel_url and st.button("Capture Screenshot"):
    about_url = channel_url.rstrip("/") + "/about"
    filename = "channel_about.png"

    with st.spinner("Processing..."):
        result = asyncio.run(capture_screenshot(about_url, filename))

    if result:
        file_path = os.path.join(TMP_FOLDER, filename)
        st.image(file_path, caption="Captured About Section (500px Height)")
        with open(file_path, "rb") as file:
            st.download_button("Download Screenshot", file, file_name="channel_about.png")
