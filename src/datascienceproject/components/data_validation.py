from src.datascienceproject import logger
import os
from src.datascienceproject.config.configuration import DataValidationConfig
import pandas as pd

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config
    
    def validat_all_columns(self) -> bool:
        
        try:
            validation_status = None
            data = pd.read_csv(self.config.unzip_data_file)
            all_cols = list(data.columns)
            all_schemas = self.config.all_scheme.keys()
            
            for cols in all_cols:
                if cols not in all_schemas:
                    validation_status = False
                    with open(self.config.STATUS_file, 'w') as f:
                        f.write(f'Validation Status: {validation_status}')
                else:
                    validation_status = True
                    with open(self.config.STATUS_file, 'w') as f:
                        f.write(f'Validation Status: {validation_status}')
            
            return validation_status
        except Exception as e:
            logger.error(f'Error occurred while validating columns: {str(e)}')
            raise e
        