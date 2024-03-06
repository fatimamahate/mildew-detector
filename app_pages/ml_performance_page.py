import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.image import imread
from src.machine_learning.evaluate_clf import load_test_evaluation

def ml_performance_page_metrics():
    """
    Function to show ML performance metrics (such as accuracy and losses)
    """
    st.header('Machine Learning (ML) Performance Metrics')
    version='v1'
    st.write('Train, Validation and Test Set: Frequencies')
    labels_dist = plt.imread(
        f'outputs/{version}/labels_distribution.png'
    )
    st.image(
        labels_dist,
        caption='Train, Validation & Test Sets - Labels Distribution'
        )
    st.info(
        f'* Train Set - 1472 images for each class  \n'
        f'* Validation Set - 210 images for each class  \n'
        f'* Test Set - 422 images for each class'

    )
    st.write('---')

    st.write('Model History')
    col1,col2=st.beta_columns(2)
    with col1:
        model_acc = plt.imread(
            f'outputs/{version}/model_training_accuracy.png'
        )
        st.image(
        model_acc,
        caption='Model Training Accuracy'        
        )
    with col2:
        model_loss = plt.imread(
            f'outputs/{version}/model_training_losses.png'
        )
        st.image(
        model_loss,
        caption='Model Training Losses'        
        )
    st.info(
        f'These plots show the accuracy and losses of model as '
        f'it is being trained. It is a normal curve and is not '
        f'overfitted and underfitted.  \n'
    )
    st.write('---')

    st.write('Generalised Performance on Test Set')
    st.dataframe(
        pd.DataFrame(
            load_test_evaluation(
                version=version
                ),
            index=['Loss', 'Accuracy']
            )
        )
    st.success('The model has accuracy of 99.53%')
    load_test_evaluation(version=version)
    

