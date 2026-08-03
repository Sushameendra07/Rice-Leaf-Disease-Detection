"""
Shared CSS & Styling Utility for Rice Leaf Disease AI System
Enforces unified Dark Glassmorphic UI with Emerald/Leaf Green & Amber Accents across all pages.
"""

import streamlit as st
import os

CUSTOM_CSS = """
<style>
/* Global Imports & Root Variables */
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&family=Inter:wght@300;400;500;600&display=swap');

:root {
    --bg-primary: #0a120b;
    --bg-card: rgba(18, 32, 20, 0.7);
    --border-card: rgba(76, 175, 80, 0.3);
    --accent-green: #00E676;
    --accent-emerald: #2e7d32;
    --accent-amber: #FFB74D;
    --text-main: #F0F4F1;
    --text-muted: #A0B2A3;
}

/* Base Body & App Background Styling */
.stApp {
    background: radial-gradient(circle at 15% 15%, #0e1e11 0%, #060c07 100%) !important;
    font-family: 'Inter', sans-serif !important;
    color: var(--text-main) !important;
}

/* Glassmorphism Cards */
.glass-card {
    background: var(--bg-card) !important;
    backdrop-filter: blur(12px) !important;
    -webkit-backdrop-filter: blur(12px) !important;
    border: 1px solid var(--border-card) !important;
    border-radius: 16px !important;
    padding: 24px !important;
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37) !important;
    transition: transform 0.3s ease, border-color 0.3s ease !important;
    margin-bottom: 20px !important;
}

.glass-card:hover {
    transform: translateY(-4px) !important;
    border-color: rgba(76, 175, 80, 0.6) !important;
}

/* Hero Container */
.hero-container {
    background: linear-gradient(135deg, rgba(27, 67, 38, 0.85) 0%, rgba(10, 25, 12, 0.95) 100%) !important;
    border: 1px solid rgba(76, 175, 80, 0.45) !important;
    border-radius: 20px !important;
    padding: 35px 30px !important;
    text-align: center !important;
    box-shadow: 0 10px 40px rgba(0, 230, 118, 0.18) !important;
    margin-bottom: 25px !important;
}

.hero-title {
    font-family: 'Outfit', sans-serif !important;
    font-size: 2.6rem !important;
    font-weight: 700 !important;
    background: linear-gradient(90deg, #FFFFFF 0%, #A5D6A7 50%, #00E676 100%) !important;
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
    margin-bottom: 10px !important;
}

.hero-subtitle {
    font-size: 1.15rem !important;
    color: var(--text-muted) !important;
    max-width: 850px !important;
    margin: 0 auto 15px auto !important;
}

/* Animated Stat Cards */
.stat-card {
    background: rgba(22, 40, 24, 0.75) !important;
    border: 1px solid rgba(0, 230, 118, 0.25) !important;
    border-radius: 14px !important;
    padding: 20px !important;
    text-align: center !important;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25) !important;
}

.stat-number {
    font-family: 'Outfit', sans-serif !important;
    font-size: 2.2rem !important;
    font-weight: 700 !important;
    color: var(--accent-green) !important;
    margin-bottom: 4px !important;
}

.stat-label {
    font-size: 0.85rem !important;
    color: var(--text-muted) !important;
    text-transform: uppercase !important;
    letter-spacing: 1px !important;
}

/* Custom Buttons */
.stButton > button {
    background: linear-gradient(135deg, #2e7d32 0%, #1b5e20 100%) !important;
    color: #ffffff !important;
    font-weight: 600 !important;
    border: 1px solid rgba(76, 175, 80, 0.6) !important;
    border-radius: 12px !important;
    padding: 10px 24px !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2) !important;
}

.stButton > button:hover {
    background: linear-gradient(135deg, #388e3c 0%, #2e7d32 100%) !important;
    border-color: #00E676 !important;
    box-shadow: 0 6px 20px rgba(0, 230, 118, 0.3) !important;
    transform: scale(1.02) !important;
}

/* Download Button Custom Styling */
.stDownloadButton > button {
    background: linear-gradient(135deg, #1b5e20 0%, #0d3b10 100%) !important;
    color: #00E676 !important;
    font-weight: 600 !important;
    border: 1px solid #00E676 !important;
    border-radius: 12px !important;
}

/* Sidebar Custom Styling */
section[data-testid="stSidebar"] {
    background-color: #081109 !important;
    border-right: 1px solid rgba(76, 175, 80, 0.25) !important;
}

/* Streamlit Headers & Text */
h1, h2, h3 {
    color: #F0F4F1 !important;
    font-family: 'Outfit', sans-serif !important;
}

/* Tables Custom Styling */
.stTable, div[data-testid="stTable"] {
    background: rgba(18, 32, 20, 0.7) !important;
    border-radius: 12px !important;
    border: 1px solid rgba(76, 175, 80, 0.25) !important;
}

/* Custom Footer */
.custom-footer {
    text-align: center !important;
    padding: 20px !important;
    color: var(--text-muted) !important;
    border-top: 1px solid rgba(76, 175, 80, 0.2) !important;
    margin-top: 40px !important;
    font-size: 0.9rem !important;
}
</style>
"""

def apply_custom_css():
    """
    Applies unified CSS styling and renders common sidebar branding across all app pages.
    """
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)
    
    # Common Sidebar Branding
    with st.sidebar:
        if os.path.exists("assets/logo.png"):
            st.image("assets/logo.png", width=110)
        st.markdown("### 🌾 Rice Leaf AI")
        st.caption("Deep Learning Diagnostic System")
        st.markdown("---")
        st.markdown(
            """
            <div style="background: rgba(0, 230, 118, 0.1); border: 1px solid rgba(0, 230, 118, 0.3); padding: 12px; border-radius: 12px; font-size: 0.85rem;">
                🎯 <strong>Model:</strong> MobileNetV2<br>
                ⚡ <strong>Accuracy:</strong> 95.65%<br>
                🍃 <strong>Classes:</strong> 3 Rice Diseases<br>
                👨‍💻 <strong>Dev:</strong> Sushameendra H.
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown("---")
