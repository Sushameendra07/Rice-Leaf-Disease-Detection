import streamlit as st
import os
from utils.styles import apply_custom_css
from utils.disease_info import DISEASE_DATA

st.set_page_config(page_title="Disease Catalog | Rice Leaf AI", page_icon="🌿", layout="wide")
apply_custom_css()

st.title("🌿 Rice Leaf Disease Catalog")
st.caption("Comprehensive agricultural reference guide for identification, treatment, and crop protection.")

st.markdown("---")

# Select Disease Category
disease_name = st.selectbox(
    "Select Disease Category to Inspect:",
    list(DISEASE_DATA.keys()),
    index=0
)

data = DISEASE_DATA[disease_name]

# Disease Header Card
st.markdown(
    f"""
    <div style="background: rgba(18, 32, 20, 0.7); border-left: 6px solid {data['badge_color']}; border-radius: 12px; padding: 20px; margin-bottom: 25px;">
        <h2 style="color: #ffffff; margin-top: 0;">{data['icon']} {data['disease_name']}</h2>
        <p style="color: #A0B2A3; font-style: italic; font-size: 1.1rem; margin-bottom: 5px;">Scientific Name: {data['scientific_name']}</p>
        <span style="background: {data['badge_color']}; color: #000000; font-weight: 700; padding: 4px 12px; border-radius: 20px; font-size: 0.85rem;">
            Severity: {data['severity']}
        </span>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("### 📜 Description & Overview")
st.write(data["description"])

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### ⚠️ Key Symptoms")
    for s in data["symptoms"]:
        st.markdown(f"- {s}")
        
    st.markdown("### 🔍 Underlying Causes")
    for c in data["causes"]:
        st.markdown(f"- {c}")

with col2:
    st.markdown("### 💊 Treatment & Remedies")
    for t in data["treatment"]:
        st.markdown(f"- {t}")
        
    st.markdown("### 🛡️ Prevention Strategies")
    for p in data["prevention"]:
        st.markdown(f"- {p}")

st.markdown("---")

st.markdown("### 🚜 Recommended Farming Practices")
for f in data["farming_practices"]:
    st.markdown(f"- {f}")

st.markdown("---")

# Grid comparing all 3 diseases at a glance
st.markdown("### 📋 Quick Comparison Matrix")

st.table([
    {
        "Disease": name,
        "Scientific Name": info["scientific_name"],
        "Primary Symptoms": info["symptoms"][0],
        "Key Fungicide/Treatment": info["treatment"][0]
    }
    for name, info in DISEASE_DATA.items()
])
