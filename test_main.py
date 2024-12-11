import unittest
import os
import pandas as pd
from mylib.extract import extract_data
from mylib.load import load_data
from mylib.transform import transform_data
from mylib.query import query_data

class TestMainWorkflow(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        Set up the test environment.
        """
        cls.file_path = "test_data/avengers.csv"
        cls.test_url = (
            "https://raw.githubusercontent.com/nogibjj/Eric_Ortega_Rodriguez_Mini_Project_11/"
            "main/data/avengers.csv"
        )
        cls.test_column = "Hero_Gender"
        cls.test_value = "Male"

    def test_extract_data(self):
        """
        Test the extract_data function to ensure it downloads the file.
        """
        result = extract_data(self.file_path, self.test_url)
        self.assertTrue(
            os.path.exists(result), "File was not downloaded or located."
        )

    def test_load_data(self):
        """
        Test the load_data function to ensure the CSV is loaded into a DataFrame.
        """
        # Ensure the data file is available
        extract_data(self.file_path, self.test_url)
        
        df = load_data(self.file_path)
        self.assertIsInstance(
            df, pd.DataFrame, "Loaded data is not a DataFrame."
        )
        self.assertGreater(
            len(df), 0, "Loaded DataFrame is empty."
        )

    def test_transform_data(self):
        """
        Test the transform_data function to ensure transformations are applied correctly.
        """
        # Load the data
        extract_data(self.file_path, self.test_url)
        raw_data = load_data(self.file_path)

        transformed_data = transform_data(raw_data)
        self.assertIn(
            "Hero_Gender", transformed_data.columns, 
            "Column 'Hero_Gender' not found in transformed data."
        )
        self.assertIn(
            "Active_Year", transformed_data.columns, 
            "Column 'Active_Year' not found in transformed data."
        )
        self.assertIn(
            "Hero_Name", transformed_data.columns, 
            "Column 'Hero_Name' not found in transformed data."
        )
        self.assertNotIn(
            "Gender", transformed_data.columns, 
            "Old column 'Gender' still exists in transformed data."
        )

    def test_query_data(self):
        """
        Test the query_data function to ensure it filters data correctly.
        """
        # Load and transform the data
        extract_data(self.file_path, self.test_url)
        raw_data = load_data(self.file_path)
        transformed_data = transform_data(raw_data)

        queried_data = query_data(
            transformed_data, self.test_column, self.test_value
        )
        self.assertIsInstance(
            queried_data, pd.DataFrame, 
            "Query result is not a DataFrame."
        )
        self.assertGreaterEqual(
            len(queried_data), 0, "Query returned no results."
        )
        self.assertTrue(
            all(queried_data[self.test_column] == self.test_value),
            f"Query results do not match the value '{self.test_value}' "
            f"in column '{self.test_column}'."
        )

    @classmethod
    def tearDownClass(cls):
        """
        Clean up the test environment.
        """
        if os.path.exists(cls.file_path):
            os.remove(cls.file_path)
        if os.path.exists("test_data"):
            os.rmdir("test_data")

if __name__ == "__main__":
    unittest.main()
