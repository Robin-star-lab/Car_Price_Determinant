import sys
from src.Car_Price_Pred.config.configuration import ModelEvaluationConfigurationManager
from src.Car_Price_Pred.components.model_evaluation import ModelEvaluation
from Exceptions import CustomException




class ModelEvaluationPipeline():
    def __init__(self):
        pass
    def main(self):
        try:
            config = ModelEvaluationConfigurationManager()
            get_model_evaluation_config = config.get_model_evaluation_config()
            model_evaluation = ModelEvaluation(config=get_model_evaluation_config)
            model_evaluation.evaluate_model()
        except Exception as e:
            raise CustomException(e,sys)