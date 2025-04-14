import sqlite3

# Connect to the database (creates it if it doesn't exist)
conn = sqlite3.connect('stayconnect.db')
cursor = conn.cursor()

# Create users table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
''')

# Create contact_messages table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS contact_messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        phone TEXT,
        email TEXT NOT NULL,
        message TEXT NOT NULL,
        confirmed BOOLEAN DEFAULT 0,
        submitted_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
''')

# Insert a sample test user
cursor.execute('''
    INSERT OR IGNORE INTO users (first_name, last_name, email, password)
    VALUES ('Test', 'User', 'test@example.com', 'password123')
''')

#Print all users
cursor.execute('SELECT * FROM users')
users = cursor.fetchall()
for user in users:
    print(user)

# Save and close
conn.commit()
conn.close()

print("Tables created and test user inserted.")
