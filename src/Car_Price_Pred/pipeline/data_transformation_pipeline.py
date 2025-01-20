from Exceptions import CustomException
import sys
from src.Car_Price_Pred.config.configuration import TransformationConfigurationManager
from src.Car_Price_Pred.components.data_transformation import DataTransformation



# Trnasformation pipeline
class DataTransformationPipeline():
    def __init__(self):
        pass
    def main(self):
        try:
            # Transformation pipeline
            config = TransformationConfigurationManager()
            get_data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransformation(config=get_data_transformation_config)
            data_transformation.get_data_transformer()
        except Exception as e:
            raise CustomException(e,sys)