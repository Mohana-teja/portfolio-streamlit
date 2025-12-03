import streamlit as st
from pathlib import Path

# Page config
st.set_page_config(
    page_title="Mohana Teja | Portfolio",
    page_icon="💼",
    layout="wide"
)

# READ CSS FILE
def load_css(file_name):
    with open(file_name, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# READ HTML FILE
def load_html(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        html = f.read()
        st.markdown(html, unsafe_allow_html=True)

# Load CSS
load_css("style.css")

# Load HTML
load_html("index.html")

# Footer (Streamlit-safe)
st.markdown("""
<hr>
<center>© 2025 Mohana Teja • Portfolio</center>
""", unsafe_allow_html=True)
