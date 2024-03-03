import streamlit as st
from app_pages.multi_page import MultiPage

# pages

from app_pages.project_summary_page import project_summary_page_body
from app_pages.leaf_visualizer_page import leaf_visualizer_page_body
from app_pages.mildew_detection_page import mildew_detection_page_body
from app_pages.project_hypothesis_page import project_hypothesis_page_body
from app_pages.ml_performance_page import ml_performance_page_metrics

app = MultiPage(app_name = 'Mildew Detector')

# add pages to app with .add_page()

app.add_page('Project Summary', project_summary_page_body)
app.add_page('Leaf Visualizer', leaf_visualizer_page_body)
app.add_page('Mildew Detection', mildew_detection_page_body)
app.add_page('Project Hypothesis', project_hypothesis_page_body)
app.add_page('ML Performance Metrics', ml_performance_page_metrics)

app.run()