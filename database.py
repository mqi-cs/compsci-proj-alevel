import sqlite3

# Connect to the database
conn = sqlite3.connect('wordle.db')

# Create a cursor
c = conn.cursor()

# Create the table if it doesn't exist
c.execute("""
CREATE TABLE IF NOT EXISTS wordle_list (
    word TEXT
)
""")

# Open the text file and read its content
with open('words_alpha.txt', 'r') as file:
    words = file.readlines()

# Insert each word into the database
for word in words:
    word = word.strip()  # Remove any surrounding whitespace
    c.execute("INSERT INTO wordle_list (word) VALUES (?)", (word,))

# Commit the transaction
conn.commit()

# Close the connection
conn.close()

