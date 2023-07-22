import sqlite3

# Connect to the SQLite3 database
connection = sqlite3.connect("db.sqlite3")

# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# Execute a simple SQL query
cursor.execute("SELECT * FROM table_element")

# Fetch the results
results = cursor.fetchall()
print(results)

# Close the cursor and the connection
cursor.close()
connection.close()
