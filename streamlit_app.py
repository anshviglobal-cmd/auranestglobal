import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="AuraNest Global Solutions",
    layout="wide"
)

# Load HTML
html_file = Path("index.html").read_text(encoding="utf-8")

# Render HTML
st.components.v1.html(html_file, height=2000, scrolling=True)
