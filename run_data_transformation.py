from src.components.data_transformation import DataTransformation
import os

# Paths to your train and test CSV files
train_path = os.path.join('artifacts', 'train.csv')  # update path if needed
test_path = os.path.join('artifacts', 'test.csv')    # update path if needed

# Create an instance of your DataTransformation class
data_transformation = DataTransformation()

# Run the method to fit the pipeline and save preprocessor.pkl
train_arr, test_arr, preprocessor_path = data_transformation.initiate_data_transformation(
    train_path=train_path,
    test_path=test_path
)

print(f"Data transformation completed. Preprocessor saved at: {preprocessor_path}")
