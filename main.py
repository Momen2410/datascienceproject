from src.datascienceproject import logger
from src.datascienceproject.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipline
from src.datascienceproject.pipeline.data_validation_pipeline import DataValidationTrainingPipline
import ssl
ssl._create_default_https_context = ssl._create_unverified_context



STAGE = 'Data Ingestion Stage'
try:
    logger.info(f'>>>>>>>>  {STAGE} starting <<<<<<<<')
    obj = DataIngestionTrainingPipline()
    obj.initiate_data_ingestion()
    logger.info(f'>>>>>>>>  {STAGE} completed <<<<<<<<\n\nx=============x')
except Exception as e:
    logger.exception(e)
    raise e


STAGE = 'Data Validation Stage'
try:
    logger.info(f'>>>>>>>>  {STAGE} starting <<<<<<<<')
    obj = DataValidationTrainingPipline()
    obj.initiate_data_validation()
    logger.info(f'>>>>>>>>  {STAGE} completed <<<<<<<<\n\nx=============x')
except Exception as e:
    logger.exception(e)
    raise e