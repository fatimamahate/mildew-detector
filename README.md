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

## Dataset Content
* We source our images from [Kaggle.](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves)
* The data set has 4208 images of leaves which are equally seperated into two classes. 

![Cherry Leaves - Healthy]()
![Cherry Leaves - Powdery Mildew]()

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
![Project summary page]()

![Leaf Visualizer page]()

![Mildew Detection page]()

![Project hypothesis page]()

![ML performance page]()

The dashboard has a menu with 5 pages as follows:

#### 1. Project Summary
![Project Summary]()
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
![Leaf Visualizer Page]()
![Average and Variability plots]()
![Difference between average plots]()
![Image Montage-Powdery Mildew]()
![Image Montage-Healthy]()
* The leaf visualizer page aims to work on Business Requirement 1.
    - checkbox 1: Looks at the average and variability plots of healthy and infected leaves.
    - checkbox 2: Looks at the difference between the average of plots of the healthy and infected leaves. 
    - checkbox 3: Looks at the image montages of healthy and powdery mildew leaves respectively.  

#### 3. Mildew Detection
![Mildew Detection Page]()
![Mildew Detection Page - Live Prediction]()
* The mildew detection page aims to work on Business requirement 2. 
    - File uploader to upload your own files as long as they are .jpg or .png format.
    - The output is a prediction of the class of the leaf alongside the name of the file (useful for when more than one image is uploaded)

#### 4. Project Hypothesis 
* The project hypothesis page shows the hypothesis of the project and the validation

#### 5. ML Performance Metrics
![Train, Validation and Test Set: Frequencies plot]()
![Model History - Accuracy and Losses Plot]()
![Model Evaluation report]()

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

## Technologies
1. Python
2. Git - for version control and making commits and pushing to GitHub
3. Github - where the code is saved (in a repo)
4. Heroku - deployed project on here
5. Microsoft Paint - to create wireframe
6. Gitpod - where the code was written (the workspace)
### Python Libraries
1. numpy 
2. pandas
3. matplotlib
4. seaborn
5. plotly
6. streamlit
7. tensorflow
8. shutil
9. PIL
10. joblib

## Deployment

### Heroku
* The App live link is: https://YOUR_APP_NAME.herokuapp.com/ 
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.
1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file. 

## Bugs 
- When getting the working directory, I struggled to get the correct one. Therefore, I used this answer in [Stack Overflow]() to work out how to get the correct working directory.
- I repeatedly got an error which would say that PIL has no attribute called ANTIALIAS. Therefore, I used this answer in [Stack Overflow]() to solve the problem.  
- The size that you can deploy to Heroku is larger than what can be used in Github. Therefore, any files that are not necessary to running the app (such as this README file and documentation files) should be added to the .slugignore file. 
- When first deploying to Heroku, the default stack Heroku uses is Heroku-22. It should be changed to Heroku-20. This can be done by logging into Heroku in ther terminal and then using the following commance - 'heroku stack:set heroku-20'

## Credits
1. As already mentioned I struggled to get the correct working directory, therefore I used the following advice in [Stack Overflow](https://stackoverflow.com/questions/1810743/how-to-set-the-current-working-directory).
2. Once again, as mentioned, I repeatedly got an error which would say that PIL has no attribute called ANTIALIAS. Therefore, I used this answer in [Stack Overflow](https://stackoverflow.com/questions/76616042/attributeerror-module-pil-image-has-no-attribute-antialias) to solve the problem. 
3. I repeatedly throughout the project used the [streamlit documentation](https://docs.streamlit.io/) which was very helpful and easy to use for each of the app pages. 
4. The Walkthrough Project 1 - Malaria Detection was used for this project. The [videos]() as well as the github [repo]() were used to help guide this project in terms of the code and to generally understand what is happening at each stage. 

## Content
1. To learn more about Mildew, I used this website from the [Royal Horticultural Society](https://www.rhs.org.uk/disease/powdery-mildews) in the UK.
2. Code Institute
    * Streamlit
    * Malaria Detector Walkthrough Project
    * Libraries

## Acknowledgements
Thank you to my mentor Precious Ijege for the guidance, support and explanations throughout this project. 