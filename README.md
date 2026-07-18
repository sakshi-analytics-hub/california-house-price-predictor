```markdown
# 🏠 California House Price Predictor

A machine learning web app that predicts California house prices using a **Linear Regression** model, built with **scikit-learn** and deployed as an interactive web application using **Streamlit**.

🔗 **Live App:** [california-house-price-predictor-2026.streamlit.app](https://california-house-price-predictor-2026.streamlit.app)

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.59.2-red)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.7.2-orange)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📌 Overview

This project uses the **California Housing dataset** to train a Linear Regression model that predicts median house values based on features like income, location, and housing characteristics. The trained model is deployed as a live, interactive web app where users can adjust input values using sliders and instantly see a predicted house price.

---

## ✨ Features

- 🎚️ Interactive sliders for 8 input features
- ⚡ Real-time price prediction on button click
- 📊 Built on a trained Linear Regression model with StandardScaler preprocessing
- 🌐 Fully deployed and publicly accessible — no installation required
- 🎨 Clean, responsive Streamlit UI with dark mode support

---

## 🧠 How It Works

1. User adjusts sliders for housing/location features
2. Inputs are scaled using a pre-fitted `StandardScaler`
3. Scaled inputs are passed to a trained `LinearRegression` model
4. Model outputs a predicted price, displayed instantly on screen

---

## 📥 Input Features

| Feature | Description | Range |
|---|---|---|
| Median Income | Median income in the block (in $10,000s) | 0.5 – 15.0 |
| House Age | Median age of houses in the block | 1 – 52 years |
| Average Rooms | Average number of rooms per household | 1 – 15 |
| Average Bedrooms | Average number of bedrooms per household | 0.3 – 5.0 |
| Population | Block population | 3 – 5000 |
| Average Occupancy | Average household occupancy | 0.5 – 10.0 |
| Latitude | Geographic latitude | 32.5 – 42.0 |
| Longitude | Geographic longitude | -124.5 – -114.0 |

**Output:** Predicted median house value (in USD)

---

## 🛠️ Tech Stack

- **Python 3.12**
- **Streamlit** – web app framework
- **scikit-learn** – model training (Linear Regression + StandardScaler)
- **NumPy** – numerical operations
- **Joblib** – model serialization/loading

---

## 📁 Project Structure

```
house-price-app/
├── app.py                        # Streamlit web app
├── house_price_model.pkl         # Trained model + scaler (serialized with joblib)
├── requirements.txt              # Python dependencies
├── Linear_Regression_Project.ipynb  # Model training & exploration notebook
└── README.md                     # Project documentation
```

---

## 🚀 Run Locally

**1. Clone the repository**
```bash
git clone https://github.com/sakshi-analytics-hub/house-price-app.git
cd house-price-app
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the app**
```bash
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`.

---

## 🌐 Deployment

This app is deployed on **Streamlit Community Cloud**, connected directly to this GitHub repository. Any changes pushed to the `main` branch are automatically redeployed.

To deploy your own copy:
1. Fork/clone this repo
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub account
4. Select this repo, branch `main`, and `app.py` as the main file
5. Click **Deploy**

---

## 📓 Model Training

The model was trained in `Linear_Regression_Project.ipynb` using the California Housing dataset. The trained `LinearRegression` model and the fitted `StandardScaler` were both saved together into a single file (`house_price_model.pkl`) using `joblib`, so the app can load and use them directly for inference.

---

## 🔮 Future Improvements

- [ ] Add a map view to visualize predictions by location
- [ ] Display feature importance / coefficients
- [ ] Try more advanced models (Random Forest, XGBoost) and compare performance
- [ ] Add input validation and error handling
- [ ] Add unit tests

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙋‍♀️ Author

**Sakshi**
🔗 [Live Demo](https://california-house-price-predictor-2026.streamlit.app) · [GitHub](https://github.com/sakshi-analytics-hub)

---

⭐ If you found this project useful, consider giving it a star on GitHub!
```

