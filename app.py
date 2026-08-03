import streamlit as st
import os
from utils.styles import apply_custom_css

# Page Configuration
st.set_page_config(
    page_title="Rice Leaf Disease AI | Deep Learning System",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply Unified Green Dark Glassmorphism CSS Theme & Sidebar
apply_custom_css()

# Main Page Hero Banner & Landing View
if os.path.exists("assets/banner.png"):
    st.image("assets/banner.png", use_container_width=True)

st.markdown(
    """
    <div class="hero-container">
        <div class="hero-title">🌾 Rice Leaf Disease Detection</div>
        <div class="hero-subtitle">
            An advanced AI-powered precision agriculture platform utilizing Transfer Learning (MobileNetV2) 
            to diagnose rice plant foliage diseases instantly with high accuracy.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Animated Statistics Row
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(
        """
        <div class="stat-card">
            <div class="stat-number">95.65%</div>
            <div class="stat-label">Model Accuracy</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div class="stat-card">
            <div class="stat-number">3</div>
            <div class="stat-label">Disease Categories</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        """
        <div class="stat-card">
            <div class="stat-number">120</div>
            <div class="stat-label">Dataset Images</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col4:
    st.markdown(
        """
        <div class="stat-card">
            <div class="stat-number">4</div>
            <div class="stat-label">Models Benchmarked</div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("---")

# Core Features Section
st.markdown("### 🌟 Application Features")

f_col1, f_col2, f_col3 = st.columns(3)

with f_col1:
    st.markdown(
        """
        <div class="glass-card">
            <h4>🔬 Real-Time Prediction</h4>
            <p>Upload foliage images (JPG, PNG) for immediate AI inference. Generates probability distributions and confidence scores.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with f_col2:
    st.markdown(
        """
        <div class="glass-card">
            <h4>🌿 Agricultural Remedies</h4>
            <p>Access structured farming recommendations, symptoms, cause analysis, and organic & chemical treatment options.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with f_col3:
    st.markdown(
        """
        <div class="glass-card">
            <h4>📊 Interactive Dashboard</h4>
            <p>Explore Plotly benchmark visualizations comparing MobileNetV2 against Custom CNN, VGG16, and EfficientNetB0.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# Quick Action CTA
st.info("👈 Select a page from the sidebar to start diagnosis or view benchmarks!")

# Custom Footer
st.markdown(
    """
    <div class="custom-footer">
        🌾 Rice Leaf Disease Detection App | Developed by <strong>Sushameendra Hampikar</strong> | Built with Streamlit & TensorFlow
    </div>
    """,
    unsafe_allow_html=True
)
