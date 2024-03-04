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
    st.header('Mildew Detection')
    st.info(
        f'Business Requirement 2 - The client is interested in '
        f'predicting if a cherry leaf is healthy or contains '
        f'powdery mildew.'
    )
    st.write('---')
    st.info(
        f'You can download the images from '
        f'[Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves)'
    )
    st.write('---')
    st.info(
        f'Upload an image of a cherry leaf for predictions (more than one is permitted)'
    )
    