import streamlit as st
from pathlib import Path
import base64

st.set_page_config(
    page_title="AuraNest Global Solutions",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Remove Streamlit default padding & header
st.markdown(
    """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100% !important;
    }
    iframe {
        height: 100vh !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def load_image(image_path):
    return base64.b64encode(
        Path(image_path).read_bytes()
    ).decode()

# Load images
logo = load_image("assets/logo.jpg")
EFuseConnect = load_image("assets/im1.jpeg")
Eutility = load_image("assets/Eutility.jpg")
BuildOps360 = load_image("assets/BuildOps360.png")
COMSID1 = load_image("assets/2.jpg")
COMSID2 = load_image("assets/3.png")
CloudFEAT = load_image("assets/CloudFEAT.jpg")
MarinPRO = load_image("assets/MarinPRO.jpg")
Education = load_image("assets/Education.png")


# Load HTML
html = Path("index.html").read_text(encoding="utf-8")

# Inject images into HTML
html = html.replace("{{EFuseConnect}}", EFuseConnect)
html = html.replace("{{Eutility}}", Eutility)
html = html.replace("{{BuildOps360}}", BuildOps360)
html = html.replace("{{COMSID1}}", COMSID1)
html = html.replace("{{COMSID2}}", COMSID2)
html = html.replace("{{CloudFEAT}}", CloudFEAT)
html = html.replace("{{MarinPRO}}", MarinPRO)
html = html.replace("{{Education}}", Education)

# Render
st.components.v1.html(html, height=2200, scrolling=True)
