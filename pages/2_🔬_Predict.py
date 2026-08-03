import streamlit as st
import numpy as np
from PIL import Image
import os
import json

from utils.styles import apply_custom_css
from utils.preprocessing import preprocess_pil_image
from utils.prediction import predict_rice_disease
from utils.disease_info import DISEASE_DATA
from utils.charts import plot_prediction_probabilities

st.set_page_config(page_title="Predict | Rice Leaf Disease AI", page_icon="🔬", layout="wide")
apply_custom_css()

st.title("🔬 Predict Rice Leaf Disease")
st.caption("Upload a foliage photo or choose a pre-loaded sample leaf to diagnose disease in real-time.")

st.markdown("---")

# Layout: 2 Columns (Left: Input & Image Preview, Right: Diagnosis & Charts)
left_col, right_col = st.columns([1, 1])

image_to_process = None
source_name = ""

with left_col:
    st.subheader("📤 Select Input Image")
    
    input_mode = st.radio("Choose Input Method:", ["Upload Image File", "Use Pre-loaded Sample Leaf"], horizontal=True)
    
    if input_mode == "Upload Image File":
        uploaded_file = st.file_uploader("Upload leaf image (JPG, JPEG, PNG)", type=["jpg", "jpeg", "png"])
        if uploaded_file is not None:
            image_to_process = Image.open(uploaded_file)
            source_name = uploaded_file.name
    else:
        sample_options = {
            "Bacterial Leaf Blight Sample": "samples/sample_bacterial_leaf_blight.jpg",
            "Brown Spot Sample": "samples/sample_brown_spot.jpg",
            "Leaf Smut Sample": "samples/sample_leaf_smut.jpg"
        }
        selected_sample = st.selectbox("Select Sample Image:", list(sample_options.keys()))
        sample_path = sample_options[selected_sample]
        if os.path.exists(sample_path):
            image_to_process = Image.open(sample_path)
            source_name = selected_sample

    if image_to_process is not None:
        st.markdown("#### 🖼️ Image Preview")
        st.image(image_to_process, caption=f"Source: {source_name}", use_container_width=True)
        
        # Display Image Metadata
        st.caption(f"Original Format: {image_to_process.format} | Resolution: {image_to_process.size[0]} x {image_to_process.size[1]} pixels | Mode: {image_to_process.mode}")

with right_col:
    st.subheader("🎯 AI Inference Results")
    
    if image_to_process is None:
        st.info("👆 Please upload an image or pick a sample leaf from the left panel to trigger AI prediction.")
    else:
        with st.spinner("🔄 Preprocessing image and executing MobileNetV2 prediction..."):
            # Preprocess image strictly matching notebook pipeline
            display_img, input_tensor = preprocess_pil_image(image_to_process)
            
            # Predict using saved model
            prediction_result = predict_rice_disease(input_tensor)
            
            pred_class = prediction_result["predicted_class"]
            confidence = prediction_result["confidence"]
            probs = prediction_result["probabilities"]
            
            # Disease metadata lookup
            disease_meta = DISEASE_DATA.get(pred_class, {})
            badge_color = disease_meta.get("badge_color", "#00E676")

        # Prediction Summary Card
        st.markdown(
            f"""
            <div style="background: rgba(20, 35, 22, 0.85); border: 2px solid {badge_color}; border-radius: 16px; padding: 24px; margin-bottom: 20px; text-align: center;">
                <h3 style="color: #ffffff; margin-bottom: 5px;">Diagnosed Disease</h3>
                <h1 style="color: {badge_color}; font-size: 2.2rem; margin-top: 0;">{disease_meta.get('icon', '🍃')} {pred_class}</h1>
                <p style="font-size: 1.1rem; color: #E0E0E0; margin-bottom: 0;">
                    Confidence Score: <strong style="color: {badge_color}; font-size: 1.3rem;">{confidence:.2f}%</strong>
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        # Plotly Probability Bar Chart
        st.markdown("#### 📊 Class Probability Distribution")
        fig_prob = plot_prediction_probabilities(probs)
        st.plotly_chart(fig_prob, use_container_width=True)

# Extended Treatment & Downloadable Report Section
if image_to_process is not None:
    st.markdown("---")
    st.subheader("🌿 Recommended Action & Diagnostic Report")
    
    tab_summary, tab_treatment, tab_report = st.tabs(["📋 Disease Summary", "💊 Treatment & Control", "📥 Download Report"])
    
    disease_meta = DISEASE_DATA.get(pred_class, {})
    
    with tab_summary:
        st.markdown(f"**Scientific Name:** *{disease_meta.get('scientific_name', 'N/A')}*")
        st.markdown(f"**Severity Level:** {disease_meta.get('severity', 'N/A')}")
        st.markdown(f"**Overview:** {disease_meta.get('description', 'N/A')}")
        
        st.markdown("##### Key Symptoms:")
        for s in disease_meta.get("symptoms", []):
            st.markdown(f"- {s}")
            
    with tab_treatment:
        col_t1, col_t2 = st.columns(2)
        with col_t1:
            st.markdown("##### 🧪 Recommended Remedies & Treatments:")
            for t in disease_meta.get("treatment", []):
                st.markdown(f"- {t}")
        with col_t2:
            st.markdown("##### 🛡️ Prevention & Best Practices:")
            for p in disease_meta.get("prevention", []):
                st.markdown(f"- {p}")
                
    with tab_report:
        report_text = f"""============================================================
RICE LEAF DISEASE DIAGNOSTIC REPORT
============================================================
Source File     : {source_name}
Diagnosed Class : {pred_class}
Confidence Score: {confidence:.2f}%
Scientific Name : {disease_meta.get('scientific_name', 'N/A')}
Severity Level  : {disease_meta.get('severity', 'N/A')}
------------------------------------------------------------
CLASS PROBABILITIES:
- Bacterial Leaf Blight : {probs.get('Bacterial Leaf Blight', 0.0):.2f}%
- Brown Spot            : {probs.get('Brown Spot', 0.0):.2f}%
- Leaf Smut             : {probs.get('Leaf Smut', 0.0):.2f}%
------------------------------------------------------------
RECOMMENDED INTERVENTIONS:
"""
        for t in disease_meta.get("treatment", []):
            report_text += f"* {t}\n"
            
        report_text += "============================================================\nGenerated by Rice Leaf Disease AI System\n"
        
        st.download_button(
            label="📄 Download Diagnostic Report (TXT)",
            data=report_text,
            file_name=f"Rice_Leaf_Diagnosis_{pred_class.replace(' ', '_')}.txt",
            mime="text/plain"
        )
