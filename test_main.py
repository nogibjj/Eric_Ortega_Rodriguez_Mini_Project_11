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
        cls.file_path = "test_data/avengers.csv"
        cls.test_url = (
            "https://raw.githubusercontent.com/nogibjj/Eric_Ortega_Rodriguez_Mini_Project_11/"
            "main/data/avengers.csv"
        )
        cls.test_column, cls.test_value = "Hero_Gender", "Male"

    def test_extract_data(self):
        result = extract_data(self.file_path, self.test_url)
        self.assertTrue(os.path.exists(result), "File not downloaded or located.")

    def test_load_data(self):
        extract_data(self.file_path, self.test_url)
        df = load_data(self.file_path)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertGreater(len(df), 0, "DataFrame is empty.")

    def test_transform_data(self):
        extract_data(self.file_path, self.test_url)
        raw_data = load_data(self.file_path)
        transformed_data = transform_data(raw_data)
        self.assertIn("Hero_Gender", transformed_data.columns)
        self.assertIn("Active_Year", transformed_data.columns)
        self.assertIn("Hero_Name", transformed_data.columns)
        self.assertNotIn("Gender", transformed_data.columns)

    def test_query_data(self):
        extract_data(self.file_path, self.test_url)
        raw_data = load_data(self.file_path)
        transformed_data = transform_data(raw_data)
        queried_data = query_data(transformed_data, self.test_column, self.test_value)
        self.assertIsInstance(queried_data, pd.DataFrame)
        self.assertGreaterEqual(len(queried_data), 0)
        self.assertTrue(all(queried_data[self.test_column] == self.test_value))

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.file_path):
            os.remove(cls.file_path)
        if os.path.exists("test_data"):
            os.rmdir("test_data")

if __name__ == "__main__":
    unittest.main()
