from dotenv import load_dotenv
from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import general_query

def main():
    load_dotenv()

    print("Extracting data....")
    extract()

    print("Transforming data...")
    load()

    print("Querying data from Databricks...")
    query = '''
        SELECT 
            a.`Name/Alias`, 
            SUM(a.Appearances) AS total_appearances, 
            COUNT(b.battle_id) AS total_battles
        FROM 
            Avengers a
        JOIN 
            Battles b ON a.avenger_id = b.avenger_id
        GROUP BY 
            a.`Name/Alias`
        HAVING 
            SUM(a.Appearances) > 100
        ORDER BY 
            total_battles DESC, total_appearances DESC
    '''
    general_query(query)

if __name__ == "__main__":
    main()



# import os
# from dotenv import load_dotenv
# from databricks import sql

# # Import your functions
# from mylib.extract import extract
# from mylib.query import general_query
# from mylib.transform_load import load

# def main():
#     # Load environment variables
#     load_dotenv()

#     # Extract data
#     print("Extracting data....")
#     extract()

#     # Transform and Load data
#     print("Transforming data...")
#     load()

#     # Query data using Databricks connection
#     print("Querying data from Databricks...")
    
#     # Define a complex SQL query with joins, aggregation, and sorting
#     query = '''
#         SELECT 
#             a."Name/Alias", 
#             SUM(a.Appearances) AS total_appearances, 
#             COUNT(b.battle_id) AS total_battles
#         FROM 
#             Avengers a
#         JOIN 
#             Battles b ON a.avenger_id = b.avenger_id
#         GROUP BY 
#             a."Name/Alias"
#         HAVING 
#             SUM(a.Appearances) > 100  -- Only Avengers with more than 100 appearances
#         ORDER BY 
#             total_battles DESC, total_appearances DESC
#     '''
    
#     # Run the query and log the results
#     general_query(query)

# if __name__ == "__main__":
#     main()


# # # Paths and parameters for the new dataset
# # dataset_path = "data/avengers.csv"
# # db_name = "avengers.db"
# # table_name = "Avengers"

# # # Extract
# # print("Extracting data from the database...")
# # # Extract data directly from the database
# # data = extract(database=db_name, table=table_name)

# # # Transform and load
# # print("Transforming and loading data...")
# # # Load the CSV data into the database if necessary
# # load(dataset=dataset_path, db_name=db_name, table_name=table_name)

# # # Query
# # print("Querying data...")
# # results = query(database=db_name, table=table_name)

# # # Print query results
# # print("Top 5 rows from the Avengers table:")
# # for row in results:
# #     print(row)
