from sklearn.linear_model import LinearRegression,Ridge,Lasso
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import sys
from Exceptions import CustomException
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from pathlib import Path
import joblib 
from src.Car_Price_Pred.config.configuration import ModelTrainingConfig
import os
from src.Car_Price_Pred.utils.common import save_models,save_parameters,save_scores
from logger import my_logger







# Model training configuration
class ModelTrainer():
    def __init__(self,config: ModelTrainingConfig):
        self.config = config
        
    def get_train_and_test_data(self):
        # Gathering the training and testing data
        train_data_path = self.config.train_data
        
        train = pd.read_csv(train_data_path,header=None)
        train.fillna(train.mean(),inplace=True)
        
        X = train.iloc[:,:-1]
        Y = train.iloc[:,-1]
        x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=0.3,random_state=42)
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
        best_model = None
        best_score = 0
        for name, model in models.items():
            try:
                model.fit(x_train, y_train)
                predictions = model.predict(x_test)
                params = model.get_params()
                score = r2_score(y_test, predictions)
                if score > best_score:
                    best_model = model
                    best_score = score
                save_models(best_model, os.path.join(self.config.root_url,f'{name}.joblib'))
                save_parameters(params, os.path.join(self.config.root_url,'params.json'))
                my_logger.info(f"Best Model is {best_model} with scores : {best_score}")
                save_scores(f"r_2score:{best_score}",os.path.join(self.config.scores_path,'scores.txt'))
            except Exception as e:
                raise CustomException(e,sys)