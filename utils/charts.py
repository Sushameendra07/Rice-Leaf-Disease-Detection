"""
Plotly Chart Utility for Rice Leaf Disease Detection
Custom interactive charts matching the dark leaf UI design.
"""

import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from utils.disease_info import MODEL_BENCHMARK_DATA

DARK_TEMPLATE = "plotly_dark"
COLOR_PALETTE = {
    "Bacterial Leaf Blight": "#FF5252",
    "Brown Spot": "#FFB74D",
    "Leaf Smut": "#26A69A",
    "Background": "rgba(20, 30, 20, 0.6)",
    "Accent": "#4CAF50"
}


def plot_prediction_probabilities(probabilities: dict) -> go.Figure:
    """
    Plots horizontal bar chart for prediction confidence distribution.
    """
    df = pd.DataFrame({
        "Disease": list(probabilities.keys()),
        "Probability (%)": list(probabilities.values())
    })
    
    # Custom color mapping per disease
    colors = [
        COLOR_PALETTE.get(disease, "#4CAF50")
        for disease in df["Disease"]
    ]
    
    fig = px.bar(
        df,
        x="Probability (%)",
        y="Disease",
        orientation="h",
        text="Probability (%)",
        color="Disease",
        color_discrete_map=COLOR_PALETTE,
        title="Prediction Confidence Distribution"
    )
    
    fig.update_traces(
        texttemplate="%{text:.2f}%",
        textposition="outside",
        marker_line_color="#1b2e1b",
        marker_line_width=1.5
    )
    
    fig.update_layout(
        template=DARK_TEMPLATE,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(15, 23, 15, 0.7)",
        xaxis=dict(range=[0, 115], title="Confidence (%)", gridcolor="rgba(255,255,255,0.1)"),
        yaxis=dict(title="Disease Class", gridcolor="rgba(255,255,255,0.1)"),
        font=dict(family="Inter, sans-serif", color="#e0e0e0"),
        showlegend=False,
        height=320,
        margin=dict(l=20, r=20, t=50, b=20)
    )
    
    return fig


def plot_model_comparison() -> go.Figure:
    """
    Grouped bar chart comparing CNN, MobileNetV2, VGG16, and EfficientNetB0 performance metrics.
    """
    data = []
    for model_name, metrics in MODEL_BENCHMARK_DATA.items():
        for metric_name in ["Accuracy", "Precision", "Recall", "F1-Score"]:
            data.append({
                "Model": model_name,
                "Metric": metric_name,
                "Score": metrics[metric_name]
            })
    
    df = pd.DataFrame(data)
    
    fig = px.bar(
        df,
        x="Metric",
        y="Score",
        color="Model",
        barmode="group",
        text_auto=".4f",
        title="Deep Learning Model Performance Benchmark",
        color_discrete_sequence=["#81C784", "#00E676", "#FFB74D", "#E57373"]
    )
    
    fig.update_traces(
        textposition="outside",
        cliponaxis=False
    )
    
    fig.update_layout(
        template=DARK_TEMPLATE,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(15, 23, 15, 0.7)",
        yaxis=dict(range=[0, 1.15], title="Score", gridcolor="rgba(255,255,255,0.1)"),
        xaxis=dict(title="Evaluation Metrics"),
        legend=dict(title="Architectures", orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        font=dict(family="Inter, sans-serif", color="#e0e0e0"),
        height=450,
        margin=dict(l=20, r=20, t=80, b=20)
    )
    
    return fig


def plot_metrics_radar() -> go.Figure:
    """
    Radar chart for MobileNetV2 metrics.
    """
    categories = ["Accuracy", "Precision", "Recall", "F1-Score"]
    mobilenet_scores = [0.9565, 0.9620, 0.9565, 0.9565]
    vgg_scores = [0.8261, 0.8247, 0.8261, 0.8230]
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=mobilenet_scores + [mobilenet_scores[0]],
        theta=categories + [categories[0]],
        fill='toself',
        name='MobileNetV2 (Best)',
        fillcolor='rgba(0, 230, 118, 0.35)',
        line=dict(color='#00E676', width=3)
    ))
    
    fig.add_trace(go.Scatterpolar(
        r=vgg_scores + [vgg_scores[0]],
        theta=categories + [categories[0]],
        fill='toself',
        name='VGG16',
        fillcolor='rgba(255, 183, 77, 0.2)',
        line=dict(color='#FFB74D', width=2, dash='dash')
    ))
    
    fig.update_layout(
        template=DARK_TEMPLATE,
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 1.0], gridcolor="rgba(255,255,255,0.1)"),
            bgcolor="rgba(15, 23, 15, 0.7)"
        ),
        paper_bgcolor="rgba(0,0,0,0)",
        showlegend=True,
        title="MobileNetV2 vs VGG16 Metrics Radar",
        height=400,
        margin=dict(l=40, r=40, t=50, b=40)
    )
    
    return fig


def plot_confusion_matrix() -> go.Figure:
    """
    Plotly heatmap for MobileNetV2 confusion matrix on validation dataset.
    """
    # Validation split matrix (23 total samples: 8 Bacterial, 8 Brown Spot, 7 Leaf Smut)
    z = [
        [8, 0, 0],
        [0, 8, 0],
        [1, 0, 6]
    ]
    x = ["Bacterial Blight", "Brown Spot", "Leaf Smut"]
    y = ["Bacterial Blight", "Brown Spot", "Leaf Smut"]
    
    fig = px.imshow(
        z,
        x=x,
        y=y,
        text_auto=True,
        color_continuous_scale="Greens",
        title="Best Model (MobileNetV2) Confusion Matrix"
    )
    
    fig.update_layout(
        template=DARK_TEMPLATE,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(15, 23, 15, 0.7)",
        xaxis_title="Predicted Class",
        yaxis_title="Actual Class",
        height=400,
        margin=dict(l=20, r=20, t=50, b=20)
    )
    
    return fig
