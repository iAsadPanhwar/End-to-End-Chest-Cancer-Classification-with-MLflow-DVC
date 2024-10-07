from cnnCLassifier import logger
from cnnCLassifier.pipeline.Stage_01_data_ingestion import DataIngestionTrainingPipeline


STAGE_NAME = "Data Ingestion Step"

try:
    logger.info(f'>>>>>>>> stage {STAGE_NAME} started <<<<<<<<')
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f'>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<\n\n X===========X')
except Exception as e:
    logger.exception(e)
    raise e