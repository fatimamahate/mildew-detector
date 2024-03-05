![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

## Codeanywhere Template Instructions

Welcome,

This is the Code Institute student template for Codeanywhere. We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions. Click the `Use this template` button above to get started.

You can safely delete the Codeanywhere Template Instructions section of this README.md file,  and modify the remaining paragraphs for your own project. Please do read the Codeanywhere Template Instructions at least once, though! It contains some important information about the IDE and the extensions we use. 

## How to use this repo

1. Use this template to create your GitHub project repo
1. Log into <a href="https://app.codeanywhere.com/" target="_blank" rel="noreferrer">CodeAnywhere</a> with your GitHub account.
1. On your Dashboard, click on the New Workspace button
1. Paste in the URL you copied from GitHub earlier
1. Click Create
1. Wait for the workspace to open. This can take a few minutes.
1. Open a new terminal and <code>pip3 install -r requirements.txt</code>
1. In the terminal type <code>pip3 install jupyter</code>
1. In the terminal type <code>jupyter notebook --NotebookApp.token='' --NotebookApp.password=''</code> to start the jupyter server.
1. Open port 8888 preview or browser
1. Open the jupyter_notebooks directory in the jupyter webpage that has opened and click on the notebook you want to open.
1. Click the button Not Trusted and choose Trust.
Note that the kernel says Python 3. It inherits from the workspace so it will be Python-3.8.12 as installed by our template. To confirm this you can use <code>! python --version</code> in a notebook code cell.
## Cloud IDE Reminders
To log into the Heroku toolbelt CLI:
1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In the terminal, run `heroku_config`
5. Paste in your API key when asked
You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you, so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.
## Dataset Conten
* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). We then created a fictitious user story where predictive analytics can be applied in a real project in the workplace.
* The dataset contains +4 thousand images taken from the client's crop fields. The images show healthy cherry leaves and cherry leaves that have powdery mildew, a fungal disease that affects many plant species. The cherry plantation crop is one of the finest products in their portfolio, and the company is concerned about supplying the market with a compromised quality product.
## Business Requirement
The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute.  The company has thousands of cherry trees, located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.


* 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
* 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.
## Hypothesis and how to validat?
* List here your project hypothesis(es) and how you envision validating it (them).
## The rationale to map the business requirements to the Data Visualisations and ML task
* List your business requirements and a rationale to map them to the Data Visualisations and ML tasks.
## ML Business Case
* In the previous bullet, you potentially visualised an ML task to answer a business requirement. You should frame the business case using the method we covered in the course.
## Dashboard Design
* List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other items, that your dashboard library supports.
* Finally, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project, you were confident you would use a given plot to display an insight, but later, you chose another plot type).
## Unfixed Bugs
* You will need to mention unfixed bugs and why they were unfixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable for consideration, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.
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
## Main Data Analysis and Machine Learning Libraries
* Here you should list the libraries used in the project and provide an example(s) of how you used these libraries.
## Credits 
* In this section, you need to reference where you got your content, media and from where you got extra help. It is common practice to use code from other repositories and tutorials. However, it is necessary to be very specific about these sources to avoid plagiarism. 
* You can break the credits section up into Content and Media, depending on what you have included in your project. 
### Content 
- The text for the Home page was taken from Wikipedia Article A.
- Instructions on how to implement form validation on the Sign-Up page were taken from [Specific YouTube Tutorial](https://www.youtube.com/).
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/).
### Media
- The photos used on the home and sign-up page are from This Open-Source site.
- The images used for the gallery page were taken from this other open-source site.
## Acknowledgements (optional)
* Thank the people that provided support throughout this project.

# Mildew Detector - Cherry Leaves Project
Mildew detector is an app which can take images of cherry leaves and determine if they are healthy or if they have powdery mildew. 
It uses a binary classification ML model to predict the outcome of the leaf. 

You can [view the live app here](https://cherry-leaves-acdb1f6c2341.herokuapp.com/)

## Content
1. [Dataset Content](#dataset-content)
2. [Business Requirements](#business-requirements)
3. [Hypothesis and How to Validate?](#hypothesis-and-how-to-validate)
4. [Rationale to map the business requirements to the Data Visualisations and ML tasks](#rationale-to-map-the-business-requirements-to-the-data-visualisations-and-ml-tasks)

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

* As a client, I would like to predict if a cherry leaf image that I have uploaded is healthy or infected with powdery mildew. 
* As a client, I would like to generate reports on the image I have uploaded.

### ML Business Case