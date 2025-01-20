import os
from pathlib import Path
import logging

project_name = "Car_Price_Pred"
list_of_files = [
    "src/__init__.py",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/entities/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/config/configuration.py",
    "config/config.yaml",
    "params.yaml",
    "requirements.txt",
    "schema.yaml",
    "setup.py",
    "app.py",
    "main.py"
]


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s : %(module)s : %(message)s')
for filepath in list_of_files:
    filepath = Path(filepath)
    file_dir,filename = os.path.split(filepath)
    
    logging.info("Splitted the filepath into :{file_dir} and  {filename}")
    if file_dir != "":
        
        os.makedirs(file_dir,exist_ok=True)
        logging.info(f"Created the directory {file_dir}")
    else:
        logging.info("File directory already exists")
        
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) ==0):
        with open(filepath,'w') as f:
                pass
        logging.info(f"Created file: {filename}")
    else:
            logging.info(f"File {filename} already exists")
            
            