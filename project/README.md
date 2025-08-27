 # Stock Price Modeling and Risk Assessment

## Project Overview
This project applies a full data science lifecycle to financial market data, with the goal of modeling stock prices and evaluating risks.  
Using data pulled from the Alpha Vantage API, we performed exploratory data analysis, feature engineering, linear regression and classification models, and risk-aware evaluation. The results were packaged into a stakeholder-ready deliverable.  

The project was developed as part of a structured bootcamp workflow, with each stage aligning to industry-standard data science practices.  



---

## Workflow

1. **Data Acquisition**  
   - API pull from Alpha Vantage (`TIME_SERIES_DAILY`)  
   - Saved to `project/data/raw/`  

2. **Exploratory Data Analysis (EDA)**  
   - Time series plots of closing price and volume  
   - Distribution of returns, outlier detection  
   - Summary statistics including skewness and kurtosis  

3. **Feature Engineering**  
   - Daily returns  
   - Rolling means and volatility measures  
   - Lag features for time-dependency  

4. **Modeling**  
   - Regression (Linear Regression): Predict next day’s close  
   - Classification (Logistic Regression): Predict up vs. down movement  
   - Performance evaluated with RMSE and R² (regression) and precision/recall (classification)  

5. **Risk and Assumptions Analysis**  
   - Parametric vs. Bootstrap confidence intervals  
   - Scenario sensitivity (mean vs. median imputation)  
   - Subgroup diagnostic (residuals by segment)  

6. **Stakeholder Report**  
   - Final deliverable with assumptions, risks, and business implications.  

---

## Key Results
- Regression R² ≈ 0.63 on engineered features (moderate predictive power).  
- Classification accuracy ~0.44, highlighting difficulty in predicting short-term price direction.  
- Bootstrap confidence intervals confirmed stability against sampling variability, but sensitivity analysis showed model fragility under different imputation assumptions.  
- Stakeholder report emphasizes caution in over-relying on linear models for financial time series and suggests exploring more advanced models (ARIMA, LSTMs).  

---

## Assumptions and Risks
- Assumed linear relationships between engineered features and target.  
- Missing values imputed via mean/median; could bias under volatile regimes.  
- Past performance may not generalize during structural breaks or unexpected shocks.  

---

## Next Steps
- Extend to non-linear models (tree-based methods, LSTMs).  
- Incorporate additional market indicators (macro data, options activity).  
- Deploy an interactive dashboard for monitoring predictions.  

---

## Requirements
Install dependencies with:

```bash
pip install -r requirements.txt


