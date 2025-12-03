import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Mohana Teja | Portfolio", layout="wide")

# Read CSS
with open("style.css", "r", encoding="utf-8") as f:
    css = f"<style>{f.read()}</style>"

# Read HTML (inner HTML only)
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Combine and render
components.html(css + html, height=8000, scrolling=True)
