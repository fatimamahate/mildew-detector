![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Mildew Detector - Cherry Leaves Project
Mildew detector is an app which can take images of cherry leaves and determine if they are healthy or if they have powdery mildew. 
It uses a binary classification ML model to predict the outcome of the leaf. 

You can [view the live app here](https://cherry-leaves-acdb1f6c2341.herokuapp.com/)

## Content
1. [Dataset Content](#dataset-content)
2. [Business Requirements](#business-requirements)
3. [Hypothesis and How to Validate?](#hypothesis-and-how-to-validate)
4. [Rationale to map the business requirements to the Data Visualisations and ML tasks](#rationale-to-map-the-business-requirements-to-the-data-visualisations-and-ml-tasks)
5. [ML Business Case](#ml-business-case)
6. [Dashboard Design](#dashboard-design)
7. [Technologies Used](#technologies-used)
8. [Deployment](#deployment)
9. [Bugs](#bugs)
10. [Credits](#credits)
11. [Content](#content)
12. [Acknowledgements](#acknowledgements)

## Dataset Content
* We source our images from [Kaggle.](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves)
* The data set has 4208 images of leaves which are equally seperated into two classes. 

![Cherry Leaves - Kaggle Site](/documentation/1_dataset_content/kaggle_site.JPG)


## Business Requirements
Farmy & Foods has a cherry tree plantation. Unfortunately, the cherry trees can be affected with powdery mildew. Traditionally, an employee would have to manually check if the tree has mildew. If it does, then a fungicidal wash would have to be applied. This process takes upward of 30 minutes per tree. Given that this a cherry farm, it is not efficient to carry the process for each tree. 

To make it easier to identify and to save time, the IT team suggested developing an ML system which would be able to detect the powdery mildew on the leaves simply after taking pictures of the leaves. 

The dataset we have is provided by Farmy & Foods. 

Farmy & Foods are our client and they are interested in :

* 1 - conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
* 2 - predicting if a cherry leaf is healthy or contains powdery mildew.

## Hypothesis and How to Validate?
* The ML model will be able to classify the leaf into healthy and powdery mildew classes with at least 97% accuracy. 
* An image montage will be able to visually show leaves belonging to the healthy class and leaves belong to the powdery_mildew class. 
    - The images in the powdery mildew class will have leaves which have white specks.
    - The images in the powdery mildew class will have leaves that are also distorted around the edges. 
    - The images in the healthy class will have leaves which do not have any white specks. 
    - The images in the healthy class will have leaves which do not have any distorted edges. 
* The average, variability and difference plots did not intuitively differentiate between the two classes. However, it should be noted that when comparing the average plots of each class, the powdery mildew plot has more white specks than the healthy plot. The average healthy plot has a more homegeneous green colour whereas the average powdery mildew plot has white specks throughout it. Similarly, the variability plot of the healthy class has a more homogeneous plot when compared to the powdery mildew variability plot. 

## Rationale to map the business requirements to the Data Visualisations and ML tasks

### Business Requirement 1
Business Requirement 1: conduct a study to visually differentiate a healthy cherry leaf from one with powdery mildew.

* As a client, I would like to show the mean and standard deviation of healthy cherry leaves.
* As a client, I would like to show the mean and standard deviation of powdery mildew cherry leaves. 
* As a client, I would like to show the difference between the average plots of healthy and powdery mildew leaves. 
* As a client, I would like to show an image montage of healthy cherry leaves. 
* As a client, I would like to show an image montage of powdery mildew leaves. 

### Business Requirement 2
Business Requirement 2: predict if a cherry leaf is healthy or contains powdery mildew.

* As a client, I would like to predict if a cherry leaf image that I have uploaded is healthy or infected with powdery mildew along with a report. 

## ML Business Case
The aim of this model is to differentiate leaves into 2 classes - healthy and powdery mildew. This will allow for farmers to diagnose whether a tree is infected faster than the current traditional methods which can take upwards of 30 minutes per tree. Therefore, since the current method takes a long time, it is not scalable on a large scale such as in a farm.
The farmer will be able to take pictures of the leaves on a tree and upload them to the model. The output will be that the leaf is healthy or infected with powdery mildew. This will reduce the time to check the trees for the farmer. We expect 97% accuracy on the test set and images that were uploaded by farmer. The training data was using the dataset from [Kaggle](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves). The original dataset includes 4208 images equally split into healthy and powdery mildew leaves. All images are of the size 256 px x 256 px. 

## Dashboard Design
### Wireframes
The wireframes for this project are as below:
![Project summary wireframe](/documentation/2_wireframes/1_wireframe_project_summary.png)

![Leaf Visualizer wireframe](/documentation/2_wireframes/2_wireframe_leaf_visualizer.png)

![Mildew Detection wireframe](/documentation/2_wireframes/3_wireframe_mildew_detection.png)

![Project hypothesis wireframe](/documentation/2_wireframes/4_wireframe_project_hypothesis.png)

![ML performance wireframe](/documentation/2_wireframes/5_wireframe_ML_performance.png)

The dashboard has a menu with 5 pages as follows:

#### 1. Project Summary
![Project Summary](/documentation/3_project_summary/project_summary.JPG)
* Information
    - General background is written as below:
        - Cherry trees are needed for the farming of cherries as well as being important for pollinators.However, cherry trees can be infected by the powdery mildew fungus which reduces the abilities of the plant.Mildew is a fungus that can grow over the leaves of the tree and produce a white, powdery substance.This reduces the ability of the tree to photosynthesise. Photosynthesis is essentially the method in how plants transform energy. Since the photosynthesis is reduced (due to the mildew), the tree will produce less cherries. For farmers, this would result in a smaller yield. For important pollinators, this would result in fewer flowers to actually pollinate. Traditionally, farmers would have to manually check each tree which is time consuming and and difficult especially in hot, humid climates.
* Business Requirements
    - The business requirements are written out as below:
        - The two business requirements for this project are: 1) The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew. 2)The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.
* Additional Information
    - the additional information contains links to the Kaggle dataset and this README file. 
    - It also contains information on how many images there are in total.

#### 2. Leaf Visualizer
![Leaf Visualizer Page](/documentation/4_leaf_visualizer/1_leaf_visualizer_page.JPG)
![Average and Variability plots](/documentation/4_leaf_visualizer/2_average_variability_plots.JPG)
![Difference between average plots](/documentation/4_leaf_visualizer/3_average_difference_plots.JPG)
![Image Montage-Powdery Mildew](/documentation/4_leaf_visualizer/4_montage_powdery.JPG)
![Image Montage-Healthy](/documentation/4_leaf_visualizer/5_montage_healthy.JPG)
* The leaf visualizer page aims to work on Business Requirement 1.
    - checkbox 1: Looks at the average and variability plots of healthy and infected leaves.
    - checkbox 2: Looks at the difference between the average of plots of the healthy and infected leaves. 
    - checkbox 3: Looks at the image montages of healthy and powdery mildew leaves respectively.  

#### 3. Mildew Detection
![Mildew Detection Page](/documentation/5_mildew_detection/1_mildew_detection_page.JPG)
* I obtained the image of the leaves below from [Pexels](https://www.pexels.com/photo/bright-green-elm-tree-leaf-4131782/) and [Unsplash](https://unsplash.com/photos/green-leaf-on-white-surface-qcRMfoIWxRo)
![Mildew Detection Page - Live Prediction](/documentation/5_mildew_detection/2_live_pred_healthy.JPG)
![Mildew Detection Page - Live Prediction - more than one image](/documentation/5_mildew_detection/3_live_pred_multi.JPG)
* The mildew detection page aims to work on Business requirement 2. 
    - File uploader to upload your own files as long as they are .jpg or .png format.
    - The output is a prediction of the class of the leaf alongside the name of the file (useful for when more than one image is uploaded)


#### 4. Project Hypothesis 
![Project Hypothesis Page](/documentation/6_project_hypothesis/1_project_hypothesis.JPG)
* The project hypothesis page shows the hypothesis of the project and the validation

#### 5. ML Performance Metrics
![Train, Validation and Test Set: Frequencies plot](/documentation/7_ML_performance_metrics/1_frequency_plot.JPG)
![Model History (Accuracy and Losses Plot) and Evaluation](/documentation/7_ML_performance_metrics/2_model_history_eval.JPG)


The dataset was split up as follows:
* Train (70%)
    - Healthy - 1472 images
    - Powdery Mildew - 1472 images
* Test (20%)
    - Healthy - 422 images
    - Powdery Mildew - 422 images
* Validation (10%)
    - Healthy - 210 images
    - Powdery Mildew - 210 images

The model has accuracy of 99.53% which is higher than the expectation of 97%. 

## Technologies Used
1. Python
2. Git - for version control and making commits and pushing to GitHub
3. GitHub - where the code is saved (in a repo)
4. Heroku - deployed project on here
5. Microsoft Paint - to create wireframe
6. Gitpod - where the code was written (the workspace)
### Python Libraries
1. [numpy] (https://numpy.org/)
2. [pandas](https://pandas.pydata.org/)
3. [matplotlib](https://matplotlib.org/)
4. [seaborn](https://seaborn.pydata.org/)
5. [plotly](https://plotly.com/python/)
6. [streamlit](https://streamlit.io/)
7. [tensorflow](https://www.tensorflow.org/)
8. [shutil](https://docs.python.org/3.8/library/shutil.html)
9. [PIL](https://en.wikipedia.org/wiki/Python_Imaging_Library)
10. [joblib](https://joblib.readthedocs.io/en/stable/)

## Deployment

### Heroku
- The live website is : https://cherry-leaves-acdb1f6c2341.herokuapp.com/
- Ensure the stack is Heroku-20 as opposed to the default Heroku-22
- To deploy
    1. Log in to Heroku (may require Multi Factor Authentication)
    2. Create an App with a unique name and select the relevant region.
    3. Go to the Deploy tab and click on it.
    4. Click on GitHub as your deployment method. 
    5. Then find your repository.
    6. Click search.
    7. Once found, click connect. 
    8. Select the branch you would like to deploy (in this case main) and then click deploy. 
        - You can choose manual deploy (recommended when still making changes to your project)
        - you can also choose automatic deploy(recommended when it is complete.)
    9. click on open app. You should be able to see your app. 
    10. If you cannot see the app, consider adding large files that are not needed for the app into your .slugignore file to reduce the size. 

## Bugs 
- When getting the working directory, I struggled to get the correct one. Therefore, I used this answer in [Stack Overflow]() to work out how to get the correct working directory.
- I repeatedly got an error which would say that PIL has no attribute called ANTIALIAS. Therefore, I used this answer in [Stack Overflow]() to solve the problem.  
- The size that you can deploy to Heroku is larger than what can be used in Github. Therefore, any files that are not necessary to running the app (such as this README file and documentation files) should be added to the .slugignore file. 
- When first deploying to Heroku, the default stack Heroku uses is Heroku-22. It should be changed to Heroku-20. This can be done by logging into Heroku in ther terminal and then using the following commance - 'heroku stack:set heroku-20'

## Credits
1. As already mentioned I struggled to get the correct working directory, therefore I used the following advice in [Stack Overflow](https://stackoverflow.com/questions/1810743/how-to-set-the-current-working-directory).
2. Once again, as mentioned, I repeatedly got an error which would say that PIL has no attribute called ANTIALIAS. Therefore, I used this answer in [Stack Overflow](https://stackoverflow.com/questions/76616042/attributeerror-module-pil-image-has-no-attribute-antialias) to solve the problem. 
3. Images for the image upload in the Mildew Detection section are taken from [Unsplash](https://unsplash.com/photos/green-leaf-on-white-surface-qcRMfoIWxRo) by Kwang Javier and from [Pexels](https://www.pexels.com/photo/bright-green-elm-tree-leaf-4131782/) by Kelly
4. I repeatedly throughout the project used the [streamlit documentation](https://docs.streamlit.io/) which was very helpful and easy to use for each of the app pages. 
5. The Walkthrough Project 1 - Malaria Detection was used for this project. The videos from [Code Institute](https://codeinstitute.net/) as well as the github [repo](https://github.com/GyanShashwat1611/WalkthroughProject01) were used to help guide this project in terms of the code and to generally understand what is happening at each stage. 

## Content
1. To learn more about Mildew, I used this website from the [Royal Horticultural Society](https://www.rhs.org.uk/disease/powdery-mildews) in the UK.
2. Code Institute
    * Streamlit
    * Malaria Detector Walkthrough Project
    * Libraries

## Acknowledgements
Thank you to my mentor Precious Ijege for the guidance, support and explanations throughout this project. 