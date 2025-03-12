from cnnClassifier.constants import CONFIG_FILE_PATH,PARAMS_FILE_PATH
from cnnClassifier.utils.common import read_yaml, create_directories
from cnnClassifier.entity.config_entity import DataIngestionConfig,BaseModelConfig
from pathlib import Path

class ConfigurationManager:
    def __init__(
            self,
            config_filepath = CONFIG_FILE_PATH,# access the config.yaml file and the params.yaml file from their paths and store them
            params_filepath = PARAMS_FILE_PATH):

            self.config = read_yaml(config_filepath)# read the yaml files using the custorm read_yaml function
            self.params = read_yaml(params_filepath)# the function returns a configBox datatype 

            create_directories([self.config.artifacts_root]) # creates a directory called artifacts root as stated in the config.yaml file

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion # using the configBox accessing method we can access the data_ingestion key inside the config file

        create_directories([config.root_dir]) # create a the root directory as mentioned in the config file

        data_ingestion_config = DataIngestionConfig( # use the previously created frozen entity for managing the data ingestion variables
            root_dir = config.root_dir,# access the information stored int he config  file and read it into respective  variables one by one
            source_URL = config.source_URL,
            local_data_file = config.local_data_file,
            unzip_dir = config.unzip_dir
        )
        
        return data_ingestion_config
    
    def get_base_model_config(self) -> BaseModelConfig:
        config = self.config.prepare_base_model

        create_directories([config.root_dir])

        base_model_config = BaseModelConfig(
            root_dir=Path(config.root_dir),
            base_model_path=Path(config.base_model_path),
            updated_base_model_path=Path(config.updated_base_model_path),
            params_image_size=self.params.IMAGE_SIZE,
            params_learning_rate=self.params.LEARNING_RATE,
            params_include_top=self.params.INCLUDE_TOP,
            params_weights=self.params.WEIGHTS,
            params_classes=self.params.CLASSES
            )
        return base_model_config