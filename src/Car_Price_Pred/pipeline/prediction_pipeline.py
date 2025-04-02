import sys
from Exceptions import CustomException
from pathlib import Path
from src.Car_Price_Pred.utils.common import load_models
import pandas as pd
import joblib

class Prediction():
    def __init__(self):
        self.model = load_models(Path("artifacts\model_evaluation\RandomForestRegressor(max_depth=10)_.joblib"))
        self.preprocessor = joblib.load(Path("artifacts\data_transformation\preprocessor.pkl"))
    
    def predict(self,input_data):
        for col in input_data.columns:
            
            if input_data[col].dtype == 'object': 
                # Only for string/categorical columns
               input_data[col] = input_data[col].replace('None', input_data[col].mode()[0])
        scaled_input_data = self.preprocessor.transform(input_data)
        Prediction = self.model.predict(scaled_input_data)
        
        return Prediction
    
    
class CustomData():
    def __init__(self,
                 Trip_Distance_km: float,
                 Time_of_Day: str,
                 Day_of_Week: str,
                 Passenger_Count: float,
                 Traffic_Conditions: str,
                 Weather: str,
                 Base_Fare: str,
                 Per_Km_Rate: float,
                 Per_Minute_Rate: float,
                 Trip_Duration_Minutes: float):
        self.Trip_Distance_km = Trip_Distance_km
        self.Time_of_Day = Time_of_Day
        self.Day_of_Week = Day_of_Week
        self.Passenger_Count = Passenger_Count
        self.Traffic_Conditions = Traffic_Conditions
        self.Weather = Weather
        self.Base_Fare = Base_Fare
        self.Per_Km_Rate = Per_Km_Rate
        self.Per_Minute_Rate = Per_Minute_Rate
        self.Trip_Duration_Minutes = Trip_Duration_Minutes
    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                "Trip_Distance_km" : [self.Trip_Distance_km],
                "Time_of_Day" : [self.Time_of_Day],
                "Day_of_Week" : [self.Day_of_Week],
                "Passenger_Count" : [self.Passenger_Count],
                "Traffic_Conditions" : [self.Traffic_Conditions],
                "Weather" : [self.Weather],
                "Base_Fare" : [self.Base_Fare],
                "Per_Km_Rate" : [self.Per_Km_Rate],
                "Per_Minute_Rate" : [self.Per_Minute_Rate],
                "Trip_Duration_Minutes" : [self.Trip_Duration_Minutes]
            }
            
            data = pd.DataFrame(custom_data_input_dict)
            return data
        except Exception as e:
            raise CustomException(e,sys)
        