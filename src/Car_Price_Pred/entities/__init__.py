from dataclasses import dataclass
from pathlib import Path


@dataclass
class DataIngestionConfig():
    root_url: Path
    source_url: str
    unzip_data: Path
    local_data_path: Path
    
@dataclass
class DataEvaluationConfig():
    root_url: Path
    data_directory: Path
    validation_status:  str
    all_schema:  dict


@dataclass
class DataTransformationConfig():
    # Data transformation configuration done here
    root_url: Path
    data_dir: Path
    preprocessor_path: Path
    
    
# Model training configuration
@dataclass
class ModelTrainingConfig():
    root_url: Path
    train_data: Path
    params: dict
    scores_path: Path
    fit_intercept: bool
    n_jobs: int
    max_depth: int
    min_samples_split: int
    min_samples_leaf: int
    random_state: int
    n_estimators: int
    alpha: float
    max_iter: int
    tol: float
    n_neighbors: int
    weights: str
    algorithm: str
    p: int
    gamma: str
    kernel: str
    C: float
    epsilon: float
    
    
    
@dataclass
class ModelEvaluationConfig():
    root_url: Path
    evaluation_data: Path
    best_model_path: Path
    all_params: dict
    scores_path: Path
    decision_tree: str
    lasso: str
    linear_regression: str
    neighbors: str
    svm: str
    random_forest: str
    
