from src.cnnClassifier.config.configuration import ConfigurationManager
from src.cnnClassifier.components.data_ingestion import DataIngestion
from src.cnnClassifier import logger
import os
STAGE_NAME = "Data Ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()

            data_ingestion = DataIngestion(config=data_ingestion_config)

            file_id = "1d_TPOi0PY6tngaVhMpzDdVaG6Vo1FAg1"

            # 🔥 SAME STYLE AS S3 CALL
            data_ingestion.download_from_gdrive(file_id)

            data_ingestion.extract_zip_file()

        except Exception as e:
            raise e