import streamlit as st
import os
from utils.styles import apply_custom_css

st.set_page_config(page_title="Home | Rice Leaf Disease AI", page_icon="🏠", layout="wide")
apply_custom_css()

# Page Header
st.title("🏠 Rice Leaf Disease Detection System")
st.caption("AI-Powered Agricultural Diagnostics for Crop Protection")

st.markdown("---")

# Hero Banner & Introduction
col_img, col_text = st.columns([1, 2])

with col_img:
    if os.path.exists("assets/logo.png"):
        st.image("assets/logo.png", width=220)

with col_text:
    st.markdown(
        """
        ### Welcome to Smart Farming AI! 🌾
        
        Rice is a primary staple food feeding over half of the world's population. However, foliar diseases such as 
        **Bacterial Leaf Blight**, **Brown Spot**, and **Leaf Smut** pose severe threats to crop yields and food security.
        
        This web application leverages **Deep Learning & Computer Vision** to instantly analyze rice leaf images, 
        identify pathogens, and provide actionable agricultural interventions for farmers, agronomists, and researchers.
        """
    )

st.markdown("---")

# Animated Metrics Showcase
st.markdown("### 📈 Project Key Metrics")

m1, m2, m3, m4 = st.columns(4)
m1.metric(label="Best Model Accuracy", value="95.65%", delta="MobileNetV2")
m2.metric(label="Precision Score", value="96.20%", delta="Weighted Avg")
m3.metric(label="Recall Score", value="95.65%", delta="Weighted Avg")
m4.metric(label="F1 Score", value="95.65%", delta="Weighted Avg")

st.markdown("---")

# Feature Highlights Grid
st.markdown("### 🛠️ Key Capabilities")

c1, c2 = st.columns(2)

with c1:
    st.markdown(
        """
        <div class="glass-card">
            <h4>1. Instant Disease Prediction</h4>
            <ul>
                <li>Supports image uploads in <strong>JPG, JPEG, PNG</strong> formats.</li>
                <li>Automatic preprocessing (224x224 RGB resizing, float32 scaling <code>1/255</code>).</li>
                <li>Real-time probability chart generation using Plotly.</li>
                <li>Exportable diagnostic report download.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

with c2:
    st.markdown(
        """
        <div class="glass-card">
            <h4>2. Deep Learning Benchmark Dashboard</h4>
            <ul>
                <li>Side-by-side comparison of <strong>Custom CNN</strong>, <strong>MobileNetV2</strong>, <strong>VGG16</strong>, and <strong>EfficientNetB0</strong>.</li>
                <li>Interactive confusion matrices, classification metrics, and loss curves.</li>
                <li>Complete model evaluation data derived directly from validation splits.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("---")
st.info("💡 **Ready to test?** Navigate to the **Predict** page in the sidebar to upload a rice leaf image or choose a pre-loaded sample!")
