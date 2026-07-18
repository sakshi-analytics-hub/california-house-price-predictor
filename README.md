
```markdown
<div align="center">

# 🏠 California House Price Predictor

### An End-to-End Machine Learning Web Application

A production-ready Linear Regression model deployed as an interactive web application, predicting median house prices in California based on demographic and geographic features.

[![Live App](https://img.shields.io/badge/🌐_Live_App-Visit_Now-success?style=for-the-badge)](https://california-house-price-predictor-2026.streamlit.app)
[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.59.2-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.7.2-F7931E?style=flat&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

[**🚀 Live Demo**](https://california-house-price-predictor-2026.streamlit.app) · [**🐛 Report Bug**](../../issues) · [**✨ Request Feature**](../../issues)

</div>

---

## 📑 Table of Contents

1. [Overview](#-overview)
2. [Demo](#-demo)
3. [Key Features](#-key-features)
4. [Tech Stack](#-tech-stack)
5. [Dataset](#-dataset)
6. [Methodology](#-methodology)
7. [Input Parameters](#-input-parameters)
8. [Project Structure](#-project-structure)
9. [Installation & Setup](#-installation--setup)
10. [Usage](#-usage)
11. [Deployment](#-deployment)
12. [Model Performance](#-model-performance)
13. [Roadmap](#-roadmap)
14. [Contributing](#-contributing)
15. [License](#-license)
16. [Contact](#-contact)
17. [Acknowledgments](#-acknowledgments)

---

## 📌 Overview

The **California House Price Predictor** is a machine learning web application that estimates median house values across California districts. Built using a **Linear Regression** model trained on the well-known **California Housing dataset**, the application provides an intuitive, slider-based interface for real-time price predictions.

This project demonstrates a complete ML workflow — from **data exploration and preprocessing**, through **model training and evaluation**, to **deployment** as a live, publicly accessible web application.

---

## 🎬 Demo

🔗 **Try it live:** [california-house-price-predictor-2026.streamlit.app](https://california-house-price-predictor-2026.streamlit.app)

> Adjust the sliders in the sidebar to input housing characteristics, then click **Predict** to instantly view the estimated median house value.

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 🎚️ **Interactive UI** | Real-time sliders for all 8 input features |
| ⚡ **Instant Predictions** | Get predictions in milliseconds on button click |
| 📊 **Trained ML Pipeline** | Linear Regression model with StandardScaler preprocessing |
| 🌐 **Publicly Deployed** | No installation required — accessible from any browser |
| 🎨 **Responsive Design** | Clean UI with light/dark mode support |
| 🔄 **Auto-Redeploy** | Connected to GitHub for continuous deployment |

---

## 🛠️ Tech Stack

**Language & Core Libraries**

| Category | Technology |
|---|---|
| Programming Language | Python 3.12 |
| Web Framework | Streamlit |
| Machine Learning | scikit-learn |
| Numerical Computing | NumPy |
| Model Serialization | Joblib |
| Deployment Platform | Streamlit Community Cloud |
| Version Control | Git & GitHub |

---

## 📊 Dataset

This project uses the **California Housing dataset**, derived from the 1990 U.S. Census. It contains information collected from various California districts, including:

- Median income
- Housing age
- Room and bedroom averages
- Population and occupancy statistics
- Geographic coordinates (latitude/longitude)
- Median house value (target variable)

---

## 🧠 Methodology

The end-to-end machine learning workflow followed in this project:

```
1. Data Loading & Exploration
        ↓
2. Data Preprocessing (Feature Scaling using StandardScaler)
        ↓
3. Train-Test Split
        ↓
4. Model Training (Linear Regression)
        ↓
5. Model Evaluation
        ↓
6. Model Serialization (joblib — model + scaler bundled together)
        ↓
7. Web App Development (Streamlit)
        ↓
8. Deployment (Streamlit Community Cloud)
```

Full implementation details are available in [`Linear_Regression_Project.ipynb`](./Linear_Regression_Project.ipynb).

---

## 📥 Input Parameters

| # | Feature | Description | Min | Max | Default |
|---|---|---|---|---|---|
| 1 | Median Income | Median income of the district (in $10,000s) | 0.5 | 15.0 | 3.87 |
| 2 | House Age | Median age of houses in the district | 1 | 52 | 28.6 |
| 3 | Average Rooms | Average number of rooms per household | 1 | 15 | 5.4 |
| 4 | Average Bedrooms | Average number of bedrooms per household | 0.3 | 5.0 | 1.1 |
| 5 | Population | Total district population | 3 | 5000 | 1425 |
| 6 | Average Occupancy | Average household occupancy | 0.5 | 10.0 | 3.0 |
| 7 | Latitude | Geographic latitude of the district | 32.5 | 42.0 | 35.6 |
| 8 | Longitude | Geographic longitude of the district | -124.5 | -114.0 | -119.5 |

**Output:** Predicted median house value (USD)

---

## 📁 Project Structure

```
house-price-app/
│
├── app.py                             # Main Streamlit application
├── house_price_model.pkl              # Serialized model + scaler (joblib)
├── requirements.txt                   # Project dependencies
├── Linear_Regression_Project.ipynb    # Model training & EDA notebook
├── README.md                          # Project documentation
└── LICENSE                            # License file
```

---

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.9 or higher
- pip package manager

### Steps

**1. Clone the repository**
```bash
git clone https://github.com/sakshi-analytics-hub/house-price-app.git
cd house-price-app
```

**2. Create a virtual environment (recommended)**
```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Run the application**
```bash
streamlit run app.py
```

The app will launch automatically at `http://localhost:8501`.

---

## ▶️ Usage

1. Launch the app (locally or via the live link)
2. Use the sidebar sliders to input district characteristics
3. Click the **Predict** button
4. View the predicted median house value displayed instantly

---

## 🚀 Deployment

This application is deployed using **Streamlit Community Cloud**, with continuous deployment configured directly from this GitHub repository. Any updates pushed to the `main` branch are automatically reflected in the live app.

### Deploy Your Own Copy

1. Fork this repository
2. Visit [share.streamlit.io](https://share.streamlit.io)
3. Sign in with GitHub
4. Click **New app** and select this repository
5. Set the main file path to `app.py`
6. Click **Deploy**

---

## 📈 Model Performance

> Metrics recorded during training (see notebook for full evaluation):

| Metric | Value |
|---|---|
| Model Type | Linear Regression |
| Preprocessing | StandardScaler |
| Dataset | California Housing (1990 Census) |

*(Add your actual R², MAE, or RMSE scores here from your notebook for a more complete picture.)*

---

## 🗺️ Roadmap

- [ ] Add geographic map visualization for predictions
- [ ] Display feature importance / model coefficients
- [ ] Benchmark against advanced models (Random Forest, XGBoost, Gradient Boosting)
- [ ] Add input validation and error handling
- [ ] Add unit and integration tests
- [ ] Add CI/CD pipeline for automated testing

---

## 🤝 Contributing

Contributions are welcome and appreciated!

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 📬 Contact

**Sakshi**

- GitHub: [@sakshi-analytics-hub](https://github.com/sakshi-analytics-hub)
- Live App: [california-house-price-predictor-2026.streamlit.app](https://california-house-price-predictor-2026.streamlit.app)

---

## 🙏 Acknowledgments

- [California Housing Dataset](https://scikit-learn.org/stable/datasets/real_world.html#california-housing-dataset) — scikit-learn
- [Streamlit Documentation](https://docs.streamlit.io/)
- [scikit-learn Documentation](https://scikit-learn.org/stable/documentation.html)

---

<div align="center">

**⭐ If you found this project useful, consider giving it a star!**

</div>
```

