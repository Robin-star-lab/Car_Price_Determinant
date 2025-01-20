import yaml
import os
from box import ConfigBox
from typing import List
from pathlib import Path
from ensure import ensure_annotations
from logger import my_logger
import joblib
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
        json.dump(params, f, indent=4, ensure_ascii=False)