"""Query the BarBeerDrinker database from a mysql database"""
import mysql.connector
import os
from dotenv import load_dotenv

LOG_FILE = "log.md"

def log_query(query, result="none"):
    """adds to a query markdown file"""
    with open(LOG_FILE, "a") as file:
        file.write(f"```sql\n{query}\n```\n\n")
        file.write(f"```response from mysql database\n{result}\n```\n\n")

def connect_to_database(host, port,user, password, database):
  """Connect to the database"""
    connection = mysql.connector.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database
    )
    return connection

def run_query(connection, query):
    """run a query"""
    cursor = connection.cursor()
    cursor.execute(query)
    
    # If the query returns data, fetch and print the results
    if cursor.description:
        results = cursor.fetchall()
        for row in results:
            print(row)
    else:
        print("Query executed successfully!")
    
    cursor.close()

def test_query():
    """main function to test the output of a query"""
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
    while True:
        query = input("enter query:")
        if query.lower() == 'exit':
            break
        run_query(connection, query)

    # Close the connection
    connection.close()
