from mylib.extract import extract_data
from mylib.load import load_data
from mylib.transform import transform_data
from mylib.query import query_data

def main():
    # File path for data
    file_path = "data/avengers.csv"

    # Step 1: Extract data
    extract_data(file_path)
    print("Data extraction completed.")

    # Step 2: Load data
    raw_data = load_data(file_path)
    if raw_data is None:
        print("Failed to load data. Exiting.")
        return

    # Step 3: Transform data
    transformed_data = transform_data(raw_data)
    if transformed_data is None:
        print("Failed to transform data. Exiting.")
        return
    print("Data transformation completed.")

    # Step 4: Query data
    query_results = query_data(transformed_data, column="Hero_Gender", value="Male")
    if query_results is not None:
        print("Query Results:")
        print(query_results.head())

if __name__ == "__main__":
    main()

