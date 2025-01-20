from src.Car_Price_Pred.config.configuration import ValidationConfigurationManager
from src.Car_Price_Pred.components.data_evaluation import DataEvaluation
import sys
from Exceptions import CustomException



class DataValidationPipeline():
    def __init__(self):
        pass
    def main(self):
        try:
            config = ValidationConfigurationManager()
            data_evaluation_config = config.data_evaluation_config()
            data_evaluation = DataEvaluation(config=data_evaluation_config)
            data_evaluation.evaluate_data()
        except Exception as e:
            raise CustomException(e,sys)