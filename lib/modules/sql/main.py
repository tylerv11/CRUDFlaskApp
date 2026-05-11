import pandas as pd
from databricks import sql
import os


class Databricks:

    def __init__(self,
                 query: str):

        # Connection details
        self.server_hostname = os.getenv("DATABRICKS_SERVER_HOSTNAME", "your-warehouse.cloud.databricks.com")
        self.http_path = os.getenv("DATABRICKS_HTTP_PATH", "/sql/1.0/warehouses/YOUR_WAREHOUSE_ID")
        self.access_token = os.getenv("DATABRICKS_ACCESS_TOKEN", "enter-your-databricks-token")
        self.query = query


    def run_query(self):
        # SQL Query
        query = self.query

        # Connect to Databricks SQL
        with sql.connect(
            server_hostname=self.server_hostname,
            http_path=self.http_path,
            access_token=self.access_token
        ) as connection:
            # Execute query
            with connection.cursor() as cursor:
                cursor.execute(query)
                # Fetch result and create DataFrame
                columns = [desc[0] for desc in cursor.description]  # Column names
                data = cursor.fetchall()  # Query rows
                df = pd.DataFrame(data, columns=columns)
                cursor.close()
                return df

