from src.Car_Price_Pred.constants import *
import yaml
from src.Car_Price_Pred.utils.common import read_yaml,create_directories
from src.Car_Price_Pred.entities import DataIngestionConfig,DataEvaluationConfig,DataTransformationConfig,ModelTrainingConfig,ModelEvaluationConfig
from logger import my_logger


class ConfigurationManager:
    def __init__(self,
                 config_file_path = CONFIG_FILE_PATH,
                 params_file_path = PARAMS_FILE_PATH,
                 schema_file_path = SCHEMA_FILE_PATH):
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)
        self.schema = read_yaml(schema_file_path)
        
        create_directories([self.config.Artifacts_root])
        
        
    def get_ingestion_config(self)->DataIngestionConfig:
        self.config = self.config.data_ingestion
        
        create_directories([self.config.root_url])
        
        get_data_ingestion_config = DataIngestionConfig(
            root_url= self.config.root_url,
            source_url= self.config.source_url,
            unzip_data= self.config.unzip_data,
            local_data_path= self.config.local_data_path
        )
        
        return get_data_ingestion_config
    
    
class ValidationConfigurationManager:
    def __init__(self, config_file_path = CONFIG_FILE_PATH,
                 params_file_path = PARAMS_FILE_PATH,
                 schema_file_path = SCHEMA_FILE_PATH):
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)
        self.schema = read_yaml(schema_file_path)
        
        create_directories([self.config.Artifacts_root])
        
    def data_evaluation_config(self)->DataEvaluationConfig:
        config = self.config.data_evaluation
        schema = self.schema.CONTENT
        create_directories([config.root_url])
        
        get_data_evalution_config = DataEvaluationConfig(
            root_url = config.root_url,
            data_directory = config.data_directory,
            validation_status = config.validation_status,
            all_schema = schema
        )
        
        return get_data_evalution_config



class TransformationConfigurationManager:
    def __init__(self, config_file_path = CONFIG_FILE_PATH,):
        self.config = read_yaml(config_file_path)
        
        # creating folder
        create_directories([self.config.Artifacts_root])
    # Accesing the configuration manager
    
    def get_data_transformation_config(self)->DataTransformationConfig:
        config = self.config.data_transformation
        
        create_directories([config.root_url])
        
        get_data_transformation_config = DataTransformationConfig(
            root_url = config.root_url,
            data_dir = config.data_dir,
            preprocessor_path=config.preprocessor_path
        )
        
        return get_data_transformation_config
    
    


# Creating model training configuration manager

class ModelTrainerConfigurationManager:
    def __init__(self,config_file_path = CONFIG_FILE_PATH,
                 param_file_path = PARAMS_FILE_PATH):
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(param_file_path)
        
        create_directories([self.config.Artifacts_root])
        
    def get_model_trainer_config(self)->ModelTrainingConfig:
        config = self.config.model_training
        params = self.params.parameters
        
        create_directories([config.root_url])
        
        get_model_trainer_config = ModelTrainingConfig(
            root_url = config.root_url,
            train_data = config.train_data,
            params = params,
            scores_path = config.scores_path,
            fit_intercept = params.fit_intercept,
            n_jobs = params.n_jobs,
            max_depth = params.max_depth,
            min_samples_split = params.min_samples_split,
            min_samples_leaf = params.min_samples_leaf,
            random_state = params.random_state,
            n_estimators = params.n_estimators,
            alpha = params.alpha,
            max_iter = params.max_iter,
            tol = params.tol,
            n_neighbors = params.n_neighbors,
            weights = params.weights,
            algorithm = params.algorithm,
            p = params.p,
            gamma = params.gamma,
            kernel = params.kernel,
            C = params.C,
            epsilon = params.epsilon
            
        )
        
        return get_model_trainer_config
    
    
    
class ModelEvaluationConfigurationManager:
    def __init__(self, config_file_path = CONFIG_FILE_PATH,
                 params_file_path = PARAMS_FILE_PATH):
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)
        
        create_directories([self.config.Artifacts_root])
        
    def get_model_evaluation_config(self)->ModelEvaluationConfig:
        config = self.config.model_evaluation
        params = self.params.parameters
        
        create_directories([config.root_url])
        model_evaluation_config = ModelEvaluationConfig(
            root_url = config.root_url,
            evaluation_data = config.evaluation_data,
            best_model_path = config.best_model_path,
            scores_path = config.scores_path,
            decision_tree = config.decision_tree,
            all_params = params,
            lasso = config.lasso,
            linear_regression = config.linear_regression,
            neighbors = config.neighbors,
            svm = config.svm,
            random_forest = config.random_forest
        )
        
        return model_evaluation_config
    