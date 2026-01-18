import streamlit as st
from pathlib import Path
import base64

st.set_page_config(
    page_title="AuraNest Global Solutions",
    layout="wide"
)

def load_image(image_path):
    return base64.b64encode(
        Path(image_path).read_bytes()
    ).decode()

# Load images
EFuseConnect = load_image("assets/im1.jpeg")
Eutility = load_image("assets/Eutility.jpg")

# Load HTML
html = Path("index.html").read_text(encoding="utf-8")

# Inject images into HTML
html = html.replace("{{EFuseConnect}}", EFuseConnect)
html = html.replace("{{Eutility}}", Eutility)

# Render
st.components.v1.html(html, height=2200, scrolling=True)
