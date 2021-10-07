# importing required packages

from flask import Flask,render_template,request,abort
import pickle
import numpy as np
import logging
import pymongo

# configuring logging method
logging.basicConfig(filename='info.txt', 
                    level=logging.INFO,
                    filemode='a',
                    format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt='%Y-%m-%d %H:%M-%S')

# Load the decision tree model
regressor = pickle.load(open('DT_bike_sharing.pkl', 'rb'))

app = Flask(__name__)

# route for 404 error handler 
@app.errorhandler(404)
def page_not_found(error):
    logging.error("Page not found: %s", (request.path))
    return render_template('404_error.html',title='404 Error', msg=request.path)

# route for 403 error handler
@app.errorhandler(405)
def page_not_found(error):
    logging.error("Method is not allowed: %s", (request.path))
    return render_template('405_error.html',title='405 Error', msg=request.path)

# route for 500 error handler
@app.errorhandler(500)
def internal_server_error(error):
    logging.error('Server Error: %s' % error)
    return render_template('500.html', title='500 Error',msg=error)

# route for main page
@app.route('/')
def index():
        try:
            logging.info("someone is accessing index.html!!!")
            return render_template("index.html")
        except Exception as e:
            logging.critical("Cannot able to access index.html...! ")
            return render_template("error.html")

# route for prediction 
@app.route('/predict', methods=['POST'])
def predict():
    try:
        if request.method == 'POST':
            Season = request.form["Season"]
            holliday = request.form["holliday"]
            Month = request.form["Month"]
            Hour = request.form["Hour"]
            day_of_week = request.form["day of week"]
            wheather = request.form["wheather"]
            temp = request.form["temp"]
            humidity = request.form["humidity"]
            windspeed = request.form["windspeed"]

            logging.info("Successfully retrieved information from user...! ")
            print(Season)
            print(holliday)
            print(Month)
            print(Hour)
            print(day_of_week)
            print(wheather)
            print(temp)
            print(humidity)
            print(windspeed)

            data = [[Season,Month,Hour,holliday,day_of_week,wheather,temp,humidity,windspeed]]
            
            prediction = regressor.predict(data)
            my_prediction = int(prediction)

            logging.info("Successfully predicted")
            
    except Exception as e:
        logging.critical("Found Exception in route /predict: ")
        return render_template("error.html")
        
    # database connections
    try:
        default_connection_url ="mongodb+srv://bike:bikepassword@cluster0.wppk4.mongodb.net/bikedb?retryWrites=true&w=majority"
        client = pymongo.MongoClient(default_connection_url)
        logging.info("Database connection established..!")
    except Exception as e:
        logging.warning("Error while connecting to Database")
            
    try:
        db_name = "bike"
        database = client[db_name]
        print("DB created!!")
        collection_name = "user_details"
        collection = database[collection_name]
        print("collection Created!!")
    except Exception as e:
        logging.warning("found error in DB or Collection ")

    try:
        info = {
            #    '_id':220,
                'Season': Season,
                'holiday': holliday,
                'Month': Month,
                'Hour': Hour,
                'day_of_week': day_of_week,
                'wheather': wheather,
                'temp': temp,
                'humidity': humidity,
                'windspeed': windspeed,
                'prediction': my_prediction
            }
        
        collection.insert_one(info)
        logging.info("data inserted")
   
    except Exception as e:
        logging.warning("found error in info json ")

    logging.info("successfully predicted")
    return render_template('Result.html', predict=my_prediction)
     
   

if __name__ == "__main__":
    app.run(debug=True)
