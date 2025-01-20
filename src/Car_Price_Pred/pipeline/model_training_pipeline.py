from src.Car_Price_Pred.config.configuration import ModelTrainerConfigurationManager
from src.Car_Price_Pred.components.model_training  import ModelTrainer
from Exceptions import CustomException
from Exceptions import CustomException
import sys




class ModelTrainingPipeline():
    def __init__(self):
        pass
    def main(self):
        try:
         config = ModelTrainerConfigurationManager()
         get_model_trainer_config = config.get_model_trainer_config()
         model_trainer = ModelTrainer(config=get_model_trainer_config)
         model_trainer.get_train_and_test_data()
        except Exception as e:
            raise CustomException(e,sys)