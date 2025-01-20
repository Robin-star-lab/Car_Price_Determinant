from src.Car_Price_Pred.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.Car_Price_Pred.pipeline.data_evaluation_pipeline import DataValidationPipeline
from src.Car_Price_Pred.pipeline.data_transformation_pipeline import DataTransformationPipeline
from src.Car_Price_Pred.pipeline.model_training_pipeline import ModelTrainingPipeline
from logger import my_logger

stage_name = 'Data Ingestion Stage'
if __name__=='__main__':
    # Injest
    obj = DataIngestionPipeline()
    obj.main()
    
    my_logger.info(f"Stage : ==========={stage_name}=======successfully implimented")
    
    
stage_name = 'Data Evaluation Stage'
if __name__=='__main__':
    # Validate
    obj =DataValidationPipeline()
    obj.main()
    my_logger.info(f"Stage : ==========={stage_name}=======successfully implimented")


stage_name = 'Data Transformation Stage'
if __name__== '__main__':
    # Transform
    obj = DataTransformationPipeline()
    obj.main()
    
    my_logger.info(f"Stage : ==========={stage_name}=======Successfully implimented")
    
    
    
stage_name = 'Model Training Stage'
if __name__=='__main__':
    # Train
    obj = ModelTrainingPipeline()
    obj.main()
    
    
    my_logger.info(f"Stage : ==========={stage_name}=======Successfully implimented")