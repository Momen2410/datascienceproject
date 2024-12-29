import os
from sklearn.linear_model import ElasticNet
from src.datascienceproject import logger
import joblib
import pandas as pd
from src.datascienceproject.config.configuration import ModelTrainerConfiguration


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfiguration):
        self.config = config
        
    def train(self):
        
        train_data = pd.read_csv(self.config.train_data)
        test_data = pd.read_csv(self.config.test_data)
        
        train_X = train_data.drop([self.config.target_columns], axis=1)
        train_y = train_data[[self.config.target_columns]]
        
        test_X = test_data.drop([self.config.target_columns], axis=1)
        test_y = test_data[[self.config.target_columns]]
        
        lr = ElasticNet(alpha=self.config.alpha, l1_ratio=self.config.l1_ratio)
        lr.fit(train_X, train_y)
        
        joblib.dump(lr, os.path.join(self.config.root_dir, self.config.model_name))