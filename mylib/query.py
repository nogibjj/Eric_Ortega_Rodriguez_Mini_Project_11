import os
from databricks import sql
from dotenv import load_dotenv

# Global variable for the log file
LOG_FILE = "query_log.md"

def log_query(query, result="none"):
    """Adds to a query markdown file."""
    with open(LOG_FILE, "a") as file:
        file.write(f"```sql\n{query}\n```\n\n")
        if result != "none":
            if isinstance(result, str):  # In case result is an error message
                file.write(f"```response from databricks\n{result}\n```\n\n")
            else:
                result_str = "\n".join(
                    [", ".join(map(str, row)) for row in result]
                )
                file.write(f"```response from databricks\n{result_str}\n```\n\n")
        else:
            file.write(f"```response from databricks\n{result}\n```\n\n")

def general_query(query):
    """Runs a user-defined query and logs the result."""
    
    load_dotenv()
    server_hostname = os.getenv("server_host")
    access_token = os.getenv("databricks_api_key")
    http_path = os.getenv("sql_path")

    result = "none"
    
    try:
        with sql.connect(
            server_hostname=server_hostname,
            http_path=http_path,
            access_token=access_token
        ) as conn:
            with conn.cursor() as c:
                c.execute(query)
                result = c.fetchall()
                
    except Exception as e:
        result = f"Error: {str(e)}"
        print(f"Query execution failed: {str(e)}")
    
    log_query(query, result)
