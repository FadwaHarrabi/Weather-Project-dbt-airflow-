from api_request import moch_fetch_data
import psycopg2

def connect_to_db():
    print("connecting to postressql database ...")
    try:
        conn=psycopg2.connect(
            host="localhost",
            port="5000",
            database="weather_data", 
            user="postgres", 
            password="system")
        return conn
    except psycopg2.Error as e:
        print(f"Error connecting to database: {e}")
        raise
def create_table(conn):
    print("Creating table if not exists ...")
    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE SCHEMA IF NOT EXISTS dev;
            CREATE TABLE IF NOT EXISTS dev.raw_weather_data (
                id SERIAL PRIMARY KEY,
                city VARCHAR(50),
                temperature FLOAT,
                weather_description VARCHAR(100),
                wind_speed FLOAT,
                time TIMESTAMP,
                inserted_at TIMESTAMP default NOW(),
                utc_offset TEXT);
            """)
        conn.commit()
        print("table was created successfully ...")
    except psycopg2.Error as e:
        print(f"Error creating table: {e}")
        raise



def insert_data(conn,data):
    print("Inserting data into the table ...")
    try:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO dev.raw_weather_data (city, temperature, weather_description, wind_speed, time, utc_offset)
            VALUES (%s, %s, %s, %s, %s, %s);
            """, (
                data['location']['name'],
                data['current']['temperature'],
                data['current']['weather_descriptions'][0],
                data['current']['wind_speed'],
                data['location']['localtime'],
                data['location']['utc_offset']
            ))
        conn.commit()
        print("Data inserted successfully ...")
    except psycopg2.Error as e:
        print(f"Error inserting data: {e}")
        raise
def main():
    try:
        data=moch_fetch_data()
        conn=connect_to_db()
        create_table(conn)
        insert_data(conn,data)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if 'conn' in locals() :
            conn.close()
            print("Database connection closed.")
main()
