import yaml
import os
from box import ConfigBox
from typing import List
from pathlib import Path
from ensure import ensure_annotations
from logger import my_logger
import joblib
import pickle
import json



@ensure_annotations
def read_yaml(file_path:Path)->ConfigBox:
    
    with open(file_path,'r') as f:
        data = yaml.safe_load(f)
        
        return ConfigBox(data)
    
    my_logger.info(f"Reads yaml file for path :{file_path}")
@ensure_annotations
def create_directories(file_path:List):
    for path in file_path:
        if path !="":
            os.makedirs(path,exist_ok=True)
            
        my_logger.info(f"Creates directory for path;{path} in file paths :{file_path}")
            
            
 
@ensure_annotations           
def save_models(model,file_path):
    
    with open(file_path, 'wb') as f:
        joblib.dump(model,f)
        
@ensure_annotations        
def save_parameters(params, filepath):
    # Assuming params is a dictionary or a list of dictionaries
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(params,f)
        
        
@ensure_annotations      
def load_models(filepath):
    with open(filepath, 'rb') as f:
        model = joblib.load(f)
        return model


@ensure_annotations
def load_parameters(filepath):
    with open(filepath, 'rb') as f:
        params = joblib.load(f)
        
        return params
    
@ensure_annotations
def save_best_model(model, filepath):
    with open(filepath, 'wb') as f:
        joblib.dump(model,f)

@ensure_annotations
def save_scores(scores, filepath):
    with open(filepath, 'w') as score_file:
        score_file.write(f"{scores}/n")
@ensure_annotations
def save_json(preprocessor, filepath):
    with open(filepath, 'wb') as pickle_obj:
        pickle.dump(preprocessor,pickle_obj)
        
def load_json(filepath):
    with open(filepath, 'rb') as pickle_obj:
        preprocessor = pickle.load(pickle_obj)
        return preprocessor