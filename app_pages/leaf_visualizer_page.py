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
    st.info(
        f'View the images and the differences between '
        f'the healthy and powdery mildew leaves.'
    )

    version = 'v1'

    if st.checkbox('Check difference between mean and variability plots'):
        mean_var_healthy = plt.imread(f'outputs/{version}/avg_var_healthy.png')
        mean_var_powdery_mildew = plt.imread(f'outputs/{version}/avg_var_powdery_mildew.png')
        st.info(
            f'As can be seen, the mean and variability images have '
            f'subtle differences between the healthy and powdery leaves. '
            f'The powdery leaf mean plot has a green color that is speckled '
            f'with white color. This can show the powdery mildew. Similarly, '
            f'the variability plot has purple color that is speckled. '
            f'The healthy leaf mean plot has green colour that is entirely green. '
            f'There are not any speckled white parts. Similarly, the respective '
            f'varibility plot has purple colour that is entirely purple.'
            f'The shapes of each respective plots are similar so there are '
            f'no patterns to clearly differentiate between healthy and powdery leaves.'
        )

        st.image(mean_var_healthy, caption='Mean and Variability of Healthy Leaves')
        st.image(mean_var_powdery_mildew,
        caption='Mean and Variability of Powdery Mildew Leaves')
        st.write('---')

    if st.checkbox('Check difference between average healthy and powdery mildew leaves'):
        diff_bet_avg = plt.imread(f'outputs/{version}/avg_diff.png')
        st.info(
            f'The average plots of the healthy and powdery leaves show that '
            f'there are white speckles on the powdery mildew plot as opposed '
            f'to the healthy plot which has a more homogeneous color. However, it is '
            f'difficult to differentiate between the plots since they have '
            f'similar patterns.' 
        )
        st.image(diff_bet_avg, caption='Difference between Average Images')
    
    if st.checkbox('Montage'):
        st.write('Choose a class and then click on "Create Montage" to see images of that class')
        st.info(
            f'The montage shows a selection of healthy and powdery mildew '
            f'leaves. This helps to differentiate between each leaf visually. \n'
            f'The powdery mildew leaves have white speckles on the leaf '
            f'as well as some distorted edges (as expected by infected leaves). '
            f'In comparison, the leaves of the healthy class are such that they do not have speckled white '
            f'spots. The shapes of the leaves are also not distorted.'
        )
        my_data_dir = 'inputs/full_dataset/cherry-leaves'
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
            print(
                f'Please decrease the number of rows or columns '
                f'in your montage. \n'
                f'You have {len(image_list)} images in your subset. '
                f'But you requested a montage with {nrows * ncols} spaces. \n'
            )
    
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


