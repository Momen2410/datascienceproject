import urllib.request as request
from src.datascienceproject import logger
import os
import zipfile
from src.datascienceproject.config.configuration import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    def download_data(self):
        if not os.path.exists(self.config.local_data_file):
            filename, header = request.urlretrieve(url = self.config.url,
                                                   filename=self.config.local_data_file)
            logger.info(f'{filename} successfully downloded!')
        else:
            logger.info('file already exists')
            
    def extract_zip_file(self):
        
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)