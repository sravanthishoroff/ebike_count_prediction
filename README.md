Rental Bike Share Prediction 🚴

Bike sharing systems are a new generation of traditional bike rentals where the whole process from membership, rental and return back has become automatic. Through these systems, users are able to easily rent a bike from a particular position and return back at another position. Currently, there are about over 500 bike-sharing programs around the world which is composed of over 500 thousand bicycles. Today, there exists great interest in these systems due to their important role in traffic, environmental and health issues. Apart from interesting real-world applications of bike sharing systems, the characteristics of data being generated by these systems make them attractive for the research. The goal here is to build an end-to-end regression task. Here the user will provide the data and the result will be given by the best performing hyper tuned Machine Learning model

Table Content ✏️

Demo
Overview
Dataset
Installation
Deployment
Documentation
Directory Tree
Technology Used
Bug/Feature Request
Future scope of project

Demo ✔️

Heroku:- https://ebikecountprediction.herokuapp.com/


AWS(Ec2):- https://ec2-54-84-85-146.compute-1.amazonaws.com:5000 [Can access only on sunday]

bike rent

Overview 📜
This is a Flask web app which predicts the count of the bikes available based on the user's input in which there are several categories to fill in like the season,windspeed,humidity,temperature,at what time user is searching and other things by which model will predict the number of bikes will be available for that particular input and conditions.Data which user enters will be stored in MongoDB for the future use,logging is done at every step.

AIM:

Taking climatic conditions into consideration this model will predict the number of bikes can be used in the particular hour of a day.The bike company make sure that those number of bikes should be available at that time in order to get the optimum utilization of those bikes and earn maximum profits.

DataSet 📊

To Know more about data and its characterstics you can download dataset form https://archive.ics.uci.edu/ml/datasets/Bike+Sharing+Dataset

Installation 🗄️

The Code is written in Python 3.8 If you don't have Python installed you can find it here. If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries, run this command in the project directory after cloning the repository:

pip install -r requirements.txt
Deployement
Heroku
Login or signup in order to create virtual app. You can either connect your github profile or download ctl to manually deploy this project.



Our next step would be to follow the instruction given on Heroku Documentation to deploy a web app.

AWS(Amazon Web Services)
Login or signup with free tier in order to create virtual amchine(EC2 instance) for free. Note:- In free trier virtual Machine will only give free service for 720hr almost a month after that you will be charged , so use carefully. I usally stop instance when it is not needed to avoid extra charge. so it may happen that deployment link for AWS might not work


Our next step would be to follow the instruction given on AWS EC2 Instance Documentation to deploy a web app.

DataBase
App Screenshot


Directory Tree
├── static 
│   ├── styles
│   |   ├── css
│   |   ├── forms
│   |   ├── img
│   |   ├── js
│   |   ├── vendor
├── template
│   ├── index.html
│   ├── result.html
│   ├── 500.html
│   ├── 404_error.html
│   ├── error.html
├── Procfile
├── bike sharing.ipynb
├── day.csv
├── hour.csv
├── README.md
├── main.py
├── DT_bike_sharing.pkl
├── requirements.txt
Documentation
Architecture

Low Level Documentation

High Level Documentation

Wired Framed Diagram

DPR(Detail Documentation Report)

Technologies Used


  

Bug/Feature Request
If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an issue here by including your search query and the expected result

Contributors 
Priyam Trivedi
Sravanthi Shoroff
Future Scope
Use Deeplearning Algorithms
Optimize Flask app.py
Front-End


Kindly, check the code and other files in Master branch 
