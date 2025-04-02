from flask import Flask,render_template,request

import pandas as pd
from Exceptions import CustomException
import numpy as np
from src.Car_Price_Pred.pipeline.prediction_pipeline import Prediction,CustomData
import sys
import os


app = Flask(__name__)
@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        try:
            # Reading inputsgiven by the user
            data = CustomData(
                Trip_Distance_km = float(request.form.get('Trip_Distance_km')),
                Time_of_Day = str(request.form.get('Time_of_Day')),
                Day_of_Week = str(request.form.get('Day_of_Week')),
                Passenger_Count = float(request.form.get('Passenger_Count')),
                Traffic_Conditions = str(request.form.get('Traffic_Conditions')),
                Weather = str(request.form.get('work_type')),
                Base_Fare = str(request.form.get('Base_Fare')),
                Per_Km_Rate = float(request.form.get('Per_Km_Rate')),
                Per_Minute_Rate = float(request.form.get('Per_Minute_Rate')),
                Trip_Duration_Minutes = float(request.form.get('Trip_Duration_Minutes'))
                )
        except Exception as e:
            raise CustomException(e,sys)
        

        data = data.get_data_as_dataframe()
            
        obj = Prediction()
        prediction = obj.predict(data)
            
        return render_template('results.html',prediction=float(prediction))
        
        
            
if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 8080)
    
