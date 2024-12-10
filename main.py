# main.py
from mylib.extract import extract_data
from mylib.transform import transform_data
from mylib.load import load_data
from mylib.query import query_data

def main():
    # Step 1: Extract data
    raw_data = extract_data()
    print("Data extraction completed.")

    # Step 2: Transform data
    transformed_data = transform_data(raw_data)
    print("Data transformation completed.")

    # Step 3: Load data
    load_data(transformed_data)
    print("Data loading completed.")

    # Step 4: Query data
    query_results = query_data()
    print("Data query completed.")
    print("Query Results:")
    print(query_results)

if __name__ == "__main__":
    main()


# from pyspark.sql import SparkSession
# from extract import extract_avengers_data
# from transform import transform_data
# from load import load_data

# def main():
#     """
#     Main function to orchestrate the ETL pipeline for Avengers data on Databricks using DBFS.
#     """
#     # Initialize SparkSession
#     spark = SparkSession.builder.appName("Avengers ETL Pipeline with DBFS").getOrCreate()

#     # Configurations
#     database_name = "Avengers_Data"  # Databricks database name
#     source_table_name = "avengers_stats"  # Source table name after extraction
#     transformed_table_name = "avengers_transformed"  # Transformed table name
#     final_table_name = "avengers_filtered"  # Final filtered table name
#     dbfs_file_path = "dbfs:/mnt/data/avengers.csv"  # DBFS path for raw data
#     raw_data_url = (
#         "https://github.com/nogibjj/Eric_Ortega_Rodriguez_Mini_Project_6/raw/main/data/avengers.csv"
#     )  # File URL for Avengers data

#     try:
#         # Step 1: Upload CSV to DBFS
#         print("Uploading raw CSV to DBFS...")
#         upload_file_to_dbfs(raw_data_url, dbfs_file_path)
#         print("Raw CSV uploaded to DBFS.")

#         # Step 2: Extract data from DBFS
#         print("Starting data extraction...")
#         extract_avengers_data(source_table_name, database=database_name, file_path=dbfs_file_path)
#         print("Data extraction completed.")

#         # Step 3: Transform data
#         print("Starting data transformation...")
#         transform_data(database_name, source_table_name, transformed_table_name)
#         print("Data transformation completed.")

#         # Step 4: Load data
#         print("Starting data load...")
#         load_data(database_name, transformed_table_name)
#         print("Data load completed.")

#     except Exception as e:
#         print(f"ETL pipeline failed: {e}")
#         raise

# def upload_file_to_dbfs(source_url, dbfs_path):
#     """
#     Uploads a file from a URL to DBFS.

#     Args:
#         source_url (str): URL of the file to upload.
#         dbfs_path (str): DBFS destination path.

#     Returns:
#         None
#     """
#     import requests
#     # Convert dbfs:/ path to /dbfs/ for local file system operations
#     local_path = "/dbfs" + dbfs_path[5:]  
#     print(f"Downloading file from {source_url} to {local_path}...")

#     # Download file and write it to the DBFS path
#     with requests.get(source_url, stream=True) as r:
#         if r.status_code == 200:
#             with open(local_path, "wb") as f:
#                 for chunk in r.iter_content(chunk_size=8192):
#                     f.write(chunk)
#             print(f"File successfully saved to {local_path}")
#         else:
#             raise Exception(f"Failed to download file from {source_url}. HTTP status code: {r.status_code}")

# if __name__ == "__main__":
#     main()
