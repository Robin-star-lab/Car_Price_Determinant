from sklearn.model_selection import train_test_split
from src.Car_Price_Pred.utils.common import load_models,save_best_model,save_scores
from sklearn.metrics import r2_score
from src.Car_Price_Pred.entities import ModelEvaluationConfig
import os
import pandas as pd
from logger import my_logger







class ModelEvaluation():
    def __init__(self, config = ModelEvaluationConfig):
        self.config = config
        
    def evaluate_model(self):
        test_data = pd.read_csv(self.config.evaluation_data)
        
        test_data.fillna(test_data.mean(),inplace=True)
        
        self.x_test = test_data.iloc[:,:-1]
        self.y_test = test_data.iloc[:,-1]
        x_train,x_test,y_train,y_test = train_test_split(self.x_test,self.y_test,test_size=0.3,random_state=42)
        
        models = [
            load_models(self.config.decision_tree),
            load_models(self.config.lasso),
            load_models(self.config.linear_regression),
            load_models(self.config.neighbors),
            load_models(self.config.svm),
            load_models(self.config.random_forest)]
        
        best_model = None
        best_score = 0
        
        for model in models:
            model.fit(x_train,y_train)
            self.y_predict = model.predict(x_test)
            score = r2_score(y_test,self.y_predict)
            if score > best_score:
                best_model = model
                best_score = score
        
        save_best_model(best_model,os.path.join(self.config.best_model_path,f"{best_model}_.joblib"))
        my_logger.info(f"Best Model is {best_model} with scores : {best_score}")
        save_scores(f"r_2score:{best_score}",os.path.join(self.config.scores_path,'scores.txt'))
        
        