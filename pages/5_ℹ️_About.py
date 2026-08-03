import streamlit as st
import pandas as pd
from utils.styles import apply_custom_css

st.set_page_config(page_title="About Project | Rice Leaf AI", page_icon="ℹ️", layout="wide")
apply_custom_css()

st.title("ℹ️ About the Project")
st.caption("Detailed Technical Overview, Deep Learning Workflow, Challenges, and Future Directions.")

st.markdown("---")

# 1. Project Overview & Problem Statement
col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
        <div class="glass-card">
            <h3>📖 Project Overview</h3>
            <p>
                Rice (<em>Oryza sativa</em>) is the primary food source feeding over half of the world's population. 
                Foliar plant diseases can ruin up to 50% of annual crop yields if not detected early. 
                Traditional manual visual inspection by agricultural experts is time-consuming, expensive, and subjective.
            </p>
            <p>
                This project builds an automated computer-vision deep learning solution that accurately detects and classifies <strong>3 major rice leaf diseases</strong>:
                <strong>Bacterial Leaf Blight</strong>, <strong>Brown Spot</strong>, and <strong>Leaf Smut</strong>.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div class="glass-card">
            <h3>🎯 Problem Statement</h3>
            <p>
                Farmers in remote agricultural regions often lack immediate access to plant pathologists. 
                Delayed diagnosis leads to inappropriate pesticide use, financial losses, and crop failure.
            </p>
            <p>
                <strong>Goal:</strong> Develop an accessible, high-accuracy, light-weight deep learning web platform 
                capable of instant foliar disease diagnosis from smartphone leaf photos.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("---")

# 2. Deep Learning Workflow
st.markdown("### 🔄 End-to-End System Architecture Workflow")

st.markdown(
    """
    <div style="background: rgba(18, 32, 20, 0.85); border: 1px solid rgba(76, 175, 80, 0.45); padding: 20px; border-radius: 12px; font-family: monospace; font-size: 0.95rem;">
        📥 [Raw Image Upload] ➡️ 🧹 [OpenCV & PIL Preprocessing: RGB, Resize (224x224), Scale /255] <br>
        ⬇️ <br>
        🧠 [TensorFlow MobileNetV2 Inference Engine] ➡️ 📊 [Softmax Probability Vector] <br>
        ⬇️ <br>
        📱 [Streamlit Glassmorphic UI & Interactive Plotly Charts] ➡️ 📄 [Downloadable Action Report]
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# 3. Dataset Information & Augmentation
st.markdown("### 📦 Dataset & Image Preprocessing")

col_d1, col_d2 = st.columns(2)

with col_d1:
    st.markdown(
        """
        <div class="glass-card">
            <h4>Dataset Breakdown:</h4>
            <ul>
                <li><strong>Total Images:</strong> 120 Rice Leaf Images</li>
                <li><strong>Number of Classes:</strong> 3 Classes
                    <ul>
                        <li>Bacterial Leaf Blight: 40 Images</li>
                        <li>Brown Spot: 40 Images</li>
                        <li>Leaf Smut: 40 Images (39 clean)</li>
                    </ul>
                </li>
                <li><strong>Validation Split:</strong> 80% Training (97 images), 20% Validation (23 images)</li>
                <li><strong>Target Resolution:</strong> 224 x 224 pixels x 3 RGB channels</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

with col_d2:
    st.markdown("#### 🧪 Data Augmentation Techniques:")
    aug_df = pd.DataFrame({
        "Technique": [
            "Image Rescaling",
            "Random Rotation",
            "Width Shift",
            "Height Shift",
            "Random Zoom",
            "Horizontal Flip",
            "Validation Split"
        ],
        "Configuration / Purpose": [
            "1. / 255.0 pixel normalization",
            "Up to 20° rotation for orientation invariance",
            "0.2 shift for horizontal placement",
            "0.2 shift for vertical placement",
            "0.2 zoom range for scale invariance",
            "True - flip images horizontally",
            "20% held-out test subset"
        ]
    })
    st.table(aug_df)

st.markdown("---")

# 4. Transfer Learning & Models Evaluated
st.markdown("### 🏗️ Deep Learning Architectures Evaluated")

st.markdown(
    """
    Four distinct deep learning architectures were trained and benchmarked:
    1. **Custom CNN:** 3 Convolution + Batch Normalization + MaxPooling blocks + Dense layer.
    2. **MobileNetV2 (Best Model - 95.65% Accuracy):** Lightweight architecture utilizing depthwise separable convolutions and inverted residual blocks. Pre-trained on ImageNet.
    3. **VGG16 (82.61% Accuracy):** 16-layer deep convolutional network with fixed 3x3 filters.
    4. **EfficientNetB0 (30.43% Accuracy):** Compound scaling convolutional architecture.
    """
)

st.markdown("---")

# 5. Key Engineering Challenges
st.markdown("### ⚠️ Engineering Challenges & Solutions")

challenges = [
    ("Limited Dataset Size (120 Images)", "Solved using Transfer Learning with pre-trained ImageNet weights to prevent training from scratch."),
    ("Preventing Overfitting", "Applied Dropout layers (0.4 rate), Batch Normalization, and EarlyStopping with ReduceLROnPlateau callbacks."),
    ("Selecting Best Architecture", "Extensive empirical benchmarking across 4 models; MobileNetV2 outperformed VGG16 by 13% in accuracy."),
    ("Preprocessing Consistency", "Enforced strict RGB color ordering and 1/255 float32 scaling across training, validation, and live Streamlit deployment."),
    ("Model Deployment on Cloud", "Exported model in modern native `.keras` format, cached in Streamlit using `@st.cache_resource` for low memory footprint.")
]

for c_title, c_desc in challenges:
    st.markdown(f"**🔹 {c_title}:** {c_desc}")

st.markdown("---")

# 6. Future Scope
st.markdown("### 🚀 Future Scope & Enhancements")

st.markdown(
    """
    - 📸 **Mobile Native Integration:** Build Progressive Web App (PWA) or Flutter mobile app for offline field diagnosis.
    - 🌍 **Multi-Language Support:** Localize farming advice into regional languages (Hindi, Tamil, Telugu, Bengali, Kannada, Punjabi).
    - 📡 **IoT & Drone Imagery Integration:** Connect with multispectral drone aerial cameras for automated field scanning.
    - 🌾 **Expanded Disease Coverage:** Expand dataset to classify 10+ paddy diseases including Rice Blast, Tungro, and Sheath Blight.
    """
)
