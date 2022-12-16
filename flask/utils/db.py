import mysql.connector
from utils.secrets import MYSQL_USERNAME, MYSQL_PASSWORD

def connect():
    db = mysql.connector.connect(
        host="localhost",
        port=3306,
        user=MYSQL_USERNAME,
        password=MYSQL_PASSWORD,

    )

    return db
