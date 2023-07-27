import streamlit as st
from PIL import Image
from pathlib import Path

def app():
    banner_img = Image.open(Path(__file__).parents[1] / 'src/img/banner.jpg')
    banner1_img = Image.open(Path(__file__).parents[1] / 'src/img/bnr1.jpg')
    banner2_img = Image.open(Path(__file__).parents[1] / 'src/img/bnr2.png')

    st.title("Kidney Disease Prediction Test Application")
    st.image(banner1_img)
    st.subheader("What Is Chronic Kidney Disease?")
    st.markdown("Chronic kidney disease (CKD) means your kidneys are damaged and can’t filter blood the way they should. The main risk factors for developing kidney disease are diabetes, high blood pressure, heart disease, and a family history of kidney failure.")
    st.subheader("Causes of Chronic Kidney Disease")
    st.markdown("Diabetes and high blood pressure are the most common causes of kidney disease. Your health care provider may do tests to find out why you have kidney disease. The cause of your kidney disease may affect the type of treatment you receive.")
    st.image(banner2_img, caption="Cycle of Chronic Kidney Disease😖")
    st.subheader("Tests & Diagnosis")
    st.markdown("Testing may be the only way to know if you have kidney disease. Get checked if you have diabetes, high blood pressure, heart disease, or a family history of kidney failure. The sooner you know you have kidney disease, the sooner you can get treatment.")
    st.subheader("Managing Chronic Kidney Disease")
    st.markdown("You can take steps to protect your kidneys. The most important step you can take to treat kidney disease is to control your blood pressure. Healthy habits can also help you manage your kidney disease.")
    st.subheader("Eating Right for Chronic Kidney Disease")
    st.markdown("Eating the right foods can help keep your kidney disease from getting worse. Work with a dietitian to create a meal plan that includes foods that you enjoy eating while maintaining your kidney health.")
    st.subheader("Preventing Chronic Kidney Disease")
    st.markdown("You are at risk for kidney disease if you have diabetes, high blood pressure, heart disease, or a family history of kidney failure. If you have risk factors, get tested for kidney disease and protect your kidneys by making healthy food choices, being more active, aiming for a healthy weight, and managing health conditions that cause kidney damage.")
    st.subheader("What if My Kidneys Fail?")
    st.markdown("Kidney failure means that your kidneys have lost most of their ability to function. Work with your health care team and family to consider your options to replace your lost kidney function, such as dialysis or transplant. Choose a treatment that is right for you.")
    st.image(banner_img)
    st.subheader("Clinical Trials")
    st.markdown("The National Institute of Diabetes and Digestive and Kidney Diseases (NIDDK) and other components of the National Institutes of Health (NIH) conduct and support research into many diseases and conditions.")
  

