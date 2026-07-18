# 🏠 California House Price Predictor

A simple **Machine Learning web app** built with **Streamlit** that predicts the median house value in a California district using a **Linear Regression** model.

🔗 **Live Demo:** _(add your Streamlit Cloud link here after deployment)_

---

## 📌 Overview

This project uses the **California Housing dataset** (built into scikit-learn) to train a Linear Regression model that predicts `MedHouseVal` (median house value) based on 8 input features. The trained model is deployed as an interactive web app using Streamlit.

## 🚀 Features

- Interactive sliders to input housing/location details
- Real-time price prediction on button click
- Clean, simple UI built with Streamlit
- Model trained with `StandardScaler` for feature scaling

## 🧠 Model Details

- **Algorithm:** Linear Regression (scikit-learn)
- **Dataset:** California Housing Dataset (20,640 rows, 8 features)
- **Preprocessing:** Missing value handling, feature scaling with `StandardScaler`
- **Evaluation Metrics:** MAE, MSE, RMSE, R²

### Input Features

| Feature | Description |
|---|---|
| MedInc | Median income in block group (in 10k $) |
| HouseAge | Median house age in block group |
| AveRooms | Average number of rooms per household |
| AveBedrms | Average number of bedrooms per household |
| Population | Block group population |
| AveOccup | Average number of household members |
| Latitude | Block group latitude |
| Longitude | Block group longitude |

## 📁 Project Structure

```
california-house-price-predictor/
├── app.py                          # Streamlit web app
├── Linear_Regression_Project.ipynb # Model training notebook
├── house_price_model.pkl           # Trained model + scaler
├── requirements.txt                # Python dependencies
└── README.md
```

## 🛠️ Installation & Local Setup

1. Clone the repository
   ```bash
   git clone https://github.com/<your-username>/california-house-price-predictor.git
   cd california-house-price-predictor
   ```

2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app
   ```bash
   python -m streamlit run app.py
   ```

4. Open [http://localhost:8501](http://localhost:8501) in your browser.

## ☁️ Deployment

This app is deployed using [Streamlit Community Cloud](https://share.streamlit.io). To deploy your own copy:

1. Push this repo to your GitHub account
2. Go to [share.streamlit.io](https://share.streamlit.io) and sign in with GitHub
3. Click **New app**, select this repo, branch `main`, and file `app.py`
4. Click **Deploy**

## 📦 Tech Stack

- Python
- scikit-learn
- Streamlit
- NumPy
- Joblib

## 📈 Future Improvements

- Try other models (Random Forest, Gradient Boosting) and compare performance
- Hyperparameter tuning with `GridSearchCV`
- Add feature engineering for improved accuracy
- Add data visualizations (e.g. prediction confidence, feature importance) to the app

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
