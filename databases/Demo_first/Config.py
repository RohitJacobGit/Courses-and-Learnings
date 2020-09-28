import mysql.connector
from mysql.connector import Error
import pandas as pd


# def create_server_connection(host_name, user_name, user_password):
#     connection = None
#     try:
#         connection = mysql.connector.connect(
#             host=host_name,
#             user=user_name,
#             passwd=user_password
#         )
#         print("MySQL Database connection successful")
#     except Error as err:
#         print(f"Error: '{err}'")
#     return connection


# After we created a databases

def create_server_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print('Database created successfully!')
    except Error as err:
        print(err)


def execute_query_list(connection, query):

    for q in query:
        cursor = connection.cursor()
        try:
            cursor.execute(q)
            connection.commit()
            print('Query executed successfully!')
        except Error as err:
            print(f"Error: '{err}'")

def execute_query(connection, query):

    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print('Query executed successfully!')
    except Error as err:
        print(f"Error: '{err}'")

def read_table(connection, query):
    
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")

# connection = create_server_connection('localhost', 'root', 'Ro@mysql@081')
# query = 'CREATE DATABASE python_integration'
# create_database(connection, query)

# connection = create_server_connection('localhost', 'root', 'Ro@mysql@081', 'python_integration')
