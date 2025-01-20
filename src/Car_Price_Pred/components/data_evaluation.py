import sys
from Exceptions import CustomException
from src.Car_Price_Pred.entities import DataEvaluationConfig
import pandas as pd



class DataEvaluation():
    def __init__(self,config: DataEvaluationConfig):
        self.config = config
        
    def evaluate_data(self):
        data_to_evaluate = pd.read_csv(self.config.data_directory)
        columns_to_evaluate = list(data_to_evaluate.columns)
        columns_compared_with = self.config.all_schema.keys()
        
        try:
            Validation_status = None
            for columns in columns_to_evaluate:
                if columns not in columns_to_evaluate:
                    Validation_status = False
                    with open(self.config.validation_status,'w') as valid:
                        valid.write(f"The Validation status is: {Validation_status}")
                else:
                    Validation_status = True
                    with open(self.config.validation_status,'w') as valid:
                        valid.write(f"The validation status is: {Validation_status}")
                        
        except Exception as e:
            raise CustomException(e,sys)