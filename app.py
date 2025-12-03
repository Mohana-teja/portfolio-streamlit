import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Mohana Teja | Portfolio", layout="wide")

# Load CSS
with open("style.css", "r", encoding="utf-8") as f:
    css = "<style>" + f.read() + "</style>"

# Load HTML (CLEAN — no <html> <body> tags)
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Combine and render inside iframe
components.html(css + html, height=7000, scrolling=True)
