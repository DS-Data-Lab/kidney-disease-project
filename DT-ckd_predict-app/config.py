# IMPORT LIB
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import streamlit as st

@st.cache_data()
def load_data():
    df = pd.read_csv('kidney_disease(cleaned).csv')

    x = df[["blood_pressure","specific_gravity","albumin","sugar","red_blood_cells","pus_cell","pus_cell_clumps",
            "bacteria","blood_glucose_random","blood_urea","serum_creatinine","sodium","potassium","haemoglobin",
            "packed_cell_volume","white_blood_cell_count","red_blood_cell_count","hypertension","diabetes_mellitus",
            "coronary_artery_disease","appetite","peda_edema","aanemia"]]

    y = df[['class']]

    return df, x, y

@st.cache_resource()
def train_model(x, y):
    model = DecisionTreeClassifier(
        ccp_alpha=0.0, class_weight=None, criterion='entropy',
        max_depth=4, max_features=None, max_leaf_nodes=None,
        min_impurity_decrease=0.0, min_samples_leaf=1,
        min_samples_split=2, min_weight_fraction_leaf=0.0,
        random_state=42, splitter='best'
    )

    model.fit(x, y)
    score = model.score(x, y)

    return model, score

def predict(x, y, features):
    model, score = train_model(x, y)
    prediction = model.predict(np.array(features).reshape(1,-1)) 
    return prediction, score
