import streamlit as st
import pickle
import json
import pandas as pd
import numpy as np
from PIL import Image

with open('./src/best_svm_pipeline_final.pkl', 'rb') as file_1:
    best_svm_model = pickle.load(file_1)

def run():

    # Membuat title
    st.title('Early Detection of Depression')
    
    image = Image.open('./src/image2.jpg')
    st.image(image, caption="It's Okay to Not Be Okay.")

    # Pembuatan Form
    with st.form(key='student-depression-awareness'): # Nama form aja 
        id = st.number_input('ID', min_value=1, max_value=999, value=1) # Value, artinya default valuenya mau dikosongkan juga silahkan
        gender = st.radio('Gender', ('Male', 'Female'), index=0)
        age = st.number_input('Age', min_value=17, max_value=99, value=17)
        city = st.text_input('City', value='--Origin--')
        profession = st.text_input('Profession', value='--Student--')
        academic_pressure = st.number_input('Academic Pressure', min_value=1, max_value=5, value=1)
        work_pressure = st.number_input('Work Pressure', min_value=1, max_value=5, value=1)
        cgpa = st.number_input('Cumulative Grade Point Average', min_value=3.0, max_value=10.0, value=3.0, step=0.1)
        study_satsifaction = st.number_input('Study Satisfaction', min_value=1, max_value=5, value=1)
        job_satisfaction = st.number_input('Job Satisfaction', min_value=1, max_value=5, value=1)
        sleep_duration = st.radio('Sleep Duration', ('Less than 5 hours', '5-6 hours', '7-8 hours', 'More than 8 hours'), index=2)
        dietary_habits = st.radio('Dietary Habits', ('Unhealthy', 'Moderate', 'Healthy'), index=1)
        degree = st.text_input('Degree', value='--Bachelor--')
        suicidal_thoughts = st.radio('Have you ever had suicidal thoughts ?', ('Yes', 'No'), index= 1)
        work_study_hours = st.number_input('Work/Study Horus', min_value=1, max_value=12, value=1)
        financial_stress = st.number_input('Financial Stress', min_value=1, max_value=5, value=1)
        fam_his_mental = st.radio('Family History of Mental Illness', ('Yes', 'No'), index= 1)

        st.subheader('Kondisi : 1 Depressed, 0 Not Depressed')

        # Membuat button, kalo gaada submit button pasti error
        submitted = st.form_submit_button('Predict')

   
    # Create New Data
        
    data_inf = {
    'id' : id,
    'gender' : gender,
    'age' : age,
    'city' : city,
    'profession' : profession,
    'academic_pressure' : academic_pressure,
    'work_pressure' : work_pressure,
    'cgpa' : cgpa,
    'study_satisfaction' : study_satsifaction,
    'job_satisfaction' : job_satisfaction,
    'sleep_duration' : sleep_duration,
    'dietary_habits' : dietary_habits,
    'degree' : degree,
    'suicidal_thoughts' : suicidal_thoughts,
    'work/study_hours' : work_study_hours,
    'financial_stress' : financial_stress,
    'fam_hist_mental_illness' : fam_his_mental,
}
    # yang kanan disamakan dengan nama variabelnya kalo yang kiri samakan dengan original columnnya 
    data_inf = pd.DataFrame([data_inf])
    data_inf

    # Tinggal copas codingan split,concate, scaling dll
    if submitted:
        # Prediksi
        prediction = best_svm_model.predict(data_inf)
        st.write('# Prediksi Kesehatan Mental Student adalah :', str(int(prediction)))


if __name__== '__main__':
    run()