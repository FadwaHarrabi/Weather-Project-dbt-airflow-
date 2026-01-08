from api_request import moch_fetch_data
import psycopg2

def connect_to_db():
    print("connecting to postressql database ...")
    try:
        conn=psycopg2.connect(host="localhost", port="5000", database="weather_data", user="postgres", password="system")
        print(conn)
    except psycopg2.Error as e:
        print(f"Error connecting to database: {e}")
        raise

connect_to_db()