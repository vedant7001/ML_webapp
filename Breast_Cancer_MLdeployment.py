# -*- coding: utf-8 -*-

import numpy as np
import pickle
import streamlit as st


# loading the saved model
loaded_model = pickle.load(open('C:/Users/VEDANT/Downloads/Breast_Cancer_deployment/Breastcancer_model.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    selected = st.selectbox('Cancer Prediction System',
                            ['Breast Cancer Prediction'],
                            index=0)

# Breast Cancer Prediction Page
if selected == 'Breast Cancer Prediction':

    # page title
    st.title('Breast Cancer Prediction using ML')


    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
         radius_mean = st.text_input('mean radius')

    with col2:
         texture_mean = st.text_input('Mean Texture')

    with col3:
         perimeter_mean  = st.text_input('Mean Perimeter')

    with col1:
         area_mean = st.text_input('Mean Area')

    with col2:
        smoothness_mean = st.text_input('Mean Smoothness')

    with col3:
         compactness_mean = st.text_input('Mean Compactness')
        
    with col1:
         concavity_mean = st.text_input('Mean Concativiy')

    with col2:
        concavepoints_mean = st.text_input('Mean Concave points')

    with col3:
        symmetry_mean = st.text_input('Mean Symmetry')

    with col1:
         fractal_dimension_mean = st.text_input('Mean Fractal Dimension')

    with col2:
        radius_se = st.text_input('Radius Error')
        
    with col3:
          texture_se = st.text_input('Texture Error')
    
    with col1:
        perimeter_se = st.text_input('Perimeter Error')

    with col2:
        area_se = st.text_input('Area Error')
        
    with col3:
       smoothness_se = st.text_input('Smoothness Error')
       
    with col1:
        compactness_se = st.text_input('Compactness Error')

    with col2:
        concavity_se = st.text_input('Concativity Error')
         
    with col3:
        concavepoints_se = st.text_input('Concave points error')
     
    with col1:
         symmetry_se = st.text_input('Symmetry Error')

    with col2:
        fractal_dimension_se = st.text_input('Fractal Dimension error')
          
    with col3:
         radius_worst = st.text_input('Worst Radius')
       
    with col1:
         texture_worst  = st.text_input('Worst Texture')

    with col2:
        perimeter_worst = st.text_input('Worst Perimeter')
          
    with col3:
         area_worst  = st.text_input('Worst Area')
       
    with col1:
          smoothness_worst  = st.text_input('Worst Smoothness')

    with col2:
         compactness_worst = st.text_input('Worst Compactness')
             
    with col3:
          concavity_worst = st.text_input('Worst Concavity')
         
    with col1:
           concavepoints_worst = st.text_input('Worst Concave Points')

    with col2:
         symmetry_worst = st.text_input('Worst Symmetry')
             
    with col3:
          fractal_dimension_worst  = st.text_input('Worst fractal dimension')

    # code for Prediction
    diagnosis = ''

    # creating a button for Prediction

    if st.button('Breast Cancer Test Result'):
        try:
            input_data = np.array([[radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean,
                                    concavity_mean, concavepoints_mean, symmetry_mean, fractal_dimension_mean, radius_se,
                                    texture_se, perimeter_se, area_se, smoothness_se, compactness_se, concavity_se,
                                    concavepoints_se, symmetry_se, fractal_dimension_se, radius_worst, texture_worst,
                                    perimeter_worst, area_worst, smoothness_worst, compactness_worst, concavity_worst,
                                    concavepoints_worst, symmetry_worst, fractal_dimension_worst]]).astype(float)

            prediction = loaded_model.predict(input_data)

            if prediction[0] == 1:
                diagnosis = 'Cancer is Malignant'
            else:
                diagnosis = 'Cancer is Benign'
        except Exception as e:
            st.error(f"Error in prediction: {e}")

    st.success(diagnosis)

