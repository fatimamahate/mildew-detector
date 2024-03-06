import streamlit as st

def project_summary_page_body():
    """
    Function for the content of project summary page
    """
    st.title('Project Summary')
    st.info(
        f'Cherry trees are needed for the farming of cherries as well as being important for pollinators.'
        f'However, cherry trees can be infected by the powdery mildew fungus which reduces the abilities of the plant.'
        f'Mildew is a fungus that can grow over the leaves of the tree and produce a white, powdery substance.'
        f'This reduces the ability of the tree to photosynthesise. Photosynthesis is essentially the method in how plants '
        f'transform energy. Since the photosynthesis is reduced (due to the mildew), the tree will produce less cherries. '
        f'For farmers, this would result in a smaller yield. For important pollinators, this would result in fewer flowers '
        f'to actually pollinate. Traditionally, farmers would have to manually check each tree which is time consuming and '
        f'and difficult especially in hot, humid climates.'
    )
    st.warning(
        f'The two business requirements for this project are: '
        f'1) The client is interested in conducting a study to '
        f'visually differentiate a healthy cherry leaf from one with powdery mildew.  \n'
        f'2)The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.'
    )
    st.write(
        f'You can find the data set here:  \n'
        f'[Dataset from Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves).  \n'
        f'This data set has a total of 4208 images split evenly into two classes.  \n'
        f'The two classes of this dataset are healthy leaves and powdery mildew leaves.  \n'
        f'For more information on this model, please visit:  \n'
        f'[Github README](https://github.com/fatimamahate/mildew-detector)'
    )
