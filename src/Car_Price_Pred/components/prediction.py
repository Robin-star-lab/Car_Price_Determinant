from src.Car_Price_Pred.entities import PredictionConfig
from src.Car_Price_Pred.utils.common import load_models,load_json

class Prediction():
    def __init__(self,config:PredictionConfig):
        self.config = config
        self.model = load_models(self.config.prediction_model)
        self.preprocessor = load_json(self.config.preprocessor)
        
    def predict(self,input_data):
        scaled_input_data = self.preprocessor.transform(input_data)
        Prediction = self.model.predict(scaled_input_data)
        
        return Prediction
    