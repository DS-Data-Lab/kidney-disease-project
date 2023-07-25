import streamlit as st
from config import predict

def app(df, x, y):

    st.title("Prediction Page")

    col1, col2, col3 = st.columns(3)
    
    # INPUT FIELD
    with col1:
        blood_pressure = st.text_input('Input blood pressure value')
    with col1:
        specific_gravity = st.text_input('Input specific gravity value')
    with col1:
        albumin = st.text_input('Input albumin value')
    with col1:
        sugar = st.text_input('Input sugar value')
    with col1:
        red_blood_cells = st.text_input('Input red blood cells value')
    with col1:
        pus_cell = st.text_input('Input push cell value')
    with col1:
        pus_cell_clumps = st.text_input('Input push cell clumps value')
    with col1:
        bacteria = st.text_input('Input bacteria value')
    with col2:
        blood_glucose_random = st.text_input('Input blood glucose random value')
    with col2:
        blood_urea = st.text_input('Input blood urea value')
    with col2:
        serum_creatinine = st.text_input('Input serum creatinine value')
    with col2:
        sodium = st.text_input('Input sodium value')
    with col2:
        potassium = st.text_input('Input pottasium value')
    with col2:
        haemoglobin = st.text_input('Input haemoglobin value')
    with col2:
        packed_cell_volume = st.text_input('Input packed cell volume value')
    with col2:
        white_blood_cell_count = st.text_input('Input white blood cell count value')
    with col3:
        red_blood_cell_count = st.text_input('Input red blood cell count value')
    with col3:
        hypertension = st.text_input('Input hypertension value')
    with col3:
        diabetes_mellitus = st.text_input('Input diabetes mellitus value')
    with col3:
        coronary_artery_disease = st.text_input('Input coronary artery disease value')
    with col3:
        appetite = st.text_input('Input appetite value')
    with col3:
        peda_edema = st.text_input('Input peda edema value')
    with col3:
        aanemia = st.text_input('Input aanemia value')

    # FEATURES INIT
    features = [blood_pressure,specific_gravity,albumin,sugar,red_blood_cells,pus_cell,
                pus_cell_clumps,bacteria,blood_glucose_random,blood_urea,serum_creatinine,
                sodium,potassium,haemoglobin,packed_cell_volume,white_blood_cell_count,
                red_blood_cell_count,hypertension,diabetes_mellitus,
                coronary_artery_disease,appetite,peda_edema,aanemia]

    # PREDICT BUTTON
    if st.button("Predict Now.. 🧰"):
        try:
            prediction, score = predict(x,y,features)
            score = score
            st.info("Prediction Success...")

            if (prediction == 1):
                st.warning("Data shows that this person is prone to kidney disease😥")
            else:
                st.success("The data shows that these people are relatively safe from kidney disease🥳")

            st.write(f"This model has accuracy {score*100}%")
        except:
            st.info("You have not entered any data or may looks like the data you entered is incomplete. Please enter data first... 😇")