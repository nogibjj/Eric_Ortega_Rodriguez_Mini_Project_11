import pandas as pd

def load_data(file_path):
    """
    Load the data from the given CSV file into a pandas DataFrame.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded data as a DataFrame.
    """
    try:
        df = pd.read_csv(file_path, encoding="ISO-8859-1")
        print(f"Data loaded successfully from {file_path}")
        return df
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def query_data(df, column, value):
    """
    Query the DataFrame for rows where the specified column matches the given value.

    Args:
        df (pd.DataFrame): The DataFrame to query.
        column (str): The column to filter on.
        value: The value to filter by.

    Returns:
        pd.DataFrame: Filtered DataFrame.
    """
    try:
        if column not in df.columns:
            print(f"Error: Column '{column}' not found in DataFrame")
            return None

        filtered_df = df[df[column] == value]
        print(f"Query successful: {len(filtered_df)} rows found.")
        return filtered_df
    except Exception as e:
        print(f"Error querying data: {e}")
        return None

if __name__ == "__main__":
    # Example usage
    file_path = "data/avengers.csv"

    # Load the data
    data = load_data(file_path)

    if data is not None:
        # Query the data
        queried_data = query_data(data, column="Gender", value="Male")

        # Display queried data
        if queried_data is not None:
            print(queried_data.head())
