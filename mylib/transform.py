import pandas as pd

def transform_data(df):
    """
    Perform data transformation such as handling missing values and renaming columns.

    Args:
        df (pd.DataFrame): Input DataFrame to transform.

    Returns:
        pd.DataFrame: Transformed DataFrame.
    """
    try:
        # Handle missing values
        df = df.fillna({
            'Gender': 'Unknown',
            'Year': 0,
            'Hero': 'Unnamed'
        })

        # Rename columns for consistency
        df = df.rename(columns={
            'Gender': 'Hero_Gender',
            'Year': 'Active_Year',
            'Hero': 'Hero_Name'
        })

        print("Data transformation complete.")
        return df
    except Exception as e:
        print(f"Error transforming data: {e}")
        return None

if __name__ == "__main__":
    # Example usage
    file_path = "data/avengers.csv"

    # Load the data
    try:
        data = pd.read_csv(file_path, encoding="ISO-8859-1")
        print("Data loaded for transformation.")
    except FileNotFoundError:
        print(f"File not found at {file_path}")
    except Exception as e:
        print(f"Error loading data: {e}")
        data = None

    if data is not None:
        # Transform the data
        transformed_data = transform_data(data)

        # Display transformed data
        if transformed_data is not None:
            print(transformed_data.head())
