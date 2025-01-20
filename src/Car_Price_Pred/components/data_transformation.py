from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder,StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from pathlib import Path
import os
from src.Car_Price_Pred.config.configuration import DataTransformationConfig
import pandas as pd
from logger import my_logger
import numpy as np




class DataTransformation():
    def __init__(self,config:DataTransformationConfig):
        self.config = config
        
    def get_data_transformer(self):
        taxi_data_path = self.config.data_dir
        folder_path = self.config.root_url
        
        taxi_data = pd.read_csv(taxi_data_path)
        x = taxi_data.iloc[:,0:-1]
        y = taxi_data.iloc[:,-1]
        
        x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=42)
        numerical_columns = x.select_dtypes(exclude=['object']).columns
        categorical_columns = x.select_dtypes(include=['object']).columns
        
        
        transformer_categorical = ColumnTransformer(
          transformers = [
             ('categorical_pipeline', Pipeline([
                 ('imputer', SimpleImputer(strategy='most_frequent')),
                 ('encoder', OrdinalEncoder()),
                ('scaler', StandardScaler())
                 ]), categorical_columns)])

        transformer_numerical = ColumnTransformer(
          transformers = [
             ('numerical_pipeline', Pipeline([
                 ('imputer', SimpleImputer(strategy='median')),
                 ('scaler', StandardScaler())
                      ]), numerical_columns)])
        
        
        preprocessor = ColumnTransformer([
             ('categorical', transformer_categorical, categorical_columns),
             ('numerical', transformer_numerical, numerical_columns)])

        
        scaled_x_train = preprocessor.fit_transform(x_train)
        scaled_x_test = preprocessor.transform(x_test)
        
        scaled_train_df = pd.DataFrame(scaled_x_train,columns = preprocessor.get_feature_names_out())
        scaled_test_df = pd.DataFrame(scaled_x_test,columns = preprocessor.get_feature_names_out())
        
        scaled_train_array = np.c_[scaled_train_df,np.array(y_train)]
        scaled_test_array = np.c_[scaled_test_df,np.array(y_test)]
        
        scaled_train = pd.DataFrame(scaled_train_array)
        scaled_test = pd.DataFrame(scaled_test_array)
        
        scaled_train.to_csv(os.path.join(folder_path,'train_data.csv'),index=False)
        scaled_test.to_csv(os.path.join(folder_path,'test_data.csv'),index=False)
