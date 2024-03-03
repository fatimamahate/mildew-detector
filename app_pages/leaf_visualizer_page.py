import streamlit as st
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.image import imread
import itertools
import random

def leaf_visualizer_page_body():
    st.header('Leaf Visualizer')
    st.info()
    version = 'v1'

    if st.checkbox('Check difference between mean and variability plots'):
        mean_var_healthy = plt.imread(f'outputs/{version}/avg_var_healthy.png')
        mean_var_powdery_mildew = plt.imread(f'outputs/{version}/avg_var_powdery_mildew.png')
        st.info()
        st.image(avg_var_healthy, caption='Mean and Variability of Healthy Leaves')
        st.image(mean_var_powdery_mildew,
        caption='Mean and Variability of Powdery Mildew Leaves')
        st.write('---')

    if st.checkbox('Check difference between average healthy and powdery mildew leaves'):
        diff_bet_avg = plt.imread(f'outputs/{version}/avg_diff.png')
        st.info()
        st.image(diff_bet_avg, caption='Difference between Average Images')
    
    if st.checkbox('Montage'):
        st.write('Click on "Create Montage"')
        st.info()
        my_data_dir = 'inputs/full_dataset_cherry-leaves'
        labels = os.listdir(my_data_dir+'/validation')
        label_to_disp = st.selectbox(
            label='Select a label:',
            options=labels,
            index=0
        )
        if st.button('Create Montage'):
            image_montage(
                dir_path=my_data_dir + '/validation',
                label_to_disp=label_to_disp,
                nrows=8,
                ncols=3,
                figsize=(10,25)
                )
        
        st.write('---')

def image_montage(dir_path, label_to_disp, nrows, ncols, figsize=(15,10)):
    sns.set_style('white')
    labels = os.listdir(dir_path)

    if label_to_disp in labels:
        image_list = os.listdir(dir_path +'/'+label_to_disp)
        if ncols * nrows < len(image_list):
            img_idx = random.sample(image_list, nrows * ncols)
        else:
            print('Too many---')
    
        row_list = range(0,nrows)
        col_list = range(0,ncols)
        plot_idx = list(itertools.product(row_list,col_list))

        fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize)
        for x in range(0, nrows * ncols):
            img = imread(f'{dir_path}/{label_to_disp}/{img_idx[x]}')
            img_shape = img.shape
            axes[plot_idx[x][0], plot_idx[x][1]].imshow(img)
            axes[plot_idx[x][0], plot_idx[x][1]].set_title(
                f'{img_shape[1]}px x {img_shape[0]}px'
            )
            axes[plot_idx[x][0], plot_idx[x][1]].set_xticks([])
            axes[plot_idx[x][0], plot_idx[x][1]].set_yticks([])
        plt.tight_layout()

        st.pyplot(fig=fig)
    else: 
        print('Error message here')


