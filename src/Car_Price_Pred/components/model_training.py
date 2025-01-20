from sklearn.linear_model import LinearRegression,Ridge,Lasso
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import sys
from Exceptions import CustomException
from pathlib import Path
import joblib 
from src.Car_Price_Pred.config.configuration import ModelTrainingConfig
import os
from src.Car_Price_Pred.utils.common import save_models,save_parameters







# Model training configuration
class ModelTrainer():
    def __init__(self,config: ModelTrainingConfig):
        self.config = config
        
    def get_train_and_test_data(self):
        # Gathering the training and testing data
        train_data_path = self.config.train_data
        
        train = pd.read_csv(train_data_path,header=None)
        train.fillna(train.mean(),inplace=True)
        
        x_train = train.iloc[:,:-1]
        y_train = train.iloc[:,-1]
        
        # Create dictionary of models
        models = {
            'linear_regression': LinearRegression(fit_intercept=self.config.fit_intercept,n_jobs=self.config.n_jobs),
            'decision_tree': DecisionTreeRegressor(max_depth=self.config.max_depth,min_samples_split=self.config.min_samples_split,min_samples_leaf=self.config.min_samples_leaf,random_state=self.config.random_state),
            'random_forest': RandomForestRegressor(n_estimators=self.config.n_estimators,max_depth=self.config.max_depth),
            'ridge': Ridge(alpha=self.config.alpha,fit_intercept=self.config.fit_intercept),
            'lasso': Lasso(alpha=self.config.alpha,fit_intercept=self.config.fit_intercept),
            'neighbors': KNeighborsRegressor(n_neighbors=self.config.n_neighbors,weights=self.config.weights,algorithm=self.config.algorithm,p=self.config.p),
            'svm': SVR(kernel=self.config.kernel,C=self.config.C,gamma=self.config.gamma,epsilon=self.config.epsilon)
        }
        
        for name, model in models.items():
            try:
                model.fit(x_train, y_train)
                params = model.get_params()
                save_models(model, os.path.join(self.config.root_url,f'{name}.joblib'))
                save_parameters(params, os.path.join(self.config.root_url,'params.json'))
            except Exception as e:
                raise CustomException(e,sys)