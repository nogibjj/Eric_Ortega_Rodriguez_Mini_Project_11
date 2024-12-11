# main.py
from mylib.extract import extract_data
from mylib.transform import transform_data
from mylib.load import extract_data
from mylib.query import query_data

def main():
    # Step 1: Extract data
    #raw_data = extract_data()
    print("Data extraction completed.")

    # Step 2: Transform data
    #transformed_data = transform_data(raw_data)
    print("Data transformation completed.")

    # Step 3: Load data
    extract_data(transformed_data)
    print("Data loading completed.")

    # Step 4: Query data
    query_results = query_data()
    print("Data query completed.")
    print("Query Results:")
    print(query_results)

if __name__ == "__main__":
    main()
