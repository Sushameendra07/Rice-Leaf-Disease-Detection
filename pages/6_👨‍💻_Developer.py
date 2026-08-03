import streamlit as st
from utils.styles import apply_custom_css

st.set_page_config(page_title="Developer | Rice Leaf AI", page_icon="👨‍💻", layout="wide")
apply_custom_css()

st.title("👨‍💻 Developer Profile")
st.caption("AI & Machine Learning Engineer | Deep Learning Specialist")

st.markdown("---")

col_avatar, col_info = st.columns([1, 2])

with col_avatar:
    st.markdown(
        """
        <div style="background: rgba(18, 32, 20, 0.85); border: 2px solid #00E676; border-radius: 20px; padding: 30px; text-align: center; box-shadow: 0 8px 32px rgba(0,230,118,0.25);">
            <div style="font-size: 5.5rem; margin-bottom: 10px;">👨‍💻</div>
            <h2 style="color: #ffffff; margin-bottom: 5px;">Sushameendra Hampikar</h2>
            <p style="color: #00E676; font-weight: 600; font-size: 1.1rem;">AI / ML & Deep Learning Engineer</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col_info:
    st.markdown(
        """
        <div class="glass-card">
            <h3>👋 Hello, I'm Sushameendra Hampikar!</h3>
            <p>
                I specialize in building production-ready Deep Learning, Computer Vision, and Generative AI applications. 
                This project demonstrates the complete end-to-end lifecycle of an industrial AI system—from dataset extraction 
                and model benchmarking to cloud-ready web application deployment.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown("### 📬 Connect with Me")
    st.markdown(
        """
        - 📧 **Email:** [sushameendrah@gmail.com](mailto:sushameendrah@gmail.com)
        - 💼 **LinkedIn:** [linkedin.com/in/sushameendra-hampikar-559063325/](https://www.linkedin.com/in/sushameendra-hampikar-559063325/)
        - 🐙 **GitHub:** [github.com/Sushameendra07](https://github.com/Sushameendra07)
        - 📂 **Project Repository:** [github.com/Sushameendra07/Rice-Leaf-Disease-Detection](https://github.com/Sushameendra07/Rice-Leaf-Disease-Detection)
        """
    )

st.markdown("---")

# Skill Matrix Wall
st.markdown("### 🛠️ Technical Skill Matrix")

skills = [
    "Deep Learning", "Computer Vision", "TensorFlow / Keras", "Transfer Learning",
    "MobileNetV2", "VGG16", "EfficientNetB0", "OpenCV", "Python 3.12",
    "Streamlit", "Plotly", "NumPy & Pandas", "Scikit-Learn", "Data Augmentation",
    "Model Deployment", "Git & GitHub", "UI/UX Design", "Glassmorphism"
]

badge_html = "<div style='display: flex; flex-wrap: wrap; gap: 10px; margin-top: 10px;'>"
for skill in skills:
    badge_html += f"<span style='background: rgba(0, 230, 118, 0.15); border: 1px solid rgba(0, 230, 118, 0.4); color: #00E676; padding: 8px 16px; border-radius: 20px; font-weight: 500; font-size: 0.95rem;'>{skill}</span>"
badge_html += "</div>"

st.markdown(badge_html, unsafe_allow_html=True)

st.markdown("---")

st.success("🌟 Thank you for checking out the Rice Leaf Disease Detection System!")
