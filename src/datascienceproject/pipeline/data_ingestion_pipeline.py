from src.datascienceproject.config.configuration import ConfigurationManager
from src.datascienceproject.components.data_ingestion import DataIngestion
from src.datascienceproject import logger

STAGE = 'Data Ingestion Stage'

class DataIngestionTrainingPipline:
    
    def __init__(self):
        pass
    
    def initiate_data_ingestion(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_data()
        data_ingestion.extract_zip_file()
        
if __name__ == '__main__':
    try:
        logger.info('>>>>>>>>  {STAGE} starting <<<<<<<<')
        obj = DataIngestionTrainingPipline()
        obj.initiate_data_ingestion()
        logger.info('>>>>>>>>  {STAGE} completed <<<<<<<<\n\nx=============x')
    except Exception as e:
        logger.exception(e)
        raise e