import urllib.request as request
from src.Car_Price_Pred.entities import DataIngestionConfig
import os
from logger import my_logger
import zipfile




class DataIngestion():
    def __init__(self, config:DataIngestionConfig):
        self.config = config
    
    # Loading and unzipping github data
    def load_data(self):
        # This function loads data from github
        local_data_path = self.config.local_data_path
        if (not os.path.exists(local_data_path)):
            file_name,headers = request.urlretrieve(
                url=self.config.source_url,
                filename=local_data_path
            )
            my_logger.info(f"Data downloaded from: {self.config.source_url} into: {local_data_path}")
    def extract_data(self):
        # This function extracts data from the downloaded zipfile
        local_data_path = self.config.local_data_path
        unzip_data = self.config.unzip_data
        if unzip_data !="":
            os.makedirs(unzip_data,exist_ok=True)
        else:
            my_logger.info("Folder already exists")
        with zipfile.ZipFile(local_data_path) as zipref:
            zipref.extractall(unzip_data)
            
        my_logger.info(f"Extracted the zipfile: {local_data_path} into: {unzip_data}")
            