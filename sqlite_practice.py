import sqlite3

# Create DB Object and cursor to create a local database
db = sqlite3.connect("books-collection.db")
cursor = db.cursor()

# Create a table
# cursor.execute("CREATE TABLE books "
#                "(id INTEGER PRIMARY KEY, "
#                "title varchar(250) NOT NULL UNIQUE, "
#                "author varchar(250) NOT NULL, "
#                "rating FLOAT NOT NULL)")

# Insert data into table
cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
db.commit()
