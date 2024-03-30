from src.mlproject.components.data_ingestion import DataIngestion
from src.mlproject.components.data_transformation import DataTransformation
from src.mlproject.components.model_trainer import ModelTrainer

data_inges= DataIngestion()
raw_data=data_inges.initiate_data_ingestion()

data_transfom=DataTransformation()
train_arr, test_arr =data_transfom.initialize_data_transformation(raw_data)

model = ModelTrainer()
model.initiate_model_trainer(train_arr, test_arr)