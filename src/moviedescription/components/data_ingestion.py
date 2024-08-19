import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import StratifiedShuffleSplit
import json

@dataclass
class DataIngestionConfig:
    raw_data_path: str = os.path.join("artifacts", "movies_data.json")
    train_data_path: str = os.path.join("artifacts", "train.csv")
    test_data_path: str = os.path.join("artifacts", "test.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()  # Data ingestion config object

    def remove_duplicates(self, df):
        logging.info("Removing duplicate images from the dataset")
        # Assuming 'cover' is the column with image paths
        df.drop_duplicates(subset=['cover'], keep='first', inplace=True)
        logging.info(f"Dataset size after removing duplicates: {df.shape}")
        return df

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            # Load the JSON dataset
            with open(self.ingestion_config.raw_data_path, "r") as f:
                data = json.load(f)
            logging.info("Read the dataset as a JSON object")

            # Convert JSON to DataFrame
            df = pd.DataFrame(data)
            logging.info("Converted JSON data to a DataFrame")

            # Ensure that the 'cover' field includes full paths to the images
            df['cover'] = df['cover'].apply(lambda x: os.path.join("C:\\Users\\user\\Desktop\\movie_ML_project\\notebook\\data\\", x))
            logging.info("Updated the 'cover' field to include full image paths")

            # Remove duplicate entries
            df = self.remove_duplicates(df)

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            # Save the raw data as a JSON file
            df.to_json(self.ingestion_config.raw_data_path, orient="records", lines=True)
            logging.info(f"Saved the raw data at {self.ingestion_config.raw_data_path}")

            # Stratified Split (Active)
            stratified_split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
            for train_index, test_index in stratified_split.split(df, df['genre']):
                train_df = df.loc[train_index]
                test_df = df.loc[test_index]
            logging.info("Performed Stratified Split")

            # Time Series Split (Commented)
            """
            # from sklearn.model_selection import TimeSeriesSplit
            # tscv = TimeSeriesSplit(n_splits=5)
            # for train_index, test_index in tscv.split(df):
            #     train_df = df.loc[train_index]
            #     test_df = df.loc[test_index]
            # logging.info("Performed Time Series Split")
            """

            # K-Fold Cross-Validation (Commented)
            """
            # from sklearn.model_selection import KFold
            # kf = KFold(n_splits=5, shuffle=True, random_state=42)
            # for fold, (train_index, test_index) in enumerate(kf.split(df)):
            #     train_df = df.loc[train_index]
            #     test_df = df.loc[test_index]
            #     logging.info(f"Performed K-Fold Cross-Validation for fold {fold + 1}")
            """

            # Leave-One-Out (LOO) (Commented)
            """
            # from sklearn.model_selection import LeaveOneOut
            # loo = LeaveOneOut()
            # for train_index, test_index in loo.split(df):
            #     train_df = df.loc[train_index]
            #     test_df = df.loc[test_index]
            # logging.info("Performed Leave-One-Out Cross-Validation")
            """

            # Monte Carlo Cross-Validation (Commented)
            """
            # from sklearn.model_selection import ShuffleSplit
            # mc_cv = ShuffleSplit(n_splits=10, test_size=0.2, random_state=42)
            # for i, (train_index, test_index) in enumerate(mc_cv.split(df)):
            #     train_df = df.loc[train_index]
            #     test_df = df.loc[test_index]
            #     logging.info(f"Performed Monte Carlo Cross-Validation iteration {i + 1}")
            """

            # Nested Cross-Validation (Commented)
            """
            # from sklearn.model_selection import KFold
            # inner_cv = KFold(n_splits=5, shuffle=True, random_state=42)
            # outer_cv = KFold(n_splits=5, shuffle=True, random_state=42)
            # for outer_train_index, outer_test_index in outer_cv.split(df):
            #     outer_train_df = df.loc[outer_train_index]
            #     outer_test_df = df.loc[outer_test_index]
            #     for inner_train_index, inner_test_index in inner_cv.split(outer_train_df):
            #         inner_train_df = outer_train_df.loc[inner_train_index]
            #         inner_test_df = outer_train_df.loc[inner_test_index]
            #         logging.info(f"Performed Nested Cross-Validation")
            """

            # Grouped Split (Commented)
            """
            # from sklearn.model_selection import GroupShuffleSplit
            # group_split = GroupShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
            # for train_index, test_index in group_split.split(df, groups=df['group_column']):
            #     train_df = df.loc[train_index]
            #     test_df = df.loc[test_index]
            # logging.info("Performed Grouped Split")
            """

            # Save the train and test sets as CSV files
            train_df.to_csv(self.ingestion_config.train_data_path, index=False)
            test_df.to_csv(self.ingestion_config.test_data_path, index=False)

            logging.info("The train and test data are saved")

            return self.ingestion_config.train_data_path, self.ingestion_config.test_data_path

        except Exception as e:
            raise CustomException(e, sys)

if __name__ == "__main__":
    ingestion = DataIngestion()
    train_data_path, test_data_path = ingestion.initiate_data_ingestion()
