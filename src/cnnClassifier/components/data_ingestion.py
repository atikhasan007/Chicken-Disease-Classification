import os
import zipfile
import gdown

from pathlib import Path
from src.cnnClassifier import logger

from src.cnnClassifier.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    # 🔥 NEW: Google Drive downloader (S3 replace)
    def download_from_gdrive(self, file_id):
        try:
            logger.info(f"Downloading data from Google Drive...")

            url = f"https://drive.google.com/uc?id={file_id}"

            gdown.download(
                url,
                self.config.local_data_file,
                quiet=False
            )

            logger.info(
                f"Downloaded data from Google Drive to {self.config.local_data_file}"
            )

        except Exception as e:
            logger.error(f"Error downloading from Google Drive: {e}")
            raise e

    # 🔥 SAME AS BEFORE (UNCHANGED OUTPUT)
    def extract_zip_file(self):
        try:
            unzip_path = self.config.unzip_dir
            os.makedirs(unzip_path, exist_ok=True)

            with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref:
                zip_ref.extractall(unzip_path)

            logger.info(f"Extracted data at: {unzip_path}")

        except Exception as e:
            logger.error(f"Error extracting zip file: {e}")
            raise e

