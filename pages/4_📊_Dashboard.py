import streamlit as st
import pandas as pd

from utils.styles import apply_custom_css
from utils.disease_info import MODEL_BENCHMARK_DATA
from utils.charts import plot_model_comparison, plot_metrics_radar, plot_confusion_matrix

st.set_page_config(page_title="Performance Dashboard | Rice Leaf AI", page_icon="📊", layout="wide")
apply_custom_css()

st.title("📊 Deep Learning Performance Dashboard")
st.caption("Benchmark analysis and evaluation metrics for Rice Leaf Disease Classification models.")

st.markdown("---")

# High-Level Metrics Summary Cards
st.subheader("🏆 Champion Model: MobileNetV2 Metrics")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Accuracy", "95.65%", "+13.04% over VGG16")
col2.metric("Precision", "96.20%", "+13.73% over VGG16")
col3.metric("Recall", "95.65%", "+13.04% over VGG16")
col4.metric("F1-Score", "95.65%", "+13.35% over VGG16")

st.markdown("---")

# Model Comparison Section with Interactive Plotly Charts
st.subheader("⚔️ Deep Learning Architectures Benchmark")

tab_bar, tab_radar, tab_cm, tab_table = st.tabs([
    "📊 Model Comparison Bar Chart", 
    "🎯 Metric Radar Chart", 
    "🧩 Confusion Matrix", 
    "📋 Benchmark Data Table"
])

with tab_bar:
    fig_bar = plot_model_comparison()
    st.plotly_chart(fig_bar, use_container_width=True)
    st.caption("Evaluation scores calculated on 20% validation split (23 validation images).")

with tab_radar:
    fig_radar = plot_metrics_radar()
    st.plotly_chart(fig_radar, use_container_width=True)
    st.caption("Radar comparison highlighting the performance lead of MobileNetV2 over VGG16.")

with tab_cm:
    fig_cm = plot_confusion_matrix()
    st.plotly_chart(fig_cm, use_container_width=True)
    st.caption("Confusion matrix showing accurate classification across Bacterial Blight, Brown Spot, and Leaf Smut.")

with tab_table:
    df_metrics = pd.DataFrame.from_dict(MODEL_BENCHMARK_DATA, orient="index")
    df_metrics = df_metrics.round(4)
    st.dataframe(df_metrics, use_container_width=True)

st.markdown("---")

# Deep-Dive Insights
st.subheader("💡 Technical Benchmark Analysis")

c_left, c_right = st.columns(2)

with c_left:
    st.markdown(
        """
        <div class="glass-card">
            <h4>🟢 Why MobileNetV2 Performed Best (95.65%)</h4>
            <ul>
                <li><strong>Depthwise Separable Convolutions:</strong> Drastically reduces parameters (~2.2M) while retaining spatial features.</li>
                <li><strong>Inverted Residual Blocks:</strong> Retains non-linear features in low dimensions without information loss.</li>
                <li><strong>Pre-trained ImageNet Weights:</strong> Transfer learning allowed rapid feature extraction even on a compact dataset (120 images).</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

with c_right:
    st.markdown(
        """
        <div class="glass-card">
            <h4>🔴 Limitations of Custom CNN & EfficientNetB0</h4>
            <ul>
                <li><strong>Custom CNN (34.78%):</strong> Severe overfitting due to shallow depth and lack of pre-trained feature representations.</li>
                <li><strong>EfficientNetB0 (30.43%):</strong> Requires larger batch sizes and compound scaling fine-tuning to converge on small datasets.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )
