import mysql.connector
import os
from dotenv import load_dotenv

LOG_FILE = "log.md"

def log_query(query, result="none"):
    with open(LOG_FILE, "a") as file:
        file.write(f"```sql\n{query}\n```\n\n")
        file.write(f"```response from mysql database\n{result}\n```\n\n")

def connect_to_database(host, port,user, password, database):
    connection = mysql.connector.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database
    )
    return connection

def run_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    
    # If the query returns data, fetch and print the results
    if cursor.description:
        results = cursor.fetchall()
        for row in results:
            print(row)
    else:
        print("Query executed successfully!")

    return results
    cursor.close()

def test_query():
    # Database credentials
    load_dotenv()
    host = os.getenv("SERVER_HOSTNAME")
    port = os.getenv("SERVER_PORT")
    user = os.getenv("USER_NAME")
    password = os.getenv("ACCESS_TOKEN")
    database = os.getenv("DATABASE_NAME")

 #   host = input("Enter host: ")
 #   port = input("Enter port: ")
 #   user = input("Enter user: ")
 #   password = input("Enter password: ")
 #   database = input("Enter database name: ")

    # Connect to the database
    connection = connect_to_database(host, port,user, password, database)

    # Run queries from the terminal
        query="select city,count(city) from Bars b left join (select s.bar from Sells s where s.price >5) a on a.bar=b.name where a.bar IS NULL group by city"

        run_query(connection, query)

    # Close the connection
    connection.close()
    log_query(f"{query}", results)
