from src.datascienceproject.components.data_validation import DataValidation
from src.datascienceproject.config.configuration import ConfigurationManager
from src.datascienceproject import logger


STAGE = 'Data Validation Stage'

class DataValidationTrainingPipline:
    
    def __init__(self):
        pass
    
    def initiate_data_validation(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validat_all_columns()


if __name__ == '__main__':
    try:
        logger.info(f'>>>>>>>>  {STAGE} starting <<<<<<<<')
        obj = DataValidationTrainingPipline()
        obj.initiate_data_validation()
        logger.info(f'>>>>>>>>  {STAGE} completed <<<<<<<<\n\nx=============x')
    except Exception as e:
        logger.exception(e)
        raise e