from housing.exception import HousingException
from housing.logger import logging
from housing.pipeline.pipeline import Pipeline
from housing.config.configuration import Configuration
from housing.component.data_transformation import DataTransformation

def main():
    try :

        pipeline = Pipeline()
        # pipeline.run_pipeline()
        pipeline.start()
        logging.info("main function execution completed  ")
        ## for data validation
        # data_validation_config = Configuration().get_data_ingestion_config()
        # print(data_validation_config)
       
        ## for data transformation
        # data_transformation_config = Configuration().get_data_transformation_config()
        # print(data_transformation_config)
        # schema_file_path = r"C:\Users\amit.singh\Desktop\ML_project\machine_learning_project\config\schema.yaml"
        # file_path = r"C:\Users\amit.singh\Desktop\ML_project\machine_learning_project\housing\artifact\data_ingestion\2022-07-04-21-12-04\ingested_data\train\housing.csv"
    
        # df = DataTrasformation.load_data(file_path=file_path, schema_file_path=schema_file_path)
        # print(df.columns)
        # print(df.dtypes)
    
    except Exception as e:
        logging.error(f"{e}")
        print(e)
if __name__=="__main__":
    main()
