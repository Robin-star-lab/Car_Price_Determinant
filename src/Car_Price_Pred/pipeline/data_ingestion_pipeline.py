from src.Car_Price_Pred.config.configuration import ConfigurationManager
from src.Car_Price_Pred.components.data_ingestion  import DataIngestion
from Exceptions import CustomException
import sys
import yaml



class DataIngestionPipeline():
    def __init__(self):
        pass
    def main(self):
        # Ingestion pipeline
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_ingestion_config()
            data_ingestion =DataIngestion(config=data_ingestion_config)
            data_ingestion.load_data()
            data_ingestion.extract_data()
        except Exception as e:
            raise CustomException(e,sys)
            