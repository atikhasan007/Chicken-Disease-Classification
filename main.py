from src.cnnClassifier import logger


# from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.cnnClassifier.pipeline.stage_02_prepare_base_model import PrparBaseModelTrainingPipeline
from src.cnnClassifier.pipeline.stage_03_model_trainer import ModelTrainingPipeline
from src.cnnClassifier.pipeline.stage_04_model_evaluation  import EvaluationPipeline


STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>> stage{STAGE_NAME} completed <<<<<\n\nx=======")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Prepare base model"
try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<")
    data_ingestion = PrparBaseModelTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>> stage{STAGE_NAME} completed <<<<<\n\nx=======")

except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Trainer"
try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<")
    data_ingestion = ModelTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>> stage{STAGE_NAME} completed <<<<<\n\nx=======")

except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Evaluation"
try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<")
    data_ingestion = EvaluationPipeline()
    data_ingestion.main()
    logger.info(f">>>>> stage{STAGE_NAME} completed <<<<<\n\nx=======")

except Exception as e:
    logger.exception(e)
    raise e
