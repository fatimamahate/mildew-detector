import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd
from src.data_management import download_dataframe_as_csv
from src.machine_learning.predictive_analytics import (
    load_model_and_predict,
    resize_input_image,
    plot_pred_prob
)

def mildew_detection_page_body():
    """
    Function to upload images to make a prediction
    """
    st.header('Mildew Detection')
    st.info(
        f'Business Requirement 2 - The client is interested in '
        f'predicting if a cherry leaf is healthy or contains '
        f'powdery mildew.'
    )
    st.write('---')
    st.info(
        f'You can download the images from '
        f'[Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves).'
    )
    st.write('---')
    st.info(
        f'Upload an image of a cherry leaf for predictions (more than one is permitted).'
    )
    img_buffer=st.file_uploader(' ', type=['png', 'jpg'], accept_multiple_files=True)
    button_for_pred = st.button('Predict!')

    if button_for_pred:
        make_pred(img_buffer)

def make_pred(img_buffer):
    """
    Function to make a prediction on uploaded image
    """
    if img_buffer is not None:
        df_report = pd.DataFrame([])
        for img in img_buffer:
            img_pil = (Image.open(img))
            st.info(f'Cherry Leaf: **{img.name}**')
            img_array = np.array(img_pil)
            st.image(
                img_pil,
                caption=f'Image Size (width x height): {img_array.shape[1]}px x {img_array.shape[0]}px'
            ) 
            version = 'v1'
            resized_img=resize_input_image(img=img_pil, version=version)
            pred_prob, pred_class = load_model_and_predict(resized_img,version=version)
            plot_pred_prob(pred_prob=pred_prob, pred_class=pred_class)
            df_report=df_report.append(
                {
                    'Name':img.name,
                    'Result': pred_class
                },
                ignore_index=True
            )
    if not df_report.empty:
        st.success('Analysis Report')
        st.table(df_report)
        st.markdown(
            download_dataframe_as_csv(df_report),
            unsafe_allow_html=True
        )  