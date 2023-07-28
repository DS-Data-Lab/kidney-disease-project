import streamlit as st
from config import *
from sklearn.metrics import mean_squared_error, accuracy_score, classification_report, mean_absolute_error
from sklearn.model_selection import train_test_split

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
        red_blood_cells = st.selectbox('Input red blood cells value', ('0 - abnormal', '1 - normal'))
    with col1:
        pus_cell = st.selectbox('Input push cell value', ('0 - abnormal', '1 - normal'))
    with col1:
        pus_cell_clumps = st.selectbox('Input push cell clumps value', ('0 - notpresent', '1 - present'))
    with col1:
        bacteria = st.selectbox('Input bacteria value', ('0 - notpresent', '1 - present'))
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
        hypertension = st.selectbox('Input hypertension value', ('0 - no', '1 - yes'))
    with col3:
        diabetes_mellitus = st.selectbox('Input diabetes mellitus value', ('3 - no', '4 - yes'))
    with col3:
        coronary_artery_disease = st.selectbox('Input coronary artery disease value', ('1 - no', '2 - yes'))
    with col3:
        appetite = st.selectbox('Input appetite value', ('0 - good', '1 - poor'))
    with col3:
        peda_edema = st.selectbox('Input peda edema value', ('0 - no', '1 - yes'))
    with col3:
        aanemia = st.selectbox('Input aanemia value', ('0 - no', '1 - yes'))

    # FEATURES INIT
    features = [blood_pressure,specific_gravity,albumin,sugar,red_blood_cells[0],pus_cell[0],
                pus_cell_clumps[0],bacteria[0],blood_glucose_random,blood_urea,serum_creatinine,
                sodium,potassium,haemoglobin,packed_cell_volume,white_blood_cell_count,
                red_blood_cell_count,hypertension[0],diabetes_mellitus[0],
                coronary_artery_disease[0],appetite[0],peda_edema[0],aanemia[0]]
    
    # PREDICT BUTTON
    if st.button("Start Diagnostics.. 🧰"):
        try:
            prediction, model = predict(x,y,features)
            st.info("Diagnostics Success...")
            x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
            y_pred = model.predict(x_test)
            if (prediction == 1):
                st.warning("Data shows that this person is prone to kidney disease😥")
            else:
                st.success("The data shows that these people are relatively safe from kidney disease🥳")
            print(f"{y_test}")
            # print(f"{y_pred}")
            print(f"{features}")
            st.write(f"Accuracy Score: {accuracy_score(y_test, y_pred)*100}%")
            st.write(f"MAE: {mean_absolute_error(y_test, y_pred)*100}%")
            st.write(f"MSE: {mean_squared_error(y_test, y_pred)*100}%")
            # st.write(f"CR:\n{classification_report(y_test, y_pred)}")
        except:
            st.info("You have not entered any data or may looks like the data you entered is incomplete. Please enter data first... 😇")
