import requests
import streamlit as st
from datetime import datetime
from dotenv import load_dotenv
import os

# # Get credentials from .env
# load_dotenv()
# api_key = os.getenv('API_KEY')

# Get the JSON for Astronomy Picture of the Day
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
response = requests.get(url)
content = response.json()

# Get title, desc, copyright info, date, and image from the JSON
title = content['title']
desc = content['explanation']
copyright_owner = content['copyright']

date = content['date']
date = datetime.strptime(date, "%Y-%m-%d").strftime("%B %d, %Y")  # Format date as Month DD, YYYY

img_url = content['url']
img = requests.get(img_url).content

# STREAMLIT

st.set_page_config(page_title='Astronomy Picture of the Day', layout="centered")

st.header("🌌 Astronomy Picture of the Day")

st.subheader(f"{date}:  {title}")

st.image(img)

st.markdown(
    f"""
    <div style="text-align: right; font-size: small; margin-top: -10px; margin-bottom: 40px">
        © {copyright_owner}
    </div>
    """,
    unsafe_allow_html=True
)


st.write(desc)
st.write(" ")

st.caption("This is a student project for the [Python Mega Course: Learn Python in 60 Days, Build 20 Apps]"
     "(https://www.udemy.com/course/the-python-mega-course) with Ardit Sulce.", unsafe_allow_html=True)

