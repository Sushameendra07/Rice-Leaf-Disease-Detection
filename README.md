# 🌾 Rice Leaf Disease Detection System (PRCP-1001)

An enterprise-grade artificial intelligence agriculture web application designed to classify foliar rice plant diseases into 3 distinct clinical categories with **95.65% accuracy**. Developed by **Sushameendra H**, the application features a modern glassmorphic interface, interactive analytics hub, AI leaf scanner, diagnostic report generator, and developer portfolio.

- **Developer:** Sushameendra H
- **Education:** B.E. Computer Science & Engineering | Jain College of Engineering and Technology (2022–2026)
- **GitHub:** [https://github.com/Sushameendra07](https://github.com/Sushameendra07)
- **Email:** [sushameendrah@gmail.com](mailto:sushameendrah@gmail.com)
- **Project Repository:** [https://github.com/Sushameendra07/Rice-Leaf-Disease-Detection](https://github.com/Sushameendra07/Rice-Leaf-Disease-Detection)

---

## 🌟 Key Application Features

### 🏠 Executive Dashboard:
- Modern glassmorphism UI layout with dark emerald background styling.
- Real-time animated KPI cards displaying Accuracy (**95.65%**), Weighted Precision (**96.20%**), Recall (**95.65%**), and F1-Score (**95.65%**).
- Interactive Machine Learning workflow breakdown and disease category index.

### 📊 Interactive Analytics Hub:
- Reuses notebook Exploratory Data Analysis (EDA) visualizations powered by Plotly.
- Model performance benchmark comparing 4 deep learning models:
  1. **MobileNetV2 (Best Model - 95.65%)**
  2. **VGG16 (82.61%)**
  3. **Custom CNN (34.78%)**
  4. **EfficientNetB0 (30.43%)**
- Confusion matrix heatmap and classification metrics breakdown.

### 🔬 AI Leaf Scanner & Image Analysis:
- Foliage photo upload drop zone (JPG, JPEG, PNG) & pre-loaded sample leaf selector.
- Automatic image preprocessing matching notebook training pipeline (`224x224` resolution, RGB channels, `1/255` float32 scaling).
- Real-time AI prediction returning disease category, confidence score, symptoms, causes, organic & chemical remedies, and prevention guidelines.

### 📋 Diagnostic Report Generator:
- Exports printable TXT diagnostic reports complete with sample info, prediction findings, confidence metrics, and recommended agricultural treatments.

### 👨‍💻 Developer Portfolio:
- Developer showcase featuring technical skills matrix, project highlights, GitHub, LinkedIn, and contact links.

---

## 🏆 Deep Learning Benchmark Summary

| Model Architecture | Model Type | Validation Accuracy | Precision | Recall | F1-Score | Status |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **MobileNetV2** | **Transfer Learning** | **95.65%** | **0.9620** | **0.9565** | **0.9565** | 🏆 **Best Model** |
| **VGG16** | Transfer Learning | 82.61% | 0.8247 | 0.8261 | 0.8230 | Benchmarked |
| **Custom CNN** | Baseline 3-Block CNN | 34.78% | 0.1210 | 0.3478 | 0.1795 | Baseline |
| **EfficientNetB0** | Transfer Learning | 30.43% | 0.0926 | 0.3043 | 0.1420 | Benchmarked |

---

## 📂 Project Structure

```
Rice-Leaf-Disease-Detection/
│
├── app.py                      # Main Streamlit application shell & sidebar navigation
├── requirements.txt            # Project Python dependencies
├── README.md                  # Complete application documentation
├── LINKEDIN_POST.md            # Social media showcase content
│
├── model/
│   └── Best_RiceLeaf_Disease_Model.keras  # Saved MobileNetV2 Keras model
│
├── assets/                    # Application visual graphics & media
│   ├── logo.png                # Brand logo
│   └── banner.png              # Executive Dashboard hero banner
│
├── samples/                    # Pre-loaded test foliage leaf images
│   ├── sample_bacterial_leaf_blight.jpg
│   ├── sample_brown_spot.jpg
│   └── sample_leaf_smut.jpg
│
├── pages/                      # Multi-page Streamlit application views
│   ├── 1_🏠_Home.py           # Executive Dashboard & Overview
│   ├── 2_🔬_Predict.py        # AI Leaf Scanner & Diagnostic Assistant
│   ├── 3_🌿_Disease_Info.py    # Agricultural Disease Reference Catalog
│   ├── 4_📊_Dashboard.py       # Performance Analytics & Benchmarks
│   ├── 5_ℹ️_About.py           # Technical Architecture & Workflow
│   └── 6_👨‍💻_Developer.py       # Developer Portfolio & Contact
│
└── utils/                      # Core backend utility modules
    ├── styles.py               # Shared Green Dark Glassmorphism CSS
    ├── preprocessing.py        # Image resizing (224x224) & float32 normalization
    ├── prediction.py           # Cached model loader & inference engine
    ├── disease_info.py         # Agricultural disease knowledge base & remedies
    └── charts.py               # Reusable Plotly visualizers
```

---

## 💻 Installation & Local Setup

### Prerequisites
- Python 3.10 or higher
- pip package manager

### 1. Clone or Navigate to Project Directory
```bash
git clone https://github.com/Sushameendra07/Rice-Leaf-Disease-Detection.git
cd Rice-Leaf-Disease-Detection
```

### 2. Install Required Dependencies
```bash
pip install -r requirements.txt
```

### 3. Launch the Application
```bash
streamlit run app.py
```

The application will open automatically in your browser at `http://localhost:8501`.

---

## 📄 License & Disclaimer
This application is developed strictly for educational, portfolio demonstration, and preliminary agricultural decision support purposes. It does not replace professional plant pathologist diagnosis in field settings.
