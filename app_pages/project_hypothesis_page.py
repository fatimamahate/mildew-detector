import streamlit as st

def project_hypothesis_page_body():
    """
    Function for the content of the project hypothesis page
    """
    st.header('Project Hypothesis and Validation')
    st.info(
        f'Whether cherry leaves are infected by powdery mildew '
        f'can be identified by looking at the leaf. If there is '
        f'a white powdery substance on the leaf, then it is infected. '
        f'Furthermore, the infected leaves also have distorted edges. '
        f'Therefore, to reduce time taken for farmers, this ML model should '
        f'be able to differentiate healthy and powdery mildew leaves to 97% accuracy.'
    )
    st.success(
        f'-The image montage shows the differences between '
        f'the healthy and powdery mildew leaves.  \n'
        f'-The average, variability image and average difference confirmed '
        f'the hypothesis since it shows there are some color differences '
        f'particularly in the centre of the image.  \n'
        f'-Finally when testing the ML model and it can differentiate '
        f'a healthy leaf and powdery mildew leaf -  >97% accuracy.'
    )