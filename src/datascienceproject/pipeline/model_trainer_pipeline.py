from src.datascienceproject import logger
from src.datascienceproject.config.configuration import ConfigurationManager
from src.datascienceproject.components.model_trainer import ModelTrainer

STAGE = 'Model Training Stage'

class ModeTrainerPipeline:
    def __init__(self):
        pass
    
    def initiate_model_training(self):

        config = ConfigurationManager()
        data_validation_config = config.get_model_training_config()
        data_validation = ModelTrainer(data_validation_config)
        data_validation.train()
        

if __name__ == '__main__':
    try:
        logger.info(f'>>>>>>>>  {STAGE} starting <<<<<<<<')
        obj = ModeTrainerPipeline()
        obj.initiate_model_training()
        logger.info(f'>>>>>>>>  {STAGE} completed <<<<<<<<\n\nx=============x')
    except Exception as e:
        logger.exception(e)
        raise e