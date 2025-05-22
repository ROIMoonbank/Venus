# connect to spanner database called inventory on the instance demo in the multiregion eur3 in project roimb-2025 
# query the table names and return the top 5 names alphabetical
from google.cloud import spanner

def list_tables(instance_id, database_id):
    """Lists tables in the database."""
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    with database.snapshot() as snapshot:
        results = snapshot.execute_sql(
            "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = '' ORDER BY TABLE_NAME LIMIT 5"
        )
        for row in results:
            print(row[0])

if __name__ == '__main__':
    list_tables('demo', 'inventory')
    