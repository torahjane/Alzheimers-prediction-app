# Alzheimer's Prediction App
An interactive machine learning web app built using Streamlit to predict the likelihood of Alzheimer’s disease based on clinical features.

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://alzheimers-prediction-app-arqjusf3atpwl3y89p4eqs.streamlit.app/)

## Try it Live

 **[Click here to open the app](https://alzheimers-prediction-app-arqjusf3atpwl3y89p4eqs.streamlit.app/)**  
No installation needed. Just open and interact!

##  What the App Does
This app uses a trained **XGBoost** model to predict Alzheimer's Disease based on key features. It uses **binarized values** (0 or 1) for the following clinical parameters:

###  Parameters Used
- `Age_binary`  
  - 0 = Age ≤ Threshold  
  - 1 = Age > Threshold  
- `SES_binary` (Socioeconomic Status)  
  - 0 = Lower or equal to median SES  
  - 1 = Higher than median SES  
- `CDR_binary` (Clinical Dementia Rating)  
  - 0 = CDR ≤ 0.5 (Normal or very mild dementia)  
  - 1 = CDR > 0.5 (Indicates dementia symptoms)  
- `nWBV_binary` (Normalized Whole Brain Volume)  
  - 0 = Larger brain volume  
  - 1 = Smaller brain volume  
- `EDUC_binary` (Years of Education)  
  - 0 = Lower or equal education level  
  - 1 = Higher education level  
- `MMSE_binary` (Mini-Mental State Examination)  
  - 0 = Higher cognitive score  
  - 1 = Lower cognitive score  
Each input value (0 or 1) is based on thresholds determined during training and preprocessing.

## Project Structure
- `app.py` - Main Streamlit app script.
- `models/` - Contains the trained model file.
- `data/` - Dataset used for training and testing.
- `notebook/` - Jupyter notebook files for model training and exploration.
- `requirements.txt` - Python dependencies required to run the app.

## Future Improvements
Add human-readable form inputs instead of 0/1
Explain thresholds to the user
Add visualizations and charts for insights
Deploy with a custom domain
Add documentation and model explainability (e.g., SHAP)

## Contact
Developed by Torah — reach out for questions or collaborations!




