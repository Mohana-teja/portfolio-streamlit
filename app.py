import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Mohana Teja | Portfolio", layout="wide")

# Load CSS
with open("style.css", "r", encoding="utf-8") as f:
    css = f"<style>{f.read()}</style>"

# Load CLEAN HTML (no <html>, <body>, <head>)
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Render properly inside an iframe
components.html(css + html, height=8000, scrolling=True)
