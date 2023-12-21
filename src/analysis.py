#import pandas;
import psycopg2;
from psycopg2 import sql;

database_params = {
    "host": "localhost",
    "port": "5432",
    "database": "Youtube",
    "user": "postgres",
    "password": "root"
}

def create_connection():
    try:
        connection = psycopg2.connect(**database_params)
        print("Connected to the database")
        return connection
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL:", error)
        return None

def close_connection(connection):
    if connection:
        connection.close()
        print("Connection closed")

def execute_query(connection, query):
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
    except (Exception, psycopg2.Error) as error:
        print("Error executing query:", error)
        return None

if __name__ == "__main__":
    #csv filr path
    file_path = 'D:\Priyanka\Data Engineering\Youtube-trend-analysis\source_data\IN_youtube_trending_data.csv'
    
    # Example query to select data from a table
    select_query = sql.SQL("SELECT * FROM silver.youtube_videos;")

    # Establish a connection
    connection = create_connection()

    # Execute the query
    if connection:
        result = execute_query(connection, select_query)
        if result:
            print("Query result:", result)

    # Close the connection
    close_connection(connection)


#df = pandas.read_csv('D:\Priyanka\Data Engineering\Youtube-trend-analysis\source_data\IN_youtube_trending_data.csv')
#print(df.dtypes)
