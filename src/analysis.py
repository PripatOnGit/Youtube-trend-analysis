
import psycopg2;
from psycopg2 import sql;
import csv;

#database Parameters
database_params = {
    "host": "localhost",
    "port": "5432",
    "database": "Youtube",
    "user": "postgres",
    "password": "root"
}

#function to create database connection
def create_connection():
    try:
        connection = psycopg2.connect(**database_params)
        print("Connected to the database")
        return connection
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL:", error)
        return None

#function to close database connection
def close_connection(connection):
    if connection:
        connection.close()
        print("Connection closed")

#function to execute query.
def execute_query(connection, query):
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
    except (Exception, psycopg2.Error) as error:
        print("Error executing query:", error)
        return None
    

#query to insert non-duplicate data in tables
def insert_data(connection, table_name, data):
    unique_keys = set()
    try:
        with connection.cursor() as cursor:
            # Construct the INSERT INTO query using sql.SQL
            query = sql.SQL("INSERT INTO silver.{} (video_id,title ,publishedAt,channelId,channelTitle, categoryId,trending_date,tags,view_count,likes,dislikes,comment_count,thumbnail_link,comments_disabled,ratings_disabled,description) VALUES (%s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);").format(sql.Identifier(table_name))

            # Execute the query for each row of data
            for row in data:
                key = row[0]
                if key not in unique_keys:
                    cursor.execute(query, row)
                    unique_keys.add(key)
                else:
                    print(f"Skipping duplicate keys: {key}")

        connection.commit()
        print("Data inserted successfully")
    except (Exception, psycopg2.Error) as error:
        print("Error inserting data:", error)

def read_csv(file_path, encoding='utf-8'):
    with open(file_path, 'r', newline='', encoding=encoding) as csvfile:
        reader = csv.reader(csvfile)
        # Skip the header if it exists
        next(reader, None)
        return [row for row in reader]
    

if __name__ == "__main__":
    
    # Replace 'your_table' and 'your_data.csv' with actual values
    table_name = 'youtube_videos'
    csv_file_path = 'D:\Priyanka\Data Engineering\Youtube-trend-analysis\source_data\IN_youtube_trending_data.csv'

    # Establish a connection
    connection = create_connection()

    if connection:
        # Read data from the CSV file
        csv_data = read_csv(csv_file_path, encoding='utf-8')

        # Insert data into the PostgreSQL database
        insert_data(connection, table_name, csv_data)

        # Close the connection
        close_connection(connection)


