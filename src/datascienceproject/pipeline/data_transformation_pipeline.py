from src.datascienceproject import logger
from src.datascienceproject.components.data_transformation import DataTransformation
from src.datascienceproject.config.configuration import ConfigurationManager

STAGE = 'Data Transformation Stage'

class DataTransformationPipeline():
    def __init__(self):
        pass
    
    def initiate_data_transformation(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(data_transformation_config)
        data_transformation.train_test_splitting()


if __name__ == '__main__':
    try:
        logger.info(f'>>>>>>>>  {STAGE} starting <<<<<<<<')
        obj = DataTransformationPipeline()
        obj.initiate_data_transformation()
        logger.info(f'>>>>>>>>  {STAGE} completed <<<<<<<<\n\nx=============x')
    except Exception as e:
        logger.exception(e)
        raise e